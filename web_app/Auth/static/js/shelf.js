let shelfName = document.getElementById('shelfName')
let capcity = document.getElementById('capcity')
let expiry_date = document.getElementById('expiry_date')
let addshelf = document.getElementById('addshelf')
let msgshelf = document.getElementById('msgshelf')
let msgcapacity = document.getElementById('msgcapacity')
let msgshelfdata = document.getElementById('msgshelfdata')

//////////////////get shelf///////////////////////////
let shelfAr = []


const getShelf = ()=>{
    axios({
                method:"get",
             url:`${local_server}/api/Shelf/`
            }).then((response)=>{
                const {data}= response;
                shelfAr = data;
                showShelf()
            }).catch((error)=> {
                console.log(error);
              })
}

getShelf()

////////////////////showshelfData///////////////////////////////


const  showShelf = ()=>{
    let shelfData =``
    for(let i=0;i< shelfAr.length;i++){
        shelfData+= `<tr>
        <td>${shelfAr[i].name}</td>
        <td>${shelfAr[i].capacity}</td>
        <td>${shelfAr[i].created_date}</td>
        <td>${shelfAr[i].expiry_date}</td>
        <td>  <button type="button" class="btn btn-danger mx-4 " onclick="deleteShelf(${shelfAr[i].id})">
        <i class="fa fa-trash"></i>
         </button>
         <button type="button" class="btn btn-primary "  onclick="updateShelf(${shelfAr[i].id})">
         <i class="fa fa-edit"></i>
          </button></td>
        </tr>
        `
    }
    document.getElementById("tbodyShelf").innerHTML = shelfData;
}

///////////////////////////add shelf////////////////////////////////////////

if(addshelf){
    addshelf.addEventListener('click',()=>{
        const data = {
            name: shelfName.value,
            capacity:capcity.value,
            expiry_date:expiry_date.value

        } 
        axios({
            method: "post",
            url: `${local_server}/api/Shelf/`,
            data: data
        }).then((response)=>{
            console.log(response);
            if(response.status === 201){
                window.open(`${local_server}/shelf/`)
                showShelf()
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

//////////////////////delete shelf ////////////////////////////////////

const deleteShelf = (id)=>{
    axios({
        method:"delete",
        "url":`${local_server}/api/Shelf/${id}/delete/`
    }).then((response)=>{
        getShelf()
    })
    }

//////////////////update shelf ///////////////////////////

const updateShelf =(id)=>{
    localStorage.setItem('shelfId',id)
    window.open(`${local_server}/updateshelf/`)
    }




