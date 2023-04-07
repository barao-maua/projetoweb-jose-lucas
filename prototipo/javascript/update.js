function seleciona(button) {
    let materia;
    let professor;
    switch (button) {
        case 'button1':
            materia = document.getElementById('materia1');
            professor = document.getElementById('professor1');
            button = document.getElementById('button1');
            break;
        case 'button2':
            materia = document.getElementById('materia2');
            professor = document.getElementById('professor2');
            button = document.getElementById('button2');
            break;
        case 'button3':
            materia = document.getElementById('materia3');
            professor = document.getElementById('professor3');
            button = document.getElementById('button3');
            break;
        case 'button4':
            materia = document.getElementById('materia4');
            professor = document.getElementById('professor4');
            button = document.getElementById('button4');
            break;
        default:
            console.log("não entrou em nenhuma condição");
            break;
        }
    if(materia.disabled == true && professor.disabled == true){
        materia.disabled = false;
        professor.disabled = false;
        button.style.background = "blue";
        button.style.color = "white";
        button.value = 1;
    }else{
        materia.disabled = true;
        professor.disabled = true;
        button.style.background = "gray";
        button.style.color = "black";
        button.value = 0;
    }
}