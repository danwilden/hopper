import math
import numpy
import random
import decimal
import scipy.linalg
import numpy.random as nrand
#mport matplotlib.pyplot as plt

class ModelParameters:
    #Holds all Params for all models


    def __init__(self,
                all_s0, all_time, all_delta, all_sigma, gbm_mu,
                 jumps_lamda=0.0, jumps_sigma=0.0, jumps_mu=0.0,
                 cir_a=0.0, cir_mu=0.0, all_r0=0.0, cir_rho=0.0,
                 ou_a=0.0, ou_mu=0.0,
                 heston_a=0.0, heston_mu=0.0, heston_vol0=0.0):
        #The starting value of the asset
        self.all_s0 = all_s0
        # The amount of time to run for
        self.all_time = all_time
        # This is the time delta, 1/252= daily 1/12= monthly, 1/1 yearly
        self.all_delta = all_delta
        # This is the volatility of the stochasitic process... shock
        self.all_sigma = all_sigma
        # this is the annual drift factor for geometric brownian motion aka Growth Rate
        self.gbm_mu = gbm_mu
        # this is the probability of a jump happening at each point for the heston
        self.lamda = jumps_lamda
        # this is the jump size for heston
        self.jumps_sigma = jumps_sigma
        # this is the average jump size
        self.jumps_mu = jumps_mu
        # this is the rate of mean reversion for Cox Ingersoll ross
        self.cir_a = cir_a
        # this is the starting interest rate value
        self.all_r0 = all_r0
        # this is the correlation between the wiener processes of the heston model
        self.cir_rho = cir_rho
        # this is the rate of mean reversion for Ornstein Uhlenbeck
        self.ou_a = ou_a
        # this is the long run average interst rate for Ornstein Uhlenbeck
        self.ou_mu = ou_mu
        # this is the rate of mean reversion for volatility in the heston model
        self.heston_a = heston_a
        #this is the long run average volatility for the Heston Model
        self.heston_mu = heston_mu
        # this is the starting volatility value for the Heston Model
        self.heston_vol0 = heston_vol0

def plot_stochastic_processes(processes, title):
    """
    This method plots a list of stochastic processes with a specified title
    :return: plots the graph of the two
    """
    plt.style.use(['bmh'])
    fig, ax = plt.subplots(1)
    fig.suptitle(title, fontsize=16)
    ax.set_xlabel('Time, t')
    ax.set_ylabel('Simulated Asset Price')
    x_axis = numpy.arange(0, len(processes[0]), 1)
    for i in range(len(processes)):
        plt.plot(x_axis, processes[i])
    plt.show()

def convert_to_returns(log_returns):
    """
    This method exponentiates a sequence of log returns to get daily returns.
    :param log_returns: the log returns to exponentiated
    :return: the exponentiated returns
    """
    print(log_returns)
    return numpy.exp(log_returns)


def convert_to_prices(param, log_returns):
    """
    This method converts a sequence of log returns into normal returns (exponentiation) and then computes a price
    sequence given a starting price, param.all_s0.
    :param param: the model parameters object
    :param log_returns: the log returns to exponentiated
    :return:
    """
    returns = convert_to_returns(log_returns)
    #print(returns)
    # A sequence of prices starting with param.all_s0
    price_sequence = [param.all_s0]
    for i in range(1, len(returns)):
        # Add the price at t-1 * return at t
        price_sequence.append(price_sequence[i - 1] * returns[i - 1])
    return numpy.array(price_sequence)

def brownian_motion_log_returns(param):
    """
    This method returns a Wiener process. The Wiener process is also called Brownian motion. For more information
    about the Wiener process check out the Wikipedia page: http://en.wikipedia.org/wiki/Wiener_process
    :param param: the model parameters object
    :return: brownian motion log returns
    """
    sqrt_delta_sigma = math.sqrt(param.all_delta) * param.all_sigma
    #print(nrand.normal(loc=0, scale=sqrt_delta_sigma, size=param.all_time))
    return nrand.normal(loc=0, scale=sqrt_delta_sigma, size=param.all_time)

def brownian_motion_levels(param):
    """
    Returns a price sequence whose returns evolve according to a brownian motion
    :param param: model parameters object
    :return: returns a price sequence which follows a brownian motion
    """
    return convert_to_prices(param, brownian_motion_log_returns(param))

def geometric_brownian_motion_log_returns(param):
    """
    This method constructs a sequence of log returns which, when exponentiated, produce a random Geometric Brownian
    Motion (GBM). GBM is the stochastic process underlying the Black Scholes options pricing formula.
    :param param: model parameters object
    :return: returns the log returns of a geometric brownian motion process
    """
    assert isinstance(param, ModelParameters)
    wiener_process = numpy.array(brownian_motion_log_returns(param))
    sigma_pow_mu_delta = (param.gbm_mu - 0.5 * math.pow(param.all_sigma, 2.0)) * param.all_delta
    return wiener_process + sigma_pow_mu_delta

def geometric_brownian_motion_levels(param):
    """
    Returns a sequence of price levels for an asset which evolves according to a geometric brownian motion
    :param param: model parameters object
    :return: the price levels for the asset
    """
    return convert_to_prices(param, geometric_brownian_motion_log_returns(param))

def median(array):
    if len(array) < 1:
        return(None)
    if len(array) % 2 == 0:
        median = (array[len(array)//2-1: len(array)//2+1])
        return sum(median) / len(median)
    else:
        return(array[len(array)//2])

def dcf(fc, equity, debt, G, equity_interest, debt_cost):
    tango = (1+equity_interest*(1-debt/(debt+equity)))+ debt_cost*(debt/(debt+equity))
    foxtrot = (equity_interest*(1-debt/(debt+equity)))+ debt_cost*(debt/(debt+equity))
    whiskey = (fc[0]/tango**1 + \
    fc[1]/tango**2 + \
    fc[2]/tango**3 + \
    fc[3]/tango**4 + \
    (fc[3]*(1+G))/ (foxtrot-G)* \
    (1/(tango))**4)
    ve =whiskey - debt
    return ve

def idcf(fc, equity, debt, G, equity_interest, debt_cost):
    counter =0
    calc_value = round(dcf(fc, equity, debt, G, equity_interest, debt_cost),0)
    while True:
        t = round(dcf(fc, calc_value, debt, G, equity_interest, debt_cost),0)
        if (calc_value == t+1 or calc_value == t or calc_value == t-1):
            #print("I cycled ", counter)
            return calc_value
        elif (calc_value != t+1 or calc_value != t or calc_value != t-1):
            print(t, calc_value)
            calc_value = t
        counter += 1

def process(paths, mp):
    geometric_brownian_motion_examples = []
    for i in range(paths):
        geometric_brownian_motion_examples.append(geometric_brownian_motion_levels(mp))
    return geometric_brownian_motion_examples
    #plot_stochastic_processes(geometric_brownian_motion_examples, "Geometric Brownian Motion")

def FC(geometric_brownian_motion_examples, paths):
    FCFF = [[],[],[],[]]

    for i in range(paths):
        FCFF[0].append(geometric_brownian_motion_examples[i][1])
        FCFF[1].append(geometric_brownian_motion_examples[i][2])
        FCFF[2].append(geometric_brownian_motion_examples[i][3])
        FCFF[3].append(geometric_brownian_motion_examples[i][4])
    top = []
    mid = []
    bottom = []
    for i in range(4):
        upper = numpy.percentile(FCFF[i], 95)
        middle = median(FCFF[i])
        lower = numpy.percentile(FCFF[i], 5)
        #print(upper, middle, lower)
        top.append(upper)
        mid.append(middle)
        bottom.append(lower)
    return (top, mid, bottom)

def execute(s,g,start, equity, debt, equity_interest, debt_cost):
    paths = 1000
    mp = ModelParameters(all_s0=start,
                     all_time=5,
                     all_delta=1,
                     all_sigma=s,
                     gbm_mu=g,
                     jumps_lamda=0.00125,
                     jumps_sigma=0.001,
                     jumps_mu=-0.2,
                     cir_a=3.0,
                     cir_mu=0.5,
                     all_r0=0.5,
                     cir_rho=0.5,
                     ou_a=3.0,
                     ou_mu=0.5,
                     heston_a=0.25,
                     heston_mu=0.35,
                     heston_vol0=0.06125)
    gbme = process(paths, mp)
    print(len(gbme))
    top, mid, bottom = FC(gbme, paths)
    print(top, mid, bottom)
    high = idcf(top, equity, debt, g, equity_interest, debt_cost)
    mid = idcf(mid, equity, debt, g, equity_interest, debt_cost)
    low = idcf(bottom, equity, debt, g, equity_interest, debt_cost)
    return high, mid, low
