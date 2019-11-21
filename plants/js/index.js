var plantNum = 1;
var plantShow = setInterval(cycleBG, 7000);
const nextImage = (pre, n, ext) => `url('${pre}${n}${ext}')`;
const imgFolder = "img/bg";

function cycleBG() {
    document.getElementsByClassName("hero")
    .heroImg
    .style
    .backgroundImage = nextImage(imgFolder, plantNum, ".jpg");
    plantNum = (plantNum === 4) ? 1:plantNum+1;
}
