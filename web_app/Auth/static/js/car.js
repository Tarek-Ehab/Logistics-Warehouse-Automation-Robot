let dropname = document.getElementById('dropname')
let addCar = document.getElementById('addCar')
let msgCar = document.getElementById('msgCar')





let carsArr = [];
const getCarDrop = ()=>{
    axios({
        method:"get",
        url:`${local_server}/api/CarDrop/`
    }).then((response)=>{
        const {data}= response;
        carsArr = data;
        showCarDrop()
    }).catch((error)=> {
        console.log(error);
      })
}

getCarDrop()



////show all carDrop //////////////////////////
const showCarDrop = ()=>{
    let cartona =``
    for(let i=0;i< carsArr.length;i++){
        cartona+= `<tr>
        <td>${carsArr[i].drop_name}</td>
        <td>${carsArr[i].delivery_status}</td>
        <td>  <button type="button" class="btn btn-danger mx-4 " onclick="deleteCar(${carsArr[i].id})">
        <i class="fa fa-trash"></i>
         </button>
         <button type="button" class="btn btn-primary "  onclick="updateCar(${carsArr[i].id})">
         <i class="fa fa-edit"></i>
          </button></td>
        </tr>
        `
    }
    document.getElementById("tcar").innerHTML = cartona;
}



//////add car/////
if(addCar){
    addCar.addEventListener('click',()=>{
        const data = {
            drop_name: dropname.value
        }
        axios({
            method: "post",
            url: `${local_server}/api/CarDrop/`,
            data: data
        }).then((response)=>{
            if(response.status === 201){
                window.open(`${local_server}/carDrop/`)
                showCarDrop()
            }
        }).catch((error)=> {
            msgCar.classList.remove('d-none');
            msgCar.innerHTML = error.response.data.drop_name
          })
    })
}




///////////////delete car ////////////////


const deleteCar = (id)=>{
    axios({
        method:"delete",
        "url":`${local_server}/api/CarDrop/${id}/delete/`
    }).then((response)=>{
        getCarDrop()
    })
    }


//////////update car ////////////////////////

const updateCar =(id)=>{
    localStorage.setItem('carId',id)
    window.open(`${local_server}/updatecardrop/`)
    }