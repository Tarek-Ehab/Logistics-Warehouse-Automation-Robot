let buyerName = document.getElementById('name')
let buyerMsg = document.getElementById('buyerMsg')
let address = document.getElementById('address')
let addressMsg = document.getElementById('addressMsg')
let phone = document.getElementById('phone')
let phoneMsg = document.getElementById('phoneMsg')
let email = document.getElementById('email')
let emailMsg = document.getElementById('emailMsg')
let buyerAdd = document.getElementById('buyerAdd')





/////////////////////////////get all buyer //////////////////////////

let BuyersArr = [];
const getBuyer = ()=>{
    axios({
        method:"get",
        url:`${local_server}/api/Buyer/`
    }).then((response)=>{
        const {data}= response;
        BuyersArr = data;
        showBuyer()
    }).catch((error)=> {
        console.log(error);
      })
}

getBuyer()



////show all buyer /////////////////////////
const showBuyer = ()=>{
    let cartona =``
    for(let i=0;i< BuyersArr.length;i++){
        cartona+= `<tr>
        <td>${BuyersArr[i].name}</td>
        <td>${BuyersArr[i].address}</td>
        <td>${BuyersArr[i].phone}</td>
        <td>${BuyersArr[i].email}</td>
        <td>${BuyersArr[i].order_count}</td>
        <td>${BuyersArr[i].created_date}</td>
        <td>  <button type="button" class="btn btn-danger mx-4 " onclick="deleteBuyer(${BuyersArr[i].id})">
        <i class="fa fa-trash"></i>
         </button>
         <button type="button" class="btn btn-primary "  onclick="updateBuyer(${BuyersArr[i].id})">
         <i class="fa fa-edit"></i>
          </button></td>
          <td><button type="button" class="btn btn-primary "  onclick="buyerProducts(${BuyersArr[i].id})">
          <i class="fa-solid fa-list"></i>
           </button></td>
        </tr>
        `
    }
    document.getElementById("tBuyer").innerHTML = cartona;
}


//////add buyer/////
if(buyerAdd){
    buyerAdd.addEventListener('click',()=>{
        const data = {
            name: buyerName.value,
            address:address.value,
            phone:phone.value,
            email:email.value
        }
        axios({
            method: "post",
            url: `${local_server}/api/Buyer/`,
            data: data
        }).then((response)=>{
            if(response.status === 201){
                window.open(`${local_server}/buyer/`)
                showBuyer()
            }
        }).catch((error)=> {
            if(error.response.data.name){
                addressMsg.classList.add('d-none');
                phoneMsg.classList.add('d-none');
                emailMsg.classList.add('d-none');
                buyerMsg.classList.remove('d-none');
                buyerMsg.innerHTML = error.response.data.name
            }else if(error.response.data.address){
                phoneMsg.classList.add('d-none');
                emailMsg.classList.add('d-none');
                buyerMsg.classList.add('d-none');
                addressMsg.classList.remove('d-none');
                addressMsg.innerHTML = error.response.data.address
            }else if(error.response.data.phone){
                addressMsg.classList.add('d-none');
                emailMsg.classList.add('d-none');
                buyerMsg.classList.add('d-none');
                phoneMsg.classList.remove('d-none');
                phoneMsg.innerHTML = error.response.data.phone
            }
            else{
                addressMsg.classList.add('d-none');
                phoneMsg.classList.add('d-none');
                buyerMsg.classList.add('d-none');
                emailMsg.classList.remove('d-none');
                emailMsg.innerHTML = error.response.data.email
            }
          })
    })
}



///////////////delete buyer ////////////////


const deleteBuyer = (id)=>{
    axios({
        method:"delete",
        "url":`${local_server}/api/Buyer/${id}/delete/`
    }).then((response)=>{
        getBuyer()
    })
    }



//////////update buye ////////////////////////

const updateBuyer =(id)=>{
    localStorage.setItem('buyerId',id)
    window.open(`${local_server}/updatebuyer/`)
    }




//////////////////////////////////////go to products by buyer page////////////////////////
const buyerProducts =(id)=>{
    localStorage.setItem('proByBuyer',id)
    window.open(`${local_server}/productsBuyer/`)
    }

    //////////////////////get product by classification ///////////////////////////////



let buyerProductsArr = [];
const getBuyerProducts = ()=>{
    axios({
        method:"get",
        url:`${local_server}/api/buyer-orders/${localStorage.getItem('proByBuyer')}/`
    }).then((response)=>{
        const {data}= response;
        buyerProductsArr = data;
        showProductsbuyer()
    }).catch((error)=> {
        console.log(error);
      })
}

getBuyerProducts()

////show all classification //////////////////////////
const showProductsbuyer = ()=>{
    let cartonaBuyer =``
    for(let i=0;i< buyerProductsArr.length;i++){
        cartonaBuyer+= `<tr>
        <td>${buyerProductsArr[i].buyer.name}</td>
        <td>${buyerProductsArr[i].product.name}</td>
        <td>${buyerProductsArr[i].drop_name.drop_name}</td>
        <td>${buyerProductsArr[i].order_date}</td>
        <td>${buyerProductsArr[i].quantity}</td>
        <td>${buyerProductsArr[i].delivery_status}</td>
        </tr>
        `
    }
    document.getElementById("buyerProducts").innerHTML = cartonaBuyer;
}