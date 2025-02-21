var video = document.querySelector("#videoElement");
var canvas = document.querySelector("#canvas");
var detectador = document.querySelector("#detectador");
const semaforos = document.querySelectorAll('.semaforo');
var contador = 4;
var nivel = document.querySelector("h1").textContent.split(" ")[1];
var im = document.querySelector(".letras");

// Función para redirigir al siguiente nivel
function goToNextLevel() {
    window.location.href = "http://127.0.0.1:8000/niveles/nivel/" + (parseInt(nivel) + 1) + "/";
}

listaNiveles = [
    ['A', 'A', 'A', 'A', 'A'],
    ['B', 'B', 'B', 'B', 'B'],
    ['A', 'B', 'A', 'B', 'A'],
    ['C', 'C', 'C', 'C', 'C'],
    ['A', 'B', 'C', 'A', 'B'],
    ['D', 'D', 'D', 'D', 'D'],
    ['A', 'B', 'C', 'D', 'A'],
    ['E', 'E', 'E', 'E', 'E'],
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'F', 'F', 'F', 'F'],
    ['A', 'B', 'C', 'D', 'F'],
    ['G', 'G', 'G', 'G', 'G'],
    ['A', 'B', 'C', 'D', 'G'],
    ['H', 'H', 'H', 'H', 'H'],
    ['A', 'B', 'C', 'D', 'H'],
    ['I', 'I', 'I', 'I', 'I'],
    ['A', 'B', 'C', 'D', 'I'],
    ['L', 'L', 'L', 'L', 'L'],
    ['A', 'B', 'C', 'D', 'L'],
    ['M', 'M', 'M', 'M', 'M'],
    ['A', 'B', 'C', 'D', 'M'],
    ['N', 'N', 'N', 'N', 'N'],
    ['A', 'B', 'C', 'D', 'N'],
    ['O', 'O', 'O', 'O', 'O'],
    ['A', 'B', 'C', 'D', 'O'],
    ['P', 'P', 'P', 'P', 'P'],
    ['A', 'B', 'C', 'D', 'P'],
    ['Q', 'Q', 'Q', 'Q', 'Q'],
    ['A', 'B', 'C', 'D', 'Q'],
    ['R', 'R', 'R', 'R', 'R'],
    ['A', 'B', 'C', 'D', 'R'],
    ['S', 'S', 'S', 'S', 'S'],
    ['A', 'B', 'C', 'D', 'S'],
    ['T', 'T', 'T', 'T', 'T'],
    ['A', 'B', 'C', 'D', 'T'],
    ['U', 'U', 'U', 'U', 'U'],
    ['A', 'B', 'C', 'D', 'U'],
    ['V', 'V', 'V', 'V', 'V'],
    ['A', 'B', 'C', 'D', 'V'],
    ['W', 'W', 'W', 'W', 'W'],
    ['A', 'B', 'C', 'D', 'W'],
    ['Y', 'Y', 'Y', 'Y', 'Y'],
    ['A', 'B', 'C', 'D', 'Y'],
    ['A', 'E', 'I', 'O', 'U'],
    ['B', 'F', 'M', 'P', 'V'],
    ['C', 'G', 'L', 'Q', 'W'],
    ['D', 'H', 'N', 'R', 'S'],
    ['E', 'I', 'O', 'U', 'A'],
    ['F', 'L', 'M', 'P', 'B'],
    ['G', 'N', 'Q', 'R', 'C'],
    ['H', 'O', 'S', 'T', 'D'],
    ['I', 'P', 'U', 'V', 'E'],
    ['L', 'Q', 'W', 'A', 'F'],
    ['M', 'R', 'B', 'C', 'G'],
    ['N', 'S', 'D', 'E', 'H'],
    ['O', 'T', 'F', 'G', 'I'],
    ['P', 'U', 'H', 'I', 'L'],
    ['Q', 'V', 'M', 'N', 'O'],
    ['R', 'W', 'P', 'Q', 'S'],
    ['S', 'Y', 'R', 'T', 'U']
]

im.src = "/static/images/letrasLSM/letra_" + listaNiveles[(nivel % 60)][contador] + ".png";
 
if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
            video.srcObject = stream;
            // Inicia el pulso después de obtener acceso a la cámara
            startPulse();
        })
        .catch(function (err0r) {
            console.log("Something went wrong!");
        });
}

function redirectLogout() {
    window.location.href = "http://127.0.0.1:8000/logout/";
  }

function startPulse() {
    // Llama a captureAndSendFrame cada 500 milisegundos
    setInterval(captureAndSendFrame, 250);
}

function captureAndSendFrame() {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    var context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    canvas.toBlob(function(blob) {
        sendFrame(blob);
    }, 'image/png');
}


function sendFrame(blob) {
    var formData = new FormData();
    formData.append('file', blob, 'frame.png');

    fetch('http://127.0.0.1:8080/api/upload/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        detectador.innerHTML = 'Actualmente detectando: ' + data['letra'];
        if (data['letra'] == listaNiveles[(nivel % 60)][contador] && contador > 0){
            const semaforo = semaforos[contador]; 
            semaforo.style.backgroundColor = 'green';
            contador--;
            im.src = "/static/images/letrasLSM/letra_" + listaNiveles[(nivel % 60)][contador] + ".png";
        }
        else if (contador == 0) {
            goToNextLevel();
        } 
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
