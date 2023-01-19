function ofertar(id, max){
    let entrada = document.getElementById("entrada");
    entrada.style.display = "flex";
    
    idOferta = document.getElementById("idOferta");
    idOferta.value = id;
    idValor = document.getElementById("idValor");
    idValor.value = 1;
    idValor.max = max;
}

function cancelarOfertar(){
    entrada.style.display = "none";
}