// Wrap every letter in a span
var textWrapper = document.querySelector('.ml2');
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

anime.timeline()
  .add({
    targets: '.ml2 .letter',
    scale: [4,1],
    opacity: [0,1],
    translateZ: 0,
    easing: "easeOutExpo",
    duration: 950,
    delay: (el, i) => 70*i
  })

var url = "http://colormind.io/api/";
var data = {
  model : "default",
  input : [[44,43,44],[90,83,82],"N","N","N"]
}

var http = new XMLHttpRequest();

http.onreadystatechange = function() {
  if(http.readyState == 4 && http.status == 200) {
      var palette = JSON.parse(http.responseText).result;
  }
}

http.open("POST", url, true);
http.send(JSON.stringify(data));
