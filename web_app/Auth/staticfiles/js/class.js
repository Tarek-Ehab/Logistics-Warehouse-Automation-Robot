//variables
let title = document.getElementById('title')
let addClassBtn = document.getElementById('add') 
let msgClass = document.getElementById('msgClass')
let update = document.getElementById('update')
let allInputs = document.getElementsByClassName('form-control');


//classifcation

/////////////////////////////get all classification //////////////////////////

let classificationsArr = [];
const getClassi = ()=>{
    axios({
        method:"get",
        url:`${local_server}/api/Classification/`
    }).then((response)=>{
        const {data}= response;
        classificationsArr = data;
        showClass()
    }).catch((error)=> {
        console.log(error);
      })
}

getClassi()

////show all classification //////////////////////////
const showClass = ()=>{
    let cartona =``
    for(let i=0;i< classificationsArr.length;i++){
        cartona+= `<tr>
        <td>${classificationsArr[i].title}</td>
        <td>  <button type="button" class="btn btn-danger mx-4 " onclick="deleteClass(${classificationsArr[i].id})">
        <i class="fa fa-trash"></i>
         </button>
         <button type="button" class="btn btn-primary "  onclick="updateClass(${classificationsArr[i].id})">
         <i class="fa fa-edit"></i>
          </button></td>
          <td><button type="button" class="btn btn-primary "  onclick="classProducts(${classificationsArr[i].id})">
          <i class="fa-solid fa-list"></i>
           </button></td>
        </tr>
        `
    }
    document.getElementById("tbodyClass").innerHTML = cartona;
}
//////add classifications/////
if(addClassBtn){
    addClassBtn.addEventListener('click',()=>{
        const data = {
            title: title.value
        }
        axios({
            method: "post",
            url: `${local_server}/api/Classification/`,
            data: data
        }).then((response)=>{
            if(response.status === 201){
                window.open(`${local_server}/classification/`)
                showClass()
            }
        }).catch((error)=> {
            msgClass.classList.remove('d-none');
          })
    })
}


///////////////delete classifications ////////////////


const deleteClass = (id)=>{
    axios({
        method:"delete",
        "url":`${local_server}/api/Classification/${id}/delete/`
    }).then((response)=>{
        getClassi()
    })
    }


//////////update classs ////////////////////////

const updateClass =(id)=>{
    localStorage.setItem('classId',id)
    window.open(`${local_server}/updateclassification/`)
    }


//////////////////////////////////////go to products by class page////////////////////////
const classProducts =(id)=>{
    localStorage.setItem('proByclass',id)
    window.open(`${local_server}/productsByClass/`)
    }

    //////////////////////get product by classification ///////////////////////////////



    let classProductsArr = [];
const getClassiProducts = ()=>{
    axios({
        method:"get",
        url:`${local_server}/api/classification/${localStorage.getItem('proByclass')}/products/`
    }).then((response)=>{
        const {data}= response;
        classProductsArr = data;
        showProductsClass()
    }).catch((error)=> {
        console.log(error);
      })
}

getClassiProducts()

////show all classification //////////////////////////
const showProductsClass = ()=>{
    let cartonaPro =``
    for(let i=0;i< classProductsArr.length;i++){
        cartonaPro+= `<tr>
        <td>${classProductsArr[i].classification.title}</td>
        <td>${classProductsArr[i].name}</td>
        <td>${classProductsArr[i].supplier.name}</td>
        <td>${classProductsArr[i].zone.name}</td>
        <td>${classProductsArr[i].shelf.name}</td>
        <td>${classProductsArr[i].price}</td>
        <td>${classProductsArr[i].quantity}</td>
        </tr>
        `
    }
    document.getElementById("classProducts").innerHTML = cartonaPro;
}