let buyerName = document.getElementById('name')
let buyerMsg = document.getElementById('buyerMsg')
let addressBuyer = document.getElementById('address')
let addressMsg = document.getElementById('addressMsg')
let phoneBuyer = document.getElementById('phone')
let phoneMsg = document.getElementById('phoneMsg')
let emailBuyer = document.getElementById('email')
let emailMsg = document.getElementById('emailMsg')
let buyerUpdate = document.getElementById('buyerUpdate')


//////////////////////////////////////get buyer by id///////////////////////////////////

const getBuyerId = ()=>{

    axios({
        method:"get",
        url:`${local_server}/api/Buyer/${localStorage.getItem('buyerId')}/`
    }).then((response)=>{
        if(response.status ===200){
            buyerName.value = response.data.name,
            addressBuyer.value =response.data.address,
            phoneBuyer.value= response.data.phone
            emailBuyer.value= response.data.email
        }
    }).catch((error)=> {
        console.log(error);
      })
}
getBuyerId()




/////////////////////////////updateBuyer////////////////////////////////////////

if(buyerUpdate){
    buyerUpdate.addEventListener('click',()=>{
        const data = {
            name: buyerName.value,
            address:addressBuyer.value,
            phone:phoneBuyer.value,
            email:emailBuyer.value
        }
        axios({
            method: "put",
            url: `${local_server}/api/Buyer/${localStorage.getItem('buyerId')}/update/`,
            data: data,
        }).then((response)=>{
           if(response.status ===200){
             window.open(`${local_server}/buyer/`)
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
