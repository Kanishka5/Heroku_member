window.onscroll = function() {myFunction()};

function myFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("navbar").className = "navbar navbar-default navbar-fixed-top";
    } else {
        document.getElementById("navbar").className = "navbar navbar-default navbar-fixed-top  my-navbar";
    }
}
