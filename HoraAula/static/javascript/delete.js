function seleciona(button) {
    switch (button) {
        case 'button1':
            button = document.getElementById('button1');
            break;
        case 'button2':
            button = document.getElementById('button2');
            break;
        case 'button3':
            button = document.getElementById('button3');
            break;
        case 'button4':
            button = document.getElementById('button4');
            break;
        default:
            console.log("não entrou em nenhuma condição");
            break;
        }
    if(button.value == 0){
        button.style.background = "red";
        button.style.color = "white";
        button.value = 1;
    }else{  
        button.style.background = "gray";
        button.style.color = "black";
        button.value = 0;
    }
}
function reload(e){
    var select = document.getElementById("escolha-dia");

     // select.addEventListener("change", function(e) {
        localStorage.setItem("selected", e.target.value);
     // });

      var opts = select.options;
      for (var opt, j = 0; opt = opts[j]; j++) {
        if (opt.value == localStorage.getItem("selected")) {
          select.selectedIndex = j;
          break;
        }
      }
      window.location.reload();
   
}

(function(){
    var select = document.getElementById("escolha-dia");
    storage = localStorage.getItem("selected");
    if(storage != " "){
        select.value =  localStorage.getItem("selected");
    }
})();