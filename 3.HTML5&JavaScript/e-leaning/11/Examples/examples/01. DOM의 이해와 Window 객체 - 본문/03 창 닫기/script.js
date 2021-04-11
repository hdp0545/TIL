window.addEventListener('load', init, false);

var windowOpenFlag = new Object;


function init () {
	var p = document.getElementsByTagName("p");
	var w;
	p[0].addEventListener('click', openSub, false);
	p[1].addEventListener('click', closeSub, false);

	function openSub () {
		w = window.open("sub.html", "sub", "width=500, height=350, menubar=yes, location=yes, resizable=yes, scrollbars=yes, status=yes");
	}

	function closeSub () {
		w.close();
	}
}