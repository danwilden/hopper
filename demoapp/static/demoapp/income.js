// TODO: Add business id selection as part of the valuation processes
// TODO: Create valuation process

var standardDeviation= function (values){
  var avg = average(values);

  var squareDiffs = values.map(function(value){
    var diff = value - avg;
    var sqrDiff = diff * diff;
    return sqrDiff;
  });

  var avgSquareDiff = average(squareDiffs);

  var stdDev = Math.sqrt(avgSquareDiff);
  return stdDev;
}
var average = function(data){
  var sum = data.reduce(function(sum, value){
    return sum + value;
  }, 0);

  var avg = sum / data.length;
  return avg;
}

var app2 = new Vue({
  delimiters: ['${', '}$'],
  el: '#app2',
  data: () => ({
    e1: 0,
    dialog: false,
    dialog2: false,
    valuations: [],
    calculations : {debt: 0, equity:0, growth:0, sigma:0},
    incheaders: [
      { text: 'Actions', value: 'name', sortable: false },
      {
        text: 'Financial Year',
        align: 'left',
        sortable: false,
        value: 'name'
      },
      { text: 'Sales', value: 'sales' },
      { text: 'Expenses', value: 'costs' },
      { text: 'Taxes', value: 'taxes' },
      { text: 'Amoritization', value: 'amort' },
      { text: 'Deprectiation', value: 'depr' },
      { text: 'Owner Salary', value: 'owner' },
      { text: 'Bank Expenses', value: 'bank' },
      { text: 'Wages', value: 'wage' },
      { text: 'Salaries and Benefits', value: 's_b' },
      { text: 'Rent', value: 'rent' },
      { text: 'Utilities', value: 'util' },
      { text: 'Insurance', value: 'ins' },
    ],
    incomes: [],
    balheaders: [
      { text: 'Actions', value: 'name', sortable: false },
      {
        text: 'Financial Year',
        align: 'left',
        sortable: false,
        value: 'name'
      },
      { text: 'Cash', value: 'cash' },
      { text: 'AR', value: 'ar' },
      { text: 'Inventory', value: 'inv' },
      { text: 'FF&E Capital and Assets', value: 'ffe' },
      { text: 'AP', value: 'ap' },
      { text: 'Bank Debt', value: 'bank' },
      { text: 'Shareholder Dues', value: 'shdue' },
      { text: 'Short Term Debt', value: 'curp' },
      { text: 'Longterm Debt', value: 'debt' },
      { text: 'Shareholder Equity', value: 'shar' },
    ],
    balances: [],
    editedIndex: -1,
    BaleditedIndex: -1,
    editedItem: {
      name: '',
      sales: 0.0,
      costs: 0.0,
      taxes: 0.0,
      amort: 0.0,
      depr: 0.0,
      owner: 0.0,
      bank: 0.0,
      wage: 0.0,
      s_b: 0.0,
      rent: 0.0,
      util: 0.0,
      ins: 0.0,
    },
    defaultItem: {
      name: '',
      sales: 0.0,
      costs: 0.0,
      taxes: 0.0,
      amort: 0.0,
      depr: 0.0,
      owner: 0.0,
      bank: 0.0,
      wage: 0.0,
      s_b: 0.0,
      rent: 0.0,
      util: 0.0,
      ins: 0.0,
    },
    BaleditedItem: {
      name: '',
      cash: 0.0,
      ar: 0.0,
      inv: 0.0,
      ffe: 0.0,
      ap: 0.0,
      bank: 0.0,
      shdue: 0.0,
      curp: 0.0,
      debt: 0.0,
      shar: 0.0,
    },
    BaldefaultItem: {
      name: '',
      cash: 0.0,
      ar: 0.0,
      inv: 0.0,
      ffe: 0.0,
      ap: 0.0,
      bank: 0.0,
      shdue: 0.0,
      curp: 0.0,
      debt: 0.0,
      shar: 0.0,
    }
  }),

  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
    },
    BalformTitle () {
      return this.BaleditedIndex === -1 ? 'New Item' : 'Edit Item'
    }
  },

  watch: {
    dialog (val) {
      val || this.close()
    }
  },

  created () {
    this.initialize()
  },

  methods: {
    initialize () {
      this.incomes = [
        {
          name: 'Year-5',
          sales: 0.0,
          costs: 0.0,
          taxes: 0.0,
          amort: 0.0,
          depr: 0.0,
          owner: 0.0,
          bank: 0.0,
          wage: 0.0,
          s_b: 0.0,
          rent: 0.0,
          util: 0.0,
          ins: 0.0,
        },
        {
          name: 'Year-4',
          sales: 0.0,
          costs: 0.0,
          taxes: 0.0,
          amort: 0.0,
          depr: 0.0,
          owner: 0.0,
          bank: 0.0,
          wage: 0.0,
          s_b: 0.0,
          rent: 0.0,
          util: 0.0,
          ins: 0.0,
        },
        {
          name: 'Year-3',
          sales: 0.0,
          costs: 0.0,
          taxes: 0.0,
          amort: 0.0,
          depr: 0.0,
          owner: 0.0,
          bank: 0.0,
          wage: 0.0,
          s_b: 0.0,
          rent: 0.0,
          util: 0.0,
          ins: 0.0,
        },
        {
          name: 'Year-2',
          sales: 0.0,
          costs: 0.0,
          taxes: 0.0,
          amort: 0.0,
          depr: 0.0,
          owner: 0.0,
          bank: 0.0,
          wage: 0.0,
          s_b: 0.0,
          rent: 0.0,
          util: 0.0,
          ins: 0.0,
        },
        {
          name: 'Year-1',
          sales: 0.0,
          costs: 0.0,
          taxes: 0.0,
          amort: 0.0,
          depr: 0.0,
          owner: 0.0,
          bank: 0.0,
          wage: 0.0,
          s_b: 0.0,
          rent: 0.0,
          util: 0.0,
          ins: 0.0,
        },
        {
          name: 'Current',
          sales: 0.0,
          costs: 0.0,
          taxes: 0.0,
          amort: 0.0,
          depr: 0.0,
          owner: 0.0,
          bank: 0.0,
          wage: 0.0,
          s_b: 0.0,
          rent: 0.0,
          util: 0.0,
          ins: 0.0,
        }
      ]
      this.balances = [
        {name: '',
        cash: 0.0,
        ar: 0.0,
        inv: 0.0,
        ffe: 0.0,
        ap: 0.0,
        bank: 0.0,
        shdue: 0.0,
        curp: 0.0,
        debt: 0.0,
        shar: 0.0,
      }
      ]
    },

    editItem (item) {
      this.editedIndex = this.incomes.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem (item) {
      const index = this.incomes.indexOf(item)
      confirm('Are you sure you want to delete this item?') && this.incomes.splice(index, 1)
    },

    close () {
      this.dialog = false
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      }, 300)
    },

    save () {
      if (this.editedIndex > -1) {
        Object.assign(this.incomes[this.editedIndex], this.editedItem)
      } else {
        this.incomes.push(this.editedItem)
      }
      this.close()
    },
    baleditItem (item) {
      this.BaleditedIndex = this.balances.indexOf(item)
      this.BaleditedItem = Object.assign({}, item)
      this.dialog2 = true
    },

    baldeleteItem (item) {
      const index = this.balances.indexOf(item)
      confirm('Are you sure you want to delete this item?') && this.balances.splice(index, 1)
    },

    balclose () {
      this.dialog2 = false
      setTimeout(() => {
        this.BaleditedItem = Object.assign({}, this.BaldefaultItem)
        this.BaleditedIndex = -1
      }, 300)
    },

    balsave () {
      if (this.BaleditedIndex > -1) {
        Object.assign(this.balances[this.BaleditedIndex], this.BaleditedItem)
      } else {
        this.balances.push(this.BaleditedItem)
      }
      this.balclose()
    },
    calculateDebt(){
      this.balances = [
        {name: '',
        cash: 500.0,
        ar: 400.0,
        inv: 300.0,
        ffe: 200.0,
        ap: 100.0,
        bank: 200.0,
        shdue: 10.0,
        curp: 200.0,
        debt: 400.0,
        shar: 0.0,
      }
      ]
      var liab=parseFloat(this.balances[0].ap)+parseFloat(this.balances[0].bank)+parseFloat(this.balances[0].shdue)+parseFloat(this.balances[0].curp)+parseFloat(this.balances[0].debt)+parseFloat(this.balances[0].shar);
      this.calculations.debt = liab;
    },
    calculateEquity(){
      var ncwc= ((parseFloat(this.balances[0].ar)+parseFloat(this.balances[0].inv)+parseFloat(this.balances[0].ffe))+parseFloat(this.balances[0].cash))-parseFloat(this.calculations.debt);
      this.calculations.equity = ncwc;
    },
    calculateGrowthRate(){
      sales = 100
      //delete below its a crap function for testing
      for (i=0; i<=this.incomes.length-1; i++){
        this.incomes[i].sales = sales + i * 10
      }
      delta =0
      //need to add some logic to check for enough years
      for (i=1; i< this.incomes.length-1; i++){
        delta += (parseFloat(this.incomes[i].sales) - parseFloat(this.incomes[i-1].sales))/parseFloat(this.incomes[i-1].sales);
      }
      var g = (delta/this.incomes.length);
      this.calculations.growth = g;
      s_arr = []
      for (i=0; i<=this.incomes.length-1; i++){
        s_arr.push(this.incomes[i].sales);
      }
      this.calculations.sigma = standardDeviation(s_arr)/365;

    },
        getValuation(){
          var data2 = {business: 1,
                      start: this.incomes[this.incomes.length-1].sales,
                      sigma: this.calculations.sigma,
                      mu: this.calculations.growth,
                      equity: this.calculations.equity,
                      debt: this.calculations.debt,
                      eroi: parseFloat(this.calculations.eroi),
                      cod: parseFloat(this.calculations.cod)}
          console.log(data2);
          fetch("../valuation/", {
              method: "post",
              credentials: "same-origin",
              headers: {
                  "X-CSRFToken": Cookies.get('csrftoken'),
                  "Accept": "application/json",
                  "Content-Type": "application/json"
              },
              body: JSON.stringify(data2)
          }).then(function(response) {
              console.log(response.json());
          }).then(function(data) {
              console.log("Data is ok", data);
          }).catch(function(ex) {
              console.log("parsing failed", ex);
          });
        }
    }

})
