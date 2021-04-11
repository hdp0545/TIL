window.addEventListener('load', init, false);

function init (event) {
	var toolTips = document.getElementsByClassName("toolTip");
	for (var i=0; i<toolTips.length; i++) {
		toolTips[i].addEventListener('mouseover', mouseOver, false);
		toolTips[i].addEventListener('mousemove', mouseOver, false);
		toolTips[i].addEventListener('mouseout', mouseOut, false);
	}
}

function mouseOver (event) {
	event.preventDefault();
	document.body.style.cursor = "help";
	var toolTipContents = event.target.getAttribute("desc");
	var tipBox = document.getElementById("tipBox")

	tipBox.innerHTML = toolTipContents;
	var mousePosX = event.clientX+20;
	var mousePosY = event.clientY+10;

	tipBox.style.display = "block";
	tipBox.style.left = mousePosX + "px";
	tipBox.style.top = mousePosY + "px";
}

function mouseOut (event) {
	event.preventDefault();
	document.body.style.cursor = "default";
	document.getElementById("tipBox").style.display = "none"
}