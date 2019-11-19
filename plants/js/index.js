var plantNum = 1;
var plantShow = setInterval(cycleBG, 7000);
function cycleBG() {
    document.getElementsByClassName("hero").heroImg.style.backgroundImage=`url('img/bg${plantNum}.jpg')`;
    plantNum = (plantNum < 8) ? plantNum+1:1;     
}
