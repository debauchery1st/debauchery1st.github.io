var plantNum = 1;
var plantShow = setInterval(cycleBG, 7000);
function cycleBG() {
    document.getElementsByClassName("hero").heroImg.style.backgroundImage=`url('img/bg${plantNum}.jpg')`;
    plantNum = (plantNum === 9) ? 1:plantNum+1;
}
