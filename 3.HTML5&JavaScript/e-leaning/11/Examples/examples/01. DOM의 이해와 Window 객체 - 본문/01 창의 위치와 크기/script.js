window.addEventListener('load', init, false);

function init() {
	var windowWidth = window.outerWidth;
	var windowHeight = window.outerHeight;
	
	alert("windowWidth = " + windowWidth + ", windowHeight = " + windowHeight);
	
	var windowX = window.screenX;
	var windowY = window.screenY;
	
	alert("windowX = " + windowX + ", windowY = " + windowY);
	
	var viewportWidth = window.innerWidth;
	var viewportHeight = window.innerHeight;
	
	alert("viewportWidth = " + viewportWidth + ", viewportHeight = " + viewportHeight);
	
	var horizontalScroll = window.pageXOffset;
	var verticalScroll = window.pageYOffset;
	
	alert("horizontalScroll = " + horizontalScroll + ", verticalScroll = " + verticalScroll);
}