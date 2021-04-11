var box = document.getElementsByTagName("div");
var boxTouch = document.getElementsByTagName("a");

boxTouch[0].addEventListener("click", setStyle, false);

function setStyle () {
	var styleType = box[0].getAttribute("class");
	switch(styleType) {
	case "yellow":
		box[0].setAttribute("class", "yellowgreen");
		break;
	case "yellowgreen":
		box[0].setAttribute("class", "pink");
		break;
	case "pink":
		box[0].setAttribute("class", "yellow");
		break;
	}
}