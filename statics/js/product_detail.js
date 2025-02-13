document.getElementById("details").style.width = "500px";

const subtract = document.querySelector(".subtraction"),
 number = document.querySelector("#quantity"),
 add = document.querySelector(".addition");

let a = 1;

subtract.addEventListener('click', ()=>{
    if(a > 1){
        a--;
        number.value = a;
    }
});

add.addEventListener('click', ()=>{
    a++;
    number.value = a;
});