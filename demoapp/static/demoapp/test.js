// TODO: Create login processes


var app = new Vue({
        delimiters: ['${', '}$'],
        el: '#app',
        data: {
            businesses: [],
            users: [],
            message: "What up motherfucker.",
            business: {
              name: '',
              description: '',
              address: '',
              val_comp: 'false',
              valuation: '0',
              owner: '',
              broker: '',
            },
              headers: [
              {
                text: 'TEST',
                align: 'left',
                sortable: false,
                value: 'name'
              },{text:'Sales', value: 'sales'},
              {text:'Cost', value:'Cost'}
            ],
              incomes:[
                {year: 2018, sales:10, cost:0},
              ]
            },

        //http: {
            //root: 'http://127.0.0.1:8000/',
            //headers: {
              //Authorization: 'Basic YXBpOnBhc3N3b3Jk'
            //}
        //},
        methods: {
          getUsers: function () {
              this.$http.get('../user/')
              .then((response)=>{
                console.log(response.body.name);
                this.users = response.body;
                console.log(this.users);
              })
          },
            getBusinesses: function () {
                this.$http.get('../business/')
                .then((response)=>{
                  console.log(response.body.name);
                  this.businesses = response.body;
                  console.log(this.businesses);
                })
            },
            checkFunction :  function(){
              var x = this.business;
              console.log(JSON.stringify(x));
            },
            postBusiness: function () {
              var data2 = this.business
              console.log(data2);
              fetch("business/", {
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
                  app.getBusinesses();
              }).catch(function(ex) {
                  console.log("parsing failed", ex);
              });
            }
        },
        mounted: function () {
          console.log("Trying");
            this.getBusinesses();
            this.getUsers();
        }
    })
