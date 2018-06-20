

var myVar;

function load() {
    myVar = setTimeout(showPage, 2000);
}

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("comingsoon").style.display = "block";
}
