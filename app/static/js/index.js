import "static/js/data.js";

//selectors
const navbar = document.getElementById("nav-bar");
const subject = document.getElementById("subject");
const matter = document.getElementById("matter");
const firstForm = () => Array(...document.getElementsByTagName('form'))[0];
const lastForm = () => Array(...document.getElementsByTagName('form')).pop();

//setters

//  mono
const displaySubject = (text) => subject.textContent = text;
const displayHTML = (xhtml) => matter.innerHTML = xhtml;

function clearScreen(){
    displaySubject(""); //clear H3
    displayHTML("");  //clear matter
}

const displayParagraph = (text) => {
    displayHTML(""); // clear matter
    const newPara = document.createElement('p'); //create
    newPara.textContent = text;  //assign
    matter.appendChild(newPara);  //assemble
}

const insertElement = (el) => {
    const holdThis = [];
    holdThis.push(matter.innerHTML);
    displayHTML(""); // clear matter
    matter.appendChild(el);
    matter.innerHTML += holdThis.pop();
}

const addParagraph = (text) => {
    const newPara = document.createElement('p'); //create
    newPara.textContent = text;  //assign
    matter.appendChild(newPara);  //assemble
}

const addMenuItem = (url, text) =>  {
    const newItem = document.createElement('a');
    newItem.href = url;
    newItem.textContent = text;
    navbar.appendChild(newItem);
}

// builders
const wrapElement = (el, str) => {
    const outside = document.createElement(str);
    outside.appendChild(el);
    return outside;
}

const buildUrl = (href, text) => {
    const newUrl = document.createElement('a');
    newUrl.href = href;
    newUrl.textContent = text;
    return newUrl;
}

const ulFromUrls = (arr) => {
    const newList = document.createElement('ul');
    newList.appendChild(arr.map((li) => wrapElement(buildUrl(li[0], li[1]), "li")));
    return newList;
}

const pKat = () => {
    const catsMeow = new Audio('static/audio/Meow.ogg');
    const cityCat = document.createElement('p');
    cityCat.style.fontSize = "2rem";
    cityCat.textContent = "🐈";
    catsMeow.play();
    return cityCat
}

function meow() {
    displaySubject("meOw");
    insertElement(pKat());
}

function thatBox() {
    const subject = "That box? i can fit in that box";
    const matter = thatBoxData;
    displaySubject(subject);
    displayHTML(matter);
}


function flaskMoments() {
    /*
        convert UTC timestamps to local human format
        https://github.com/miguelgrinberg/Flask-Moment
        https://momentjs.com/
    */
    function toLocalTime(el, fmt){
        return moment(el.attributes.getNamedItem('data-timestamp').value).format(fmt);
    }
    function toLocalDelta(el) {
        return moment(el.attributes.getNamedItem('data-timestamp').value).fromNow();
    }
    function prettyTime(el, tsFormat=(()=>el.attributes.getNamedItem('data-format').value)) {
        el.innerText = (tsFormat() == "fromNow(0)") ? toLocalDelta(el):toLocalTime(el, tsFormat().split("'")[1])
    }
    Array(...document.getElementsByClassName("flask-moment")).forEach((el) => prettyTime(el));
}

function uFixUp() {
    // sort through the list of posts (paginated)
    // {"url": "https://www.python.org/", "text":"[Python]"}
    function getJSON(el){
        let arr = Array(...el.innerText);
        let start = arr.indexOf('{');
        if (!start) {
            // do nothing
            return;
        }
        let end = 1 + arr.indexOf('}');
        if (!end) {
            // do nothing
            return;
        }
        let alink = JSON.parse(el.innerText.slice(start, end));
        if (!alink){
            // do nothing
            return;
        }
    const newLink = document.createElement('a');
    newLink.target = "_blank";
    newLink.text = alink.text;
    newLink.href = alink.url;
    el.textContent = "";
    el.appendChild(newLink);
    }
    Array(...document.getElementsByClassName("user-posted")).map(getJSON);
}

function exampleMenu(){
    // href="javascript:sndCoin.play().then(console.log('ok'));"
    addMenuItem("javascript:sndCoin.play();", "#!/𝝺 ");
    addMenuItem("javascript:thatBox();", ".thatBox");
    addMenuItem("javascript:meow();", ".meow");
}

function run() {
    flaskMoments(); // run immediately
    uFixUp(); // run immediately
    var localTimeConversion = setInterval(flaskMoments, 10000); // run again every 10 seconds
    var urlFixUp = setInterval(uFixUp, 10000); // again every 10s?
    // maybe this should be run on-change
}

if (!sndSelect){
    var sndSelect = new Audio('static/audio/select.wav');
    var sndCoin = new Audio('static/audio/coin01.wav');
    var sndKey = new Audio('static/audio/key01.wav');
    var sndSelect2 = new Audio('/static/audio/select02.wav');
    var sndJump = new Audio('static/audio/jump01.wav');
}

function loadUrl(newLocation) {
    this.location = newLocation
    return false;
}

function soundClick(n=0){
    return [sndCoin, sndJump, sndKey, sndSelect, sndSelect2][Math.min(n, 4)];
}

function clickUrl(url, n=0, delay=700){
    // function sleep(milliseconds) {
    //     return new Promise(resolve => setTimeout(resolve, milliseconds));
    // }
    // loadUrl(url).then(()=> soundClick(n).play());
    // soundClick(n).play().then(() => sleep(delay).then(() => loadUrl(url)));
    loadUrl(url);
}
