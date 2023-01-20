const janela = document.getElementById('janela');
const grafico = janela.getContext('2d');

grafico.imageSmoothingEnabled = true;
grafico.imageSmoothingQuality = "high";

const info = document.getElementById("info");
let tipo = 'Eu';
let caminho = '';

janela.addEventListener('mousemove', function (event) {
    
    const rect = janela.getBoundingClientRect();
    const x = event.clientX - rect.left - 5;
    const y = event.clientY - rect.top - 5;

    grafico.fillStyle = 'white';
    grafico.clearRect(0, 0, rect.width, rect.height);
    
    desenhaReferencias();

    grafico.fillRect(x, y, 3, 22);
    grafico.fillRect(x, y, 3, -20);
    grafico.fillRect(x, y, 22, 3);
    grafico.fillRect(x, y, -20, 3);

    info.innerHTML = "x: " + parseInt(x) + ", y: " + parseInt(y);
});

janela.addEventListener('click', function (event) {
    
    const rect = janela.getBoundingClientRect();
    const x = event.clientX - rect.left - 5;
    const y = event.clientY - rect.top - 5;

    window.location = (caminho + '/' + tipo + '/' + parseInt(x) + '/' + parseInt(y) + '/novo');
});

var imagens = [];

class Imagem {
    constructor(img, x, y){
        this.img = img;
        this.x = x;
        this.y = y;
    }
}

function setTipo(entrada){
    tipo = entrada
}

function clickNovaReferencia(){

}

function carregarReferencia(tipo, x, y) {
    imagens.push(new Imagem(document.querySelector("#" + tipo).cloneNode(true), x, y));
}

function desenhaReferencias() {    
    for (let index = 0; index < imagens.length; index++) {
        grafico.drawImage(imagens[index].img, imagens[index].x -25, imagens[index].y - 25, 50, 50);
    }
}

setTimeout(() => {
    desenhaReferencias();
}, 300);