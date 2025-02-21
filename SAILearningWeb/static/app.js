let contador = 0;
function myFunctin(){
  contador++
  let Elemento = document.getElementById("ddl");
  if(contador%2 == 0){
    
    console.log(Elemento);
    Elemento.style.display = "none";
  }
  else {
    Elemento.style.display = "block";
  }
  
}

function redirectLogout() {
  window.location.href = "http://127.0.0.1:8000/logout/";
}
  