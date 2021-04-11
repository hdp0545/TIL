var box = document.getElementsByTagName("div");
var boxTouch = document.getElementsByTagName("a");
var clickCount = 0
boxTouch[0].addEventListener("click", setStyle, false);

function setStyle () {
	var styleNum = clickCount % 3;
	switch(styleNum) {
	case 0:
		box[0].style.backgroundColor = "yellowgreen";
		break;
	case 1:
		box[0].style.backgroundColor = "pink";
		break;
	case 2:
		box[0].style.backgroundColor = "yellow";
		break;
	}
	clickCount++;
}