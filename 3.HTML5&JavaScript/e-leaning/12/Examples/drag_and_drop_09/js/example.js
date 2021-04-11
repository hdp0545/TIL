document.addEventListener('load', dragNdropInit, true);

function dragNdropInit () {
	document.getElementById("drag").addEventListener('mousedown', mouseDown, true);
	document.getElementById("drag").addEventListener('mouseup', mouseUp, true);
}

function mouseDown (event) {
	event.preventDefault();
	
	dragNdropInit.objPosX =  event.target.offsetLeft;
	dragNdropInit.objPosY =  event.target.offsetTop;
	dragNdropInit.startPosX = event.clientX;
	dragNdropInit.startPosY = event.clientY;
	
	document.getElementById("drag").addEventListener('mousemove', mouseMove, true);
}

function mouseMove (event) {	
	var newPosX = event.clientX;
	var newPosY = event.clientY;
	event.target.style.left = dragNdropInit.objPosX + newPosX - dragNdropInit.startPosX + "px";
	event.target.style.top = dragNdropInit.objPosY + newPosY - dragNdropInit.startPosY + "px";
}

function mouseUp (event) {
	document.getElementById("drag").removeEventListener('mousemove', mouseMove, true);
}