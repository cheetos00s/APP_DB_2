function updateFileLabel() {
    const fileInput = document.getElementById("file");
    const fileLabel = document.getElementById("file-label");

    if (fileInput.files.length > 0) {
        fileLabel.textContent = fileInput.files[0].name;
    } else {
        fileLabel.textContent = "Choose File";
    }
}

// Llamada inicial a la función para establecer el texto del label
updateFileLabel();

// Agregar el evento change al input file
const fileInput = document.getElementById("file");
fileInput.addEventListener("change", updateFileLabel);