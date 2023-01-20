var chat = document.getElementById("chat");
chat.scrollTop = chat.scrollHeight;
document.getElementById("aceitar").value = 'False';

function ofertar(id, max){
    let entrada = document.getElementById("entrada");
    entrada.style.display = "flex";
    
    idOferta = document.getElementById("idOferta");
    idOferta.value = id;
    idValor = document.getElementById("idValor");
    idValor.value = 1;
    idValor.max = max;
}

function denunciar(){
    let entrada = document.getElementById("entrada");
    entrada.style.display = "flex";
}

function cancelarDenuncia(){
    entrada.style.display = "none";
}