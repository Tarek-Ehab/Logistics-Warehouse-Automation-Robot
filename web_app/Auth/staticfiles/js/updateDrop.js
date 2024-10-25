let dropname = document.getElementById('dropname')
let updateCar = document.getElementById('UpdateCar')
let msgCar = document.getElementById('msgCar')
 ///////////////////////get carDrop by Id//////////////////////////////


 const getCarId = ()=>{

    axios({
        method:"get",
        url:`${local_server}/api/CarDrop/${localStorage.getItem('carId')}/`
    }).then((response)=>{
        if(response.status ===200){
            dropname.value = response.data.drop_name
          
        }
    }).catch((error)=> {
        console.log(error);
      })
}
getCarId()


/////////////////////////////updateCar////////////////////////////////////////

if(updateCar){
    updateCar.addEventListener('click',()=>{
        const data = {
            drop_name: dropname.value,
        }
        axios({
            method: "put",
            url: `${local_server}/api/CarDrop/${localStorage.getItem('carId')}/update/`,
            data: data,
        }).then((response)=>{
           if(response.status ===200){
            window.open(`${local_server}/carDrop/`)
           }
        }).catch((error)=> {
            msgCar.classList.remove('d-none');
            msgCar.innerHTML = error.response.data.drop_name
           
          })
    })
 } 
