var btns = document.getElementsByClassName("btns");
var slide = document.getElementById("slide");

btns[0].onclick = function(){
    slide.style.transform = "translatex(0px)";
    for(i=0;i<4;i++){
        btns[i].classList.remove("active")
    }
    this.classList.add("active")
}
btns[1].onclick = function(){
    slide.style.transform = "translatex(-800px)";
    for(i=0;i<4;i++){
        btns[i].classList.remove("active")
    }
    this.classList.add("active")
}
btns[2].onclick = function(){
    slide.style.transform = "translatex(-1600px)";
    for(i=0;i<4;i++){
        btns[i].classList.remove("active")
    }
    this.classList.add("active")
}
btns[3].onclick = function(){
    slide.style.transform = "translatex(-2400px)";
    for(i=0;i<4;i++){
        btns[i].classList.remove("active")
    }
    this.classList.add("active")
}

