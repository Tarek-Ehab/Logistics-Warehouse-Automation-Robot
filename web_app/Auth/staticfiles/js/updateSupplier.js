let supName = document.getElementById('name')
let address = document.getElementById('address')
let phone = document.getElementById('phone')
let email = document.getElementById('email')
let updatesupp =   document.getElementById('updatesupp')
let msgsup = document.getElementById('msgsup')
let msgaddress = document.getElementById('msgaddress')
let msgphone = document.getElementById('msgphone')
let msgemail = document.getElementById('msgemail')



/////////////////////get supplierById/////////////////////////

const getSuppId = ()=>{

    axios({
        method:"get",
        url:`${local_server}/api/Supplier/${localStorage.getItem('supplierId')}/`
    }).then((response)=>{
        if(response.status ===200){
            supName.value = response.data.name,
            address.value =response.data.address,
            phone.value= response.data.phone
            email.value= response.data.email
        }
    }).catch((error)=> {
        console.log(error);
      })
}
getSuppId()

///////////////////////////update supp/////////////////////////
if(updatesupp){
    updatesupp.addEventListener('click',()=>{
        const data = {
            name: supName.value,
            address:address.value,
            phone:phone.value,
            email:email.value
        }
        axios({
            method: "put",
            url: `${local_server}/api/Supplier/${localStorage.getItem('supplierId')}/update/`,
            data: data,
        }).then((response)=>{
           if(response.status ===200){
            window.open(`${local_server}/supplier/`)
           }
        }).catch((error)=> {
            if(error.response.data.name){
                msgsup.classList.remove('d-none');
                msgaddress.classList.add('d-none');
                msgphone.classList.add('d-none');
                msgemail.classList.add('d-none');
                msgsup.innerHTML = error.response.data.name
           }else if(error.response.data.address){
                 msgaddress.classList.remove('d-none');
                 msgsup.classList.add('d-none');
                msgphone.classList.add('d-none');
                msgemail.classList.add('d-none');
                msgaddress.innerHTML = error.response.data.address
            }else if(error.response.data.phone){
                msgphone.classList.remove('d-none');
                msgsup.classList.add('d-none');
                msgaddress.classList.add('d-none');
               msgemail.classList.add('d-none');
               msgphone.innerHTML = error.response.data.phone
           }else{
                msgemail.classList.remove('d-none');
                msgsup.classList.add('d-none');
                msgaddress.classList.add('d-none');
                msgphone.classList.add('d-none');
               msgemail.innerHTML = error.response.data.email
           }
          })
    })
 }  