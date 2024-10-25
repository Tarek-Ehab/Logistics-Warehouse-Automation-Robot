
let addZone = document.getElementById('addzone')
let zoneName = document.getElementById('zoneName')
let msgzone = document.getElementById('msgzone')
//////////////////////////////////////get all zones ////////////////////////////////
let zoneArr = []


const getzone = ()=>{
    axios({
            method:"get",
             url:`${local_server}/api/Zone/`
            }).then((response)=>{
                const {data}= response;
                zoneArr = data;
                showzone()
            }).catch((error)=> {
                console.log(error);
              })
}

getzone()

////////////////////showzoneData///////////////////////////////


const showzone = ()=>{
    let zoneData =``
    for(let i=0;i< zoneArr.length;i++){
        zoneData+= `<tr>
        <td>${zoneArr[i].name}</td>
        <td>  <button type="button" class="btn btn-danger mx-4 " onclick="deletezone(${zoneArr[i].id})">
        <i class="fa fa-trash"></i>
         </button>
         <button type="button" class="btn btn-primary "  onclick="updatezone(${zoneArr[i].id})">
         <i class="fa fa-edit"></i>
          </button></td>
          <td><button type="button" class="btn btn-primary "  onclick="zoneProducts(${zoneArr[i].id})">
          <i class="fa-solid fa-list"></i>
           </button></td>
        </tr>
        `
    }
    document.getElementById("tZone").innerHTML = zoneData;
}


//////////////////////delete zone ////////////////////////////////////

const deletezone = (id)=>{
    axios({
        method:"delete",
        "url":`${local_server}/api/Zone/${id}/delete/`
    }).then((response)=>{
        getzone()
    })
    }

//////////////////update zone ///////////////////////////

const updatezone =(id)=>{
    localStorage.setItem('zoneId',id)
    window.open(`${local_server}/updateZone/`)
    }



    /////////////////////////////////add zone ///////////////////////////

    if(addZone){
        addZone.addEventListener('click',()=>{
            const data = {
                name: zoneName.value,
            }
            axios({
                method: "post",
                url: `${local_server}/api/Zone/`,
                data: data
            }).then((response)=>{
                console.log(response);
                if(response.status === 201){
                    window.open(`${local_server}/zone/`)
                    showzone()
                }
            }).catch((error)=> {
                console.log(error);
                    msgzone.classList.remove('d-none');
                    msgzone.innerHTML = error.response.data.message;   
              })
        })
    }



//////////////////////////////////////go to products by zone page////////////////////////
const zoneProducts =(id)=>{
    localStorage.setItem('proByzone',id)
    window.open(`${local_server}/productsZone/`)
    }

    //////////////////////get product by zone ///////////////////////////////



let zoneProductsArr = [];
const getZoneProducts = ()=>{
    axios({
        method:"get",
        url:`${local_server}/api/zone-producs/${localStorage.getItem('proByzone')}/`
    }).then((response)=>{
        console.log('hi');
        const {data}= response;
        zoneProductsArr = data;
        showProductsZone()
    }).catch((error)=> {
        console.log(error);
      })
}

getZoneProducts()

////show all zone //////////////////////////
const showProductsZone = ()=>{
    let cartonaZone=``
    for(let i=0;i< zoneProductsArr.length;i++){
        cartonaZone+= `<tr>
        <td>${zoneProductsArr[i].zone.name}</td>
        <td>${zoneProductsArr[i].name}</td>
        <td>${zoneProductsArr[i].supplier.name}</td>
        <td>${zoneProductsArr[i].classification.title}</td>
        <td>${zoneProductsArr[i].shelf.name}</td>
        <td>${zoneProductsArr[i].price}</td>
        <td>${zoneProductsArr[i].quantity}</td>
        </tr>
        `
    }
    document.getElementById("zoneProducts").innerHTML = cartonaZone;
}