const dragArea = document.querySelector(".drag-area");
const dragText = dragArea.querySelector('h2');
const button = dragArea.querySelector('button');
const input = dragArea.querySelector("#input-file");
let files;

button.addEventListener("click", (e) =>{
    input.click();
});

input.addEventListener("change", (e) => {
    files = this.files;
    dragArea.classList.add("activate");
    showFiles(files);
    dragArea.classList.remove("activate");
});

dragArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dragArea.classList.add("activate");
    dragText.textContent = "suelta para subir los archivos";
});

dragArea.addEventListener("dragleave", (e) => {
    e.preventDefault();
    dragArea.classList.remove("activate");
    dragText.textContent = "suelta para subir los archivos";
});

dragArea.addEventListener("drop", (e) => {
    e.preventDefault();
    files = e.dataTransfer.files;
    showFiles(files);
    dragArea.classList.remove("activate");
    dragText.textContent = "suelta para subir los archivos";
});

function showFiles(files){
    if(files.length == undefined){
        processFile(files);
    } else {
        for(const file of files){
            processFile(file);
        }
    }
}

function processFile(file){
    const docType = file.type;
    const validExtensions = ['text/csv'];

    if(validExtensions.includes(docType)){
        //archivo valido
        console.log("se cargo el archivo");
        const fileReader = new FileReader();
        const id = `file-${Math.random().toString(32).substring(7)}`;

        fileReader.addEventListener('load', e => {
            console.log("se cargo el archivo");
        });

        
    }else{
        //no es valido
        alert('No es un archivo valido');
    }
}