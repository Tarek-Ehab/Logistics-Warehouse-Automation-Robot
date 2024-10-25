let proList = document.getElementById('proList')
let BuyList = document.getElementById('BuyList')
let SupList = document.getElementById('SupList')
let qty = document.getElementById('qty')
let DropList = document.getElementById('DropList')
let Status = document.getElementById('status')
let qtyMsg = document.getElementById('qtyMsg')
let updateOrder = document.getElementById('updateOrder')
let updateDelivery = document.getElementById('updateDelivery')
let address = document.getElementById("address");
let addDelivery = document.getElementById("addDelivery");
let deliveryDate = document.getElementById("date");
let oDate = document.getElementById("oDate");






/////////////////////////////////get product list /////////////////////////////////////////////////

let productarray = [];
const getproductsLists = async () => {
  axios({
    method: "get",
    url: `${local_server}/api/Product/`,
  }).then((response) => {
        const {data} = response;
        productarray = data;
        showproductarr()
    }).catch((error) => {
      console.log(error);
    });
};

getproductsLists()

// add product to list

const showproductarr = function () {
  let procartona =``
    for(var i = 0; i <productarray.length;i++ ){
      procartona += `<option value='${productarray[i].name}'>${productarray[i].name}</option>`
    }
    document.getElementById("proList").innerHTML = procartona;

};




/////////////////////////////////get Buyer list /////////////////////////////////////////////////

let BuyerArray = [];
const getBuyerList = async () => {
    axios({
        method:"get",
        url:`${local_server}/api/Buyer/`
    }).then((response)=>{
        const {data}= response;
        BuyerArray = data;
        showdataBuyer()
    }).catch((error)=> {
        console.log(error);
      })
};
getBuyerList()
// add buyer to list
const showdataBuyer = function () {
    BuyerArray.forEach((buy) => {
    document.getElementById("BuyList").innerHTML += `
            <option value='${buy.name}'>${buy.name}</option>
        `;
  });
};


/////////////////////////////////get supplier list /////////////////////////////////////////////////

let supplyArray = [];
const getSupplyList = async () => {
    axios({
        method:"get",
        url:`${local_server}/api/Supplier/`
      }).then((response)=>{
        const {data}= response;
        supplyArray = data;
        showdataSupply()
    }).catch((error)=> {
        console.log(error);
      })
};
getSupplyList()
// add supplier to list
const showdataSupply = function () {
    supplyArray.forEach((item) => {
    document.getElementById("SupList").innerHTML += `
            <option value='${item.name}'>${item.name}</option>
        `;
  });
};



/////////////////////////////////get drop list /////////////////////////////////////////////////

let DropArray = [];
const getDropList = async () => {
    axios({
        method:"get",
        url:`${local_server}/api/CarDrop/`
    }).then((response)=>{
        const {data}= response;
        DropArray = data;
        showdataDrop()
    }).catch((error)=> {
        console.log(error);
      })
};
getDropList()
// add supplier to list
const showdataDrop = function () {
    DropArray.forEach((item) => {
    document.getElementById("DropList").innerHTML += `
            <option value='${item.drop_name}'>${item.drop_name}</option>
        `;
  });
};



///////////////////////////////////////////////get order by id ////////////////////////////////////////
const getorderId = ()=>{

    axios({
        method:"get",
        url:`${local_server}/api/Order/${localStorage.getItem('orderId')}/`
    }).then((response)=>{
        if(response.status ===200){
              proList.value = response.data.product.name,
              qty.value=response.data.quantity,
              BuyList.value=response.data.buyer.name,
              DropList.value= response.data.drop_name.drop_name,
              oDate.value = response.data.order_date,
              Status.value = response.data.delivery_status
         }
    }).catch((error)=> {
        console.log(error);
      })
  }
  getorderId()
  
  
  
  
  
  //////////////////////////////////////update order /////////////////////////////////////////////////
  if(updateOrder){
    updateOrder.addEventListener('click',()=>{
      const data = {
        product_name:proList.value,
        quantity:qty.value,
        buyer_name:BuyList.value,
        delivery_status:Status.value,
        drop_name:DropList.value,
        order_date:oDate.value,
    }
        axios({
            method: "put",
            url:`${local_server}/api/Order/${localStorage.getItem('orderId')}/update/`,
            data: data,
        }).then((response)=>{
          console.log(response);
           if(response.status ===200){
            window.open(`${local_server}/order/`)
          }
        }).catch((error)=> {
          console.log(error);
          if(error.message === 'Request failed with status code 500'){
            qtyMsg.classList.remove('d-none');
          }
          })
    })
  }
  






  