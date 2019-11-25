function displayOnScreen(subject, matter) {
    document.getElementById("subject").innerText = subject;
    document.getElementById("matter").innerHTML = `<p>${matter}</p>`;
}