window.onscroll = function() {
  var gradient = document.querySelector(".container").offsetTop;

  if (gradient == 0) {
    gradient = 1
  }

  var opac = 0;
  if (window.pageYOffset > 0) {
    opac = (window.pageYOffset / gradient);
  }

  document.body.style.background = "linear-gradient(rgba(255, 255, 255, " + opac + "), rgba(255, 255, 255, " + opac + ")), url(static/js/background_gradient.jpg) no-repeat";
}
