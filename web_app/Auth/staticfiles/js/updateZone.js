let updatezone = document.getElementById('zoneup')
let msgzony = document.getElementById('msgzony')
let zoneupdate = document.getElementById('zoneupdate')
 ////////////////////////get zone by id ///////////////////////////////////////

 const getZoneId = ()=>{

    axios({
        method:"get",
        url:`${local_server}/api/Zone/${localStorage.getItem('zoneId')}/`
    }).then((response)=>{
        if(response.status ===200){
            zoneupdate.value = response.data.name
          
        }
    }).catch((error)=> {
        console.log(error);
      })
}
getZoneId()


//////////////////////////////update zone///////////////////////////////
if(updatezone){
    updatezone.addEventListener('click',()=>{
        const data = {
            name: zoneupdate.value,
        }
        axios({
            method: "put",
            url: `${local_server}/api/Zone/${localStorage.getItem('zoneId')}/update/`,
            data: data,
        }).then((response)=>{
           if(response.status ===200){
            window.open(`${local_server}/zone/`)
           }
        }).catch((error)=> {
            console.log(error);
            msgzony.classList.remove('d-none');
            msgzony.innerHTML = error.response.data.detail
          })
    })
 } 
