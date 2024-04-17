let nombre = document.getElementById("nombre")
let email = document.getElementById("email")
let subject = document.getElementById("subject")
let mensaje = document.getElementById("mensaje")


function validacion() {
    if (nombre.value === "" || email.value === "" || subject.value === "") {

    } else {
        alert("Falta completar datos.")
    }
}

var valNombre = contieneNumeros(nombre.value)

if (valNombre == true) {
    alert("El nombre no puede contener numeros.")
}


function contieneNumeros(texto) {
    var contiene = false;
    for (let i = 0; i < texto.length; i++) {
        if (texto[i] == "0" || texto[i] == "1" || texto[i] == "0" || texto[i] == "2" || texto[i] == "3" || texto[i] == "4" || texto[i] == "5" || texto[i] == "6" || texto[i] == "0" || texto[i] == "7" || texto[i] == "8" || texto[i] == "9") {
            contiene = true
        }
    }
    if (contiene == true) {
        return true
    } else {
        return false
    }
}