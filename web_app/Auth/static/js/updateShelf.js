
let updateShelf = document.getElementById('updateShelf')
let shelfName = document.getElementById('shelfName')
let capcity = document.getElementById('capcity')
let expiry_date = document.getElementById('expiry_date')
let msgshelf = document.getElementById('msgshelf')
let msgcapacity = document.getElementById('msgcapacity')
let msgshelfdata = document.getElementById('msgshelfdata')

 ////////////////////////get shelf by id/////////////////////////

 const getShelfId = ()=>{

    axios({
        method:"get",
        url:`${local_server}/api/Shelf/${localStorage.getItem('shelfId')}/`
    }).then((response)=>{
        if(response.status ===200){
            shelfName.value = response.data.name,
            capcity.value =response.data.capacity,
            expiry_date.value= response.data.expiry_date
        }
    }).catch((error)=> {
        console.log(error);
      })
}
getShelfId()


///////////////////////////update shelf//////////////////////////////

if(updateShelf){
    updateShelf.addEventListener('click',()=>{
        const data = {
            name: shelfName.value,
            capacity:capcity.value,
            expiry_date:expiry_date.value
        }
        axios({
            method: "put",
            url: `${local_server}/api/Shelf/${localStorage.getItem('shelfId')}/update/`,
            data: data,
        }).then((response)=>{
           if(response.status ===200){
             window.open(`${local_server}/shelf/`)
           }
        }).catch((error)=> {
            if(error.response.data.name){
                msgcapacity.classList.add('d-none');
                msgshelfdata.classList.add('d-none');
                msgshelf.classList.remove('d-none');
                msgshelf.innerHTML = error.response.data.name
            }else if(error.response.data.capacity){
                msgshelfdata.classList.add('d-none');
                msgshelf.classList.add('d-none');
                msgcapacity.classList.remove('d-none');
            }else{
                msgshelf.classList.add('d-none');
                msgcapacity.classList.add('d-none');
                msgshelfdata.classList.remove('d-none');
            }
          })
    })
 }  