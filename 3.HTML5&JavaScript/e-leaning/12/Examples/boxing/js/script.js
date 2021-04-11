window.addEventListener('load', init, false);

function init (event) {
	document.addEventListener('mousemove', mouseMove, false);
	document.addEventListener('mousedown', mouseDown, false);
	document.addEventListener('mouseup', mouseUp, false);
}

function mouseMove (event) {
	event.preventDefault();
	var boxingGlove = document.getElementById("boxingGlove");
	var cursorX = event.clientX;
	var cursorY = event.clientY;

	// 70과 50 픽셀을 뺀 것은 움직임의 중심이 글로브 이미지 좌측 상단이 아니라 
	// 글로브 주먹 주간 쯤으로 옮기기 위한 좌표 보정입니다.
	// 이 코드를 게임 등에서 사용할 때 반응성을 좋게 하기 위함입니다.
	boxingGlove.style.left = cursorX - 70 + "px";
	boxingGlove.style.top = cursorY - 50 +"px";
}

function mouseDown (event) {
	event.preventDefault();
	document.getElementById("boxingGlove").setAttribute("src", "img/boxing_glove_s.png");
}

function mouseUp (event) {
	document.getElementById("boxingGlove").setAttribute("src", "img/boxing_glove.png");
}