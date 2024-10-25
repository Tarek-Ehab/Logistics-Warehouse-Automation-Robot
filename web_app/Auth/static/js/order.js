let addOrder = document.getElementById('addOrder')
let proList = document.getElementById('proList')
let BuyList = document.getElementById('BuyList')
let qty = document.getElementById('qty')
let DropList = document.getElementById('DropList')
let Status = document.getElementById('status')
let qtyMsg = document.getElementById('qtyMsg')
let updateOrder = document.getElementById('updateOrder')
let daty = document.getElementById('daty')


////////////////////////////get orders list//////////////////////////////////////////////////

let OrdersArr = [];
const getOrders = async () => {
  axios({
    method: "get",
    url:`${local_server}/api/Order/`,
  })
    .then((response) => {
        const { data } = response;
        OrdersArr = data;
        showOrderData();
    })
    .catch((error) => {
      console.log(error);
    });
};

getOrders();
/////////////////////////////////////////show data/////////////////////////////////////////////////
const showOrderData = () => {
  let cartona ="";
  for (let i = 0; i < OrdersArr.length; i++) {  
      cartona += `<tr>
        <td>${OrdersArr[i].product.name}</td>
        <td>${OrdersArr[i].buyer.name}</td>
        <td>${OrdersArr[i].quantity}</td>
        <td>${OrdersArr[i].drop_name.drop_name}</td>
        <td>${OrdersArr[i].order_date}</td>
        <td>${OrdersArr[i].delivery_status}</td>
        <td>  <button type="button" class="btn btn-danger" onclick="deleteOrder(${OrdersArr[i].id})">
        <i class="fa fa-trash"></i>
        </button>
        <button type="button" class="btn btn-primary "  onclick="updateOrders(${OrdersArr[i].id})">
        <i class="fa fa-edit"></i>
          </button></td>
          <td/>
          <button type="button" class="btn btn-primary "  onclick="send_product('${OrdersArr[i].product.name}')">
          <i class="fa-solid fa-list"></i>
          </button></td>
    
        </tr>
        `;
  }
  document.getElementById("orderBdy").innerHTML = cartona;
};




///////////////////////////////////delete order//////////////////////////////////////////////////
const deleteOrder = (id) => {
    axios({
      method: "delete",
      url: `${local_server}/api/Order/delete/${id}/`,
    }).then((response) => {
        getOrders();
    });
  };
  
  //////////////////////////////////////update order///////////////////////////////////////////////////////
  const updateOrders = (id) => {
    localStorage.setItem('orderId',id)
    window.open(`${local_server}/updateorder/`)
  };
  

 




/////////////////////////////////get product list /////////////////////////////////////////////////

let productsArray = [];
const getproducts =() => {
  axios({
    method: "get",
    url: `${local_server}/api/Product/`,
  }).then((response) => {
        const { data } = response;
        productsArray = data;
        showdataPro();
    })
    .catch((error) => {
      console.log(error);
    });
};
 getproducts()
// add product to list
const showdataPro = function () {
  let cartonepro =``
    for(var i = 0; i <productsArray.length;i++ ){
      cartonepro += `<option value='${productsArray[i].name}'>${productsArray[i].name}</option>`
    }
    document.getElementById("proList").innerHTML = cartonepro;

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





//////////////////////////add order//////////////////////////////

if(addOrder){
    addOrder.addEventListener('click',()=>{
        const data = {
            product: proList.value,
            quantity:qty.value,
            buyer:BuyList.value,
            delivery_status:Status.value,
            drop_name:DropList.value,
            order_date:daty.value
        }
        console.log(proList.value);
        axios({
            method: "post",
            url: `${local_server}/api/Order/`,
            data: data
        }).then((response)=>{
            if(response.status === 201){
              window.open(`${local_server}/order/`)
                showOrderData()
            }
        }).catch((error)=> {
            if(error.message === 'Request failed with status code 500'){
              qtyMsg.classList.remove('d-none');
            }else if(error.data.message){
              qtyMsg.classList.remove('d-none');
              qtyMsg.innerHTML = error.data.message;
            }
            console.log(error);
          })
    })
  }
  









