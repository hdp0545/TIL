window.addEventListener('load', init, false);

function init () {
	var p = document.getElementsByTagName("p");
	p[0].addEventListener('click', openSub, false);
	p[1].addEventListener('click', openSub2, false);

	function openSub () {
		var w = window.open("sub.html", "sub", "width=500, height=350, menubar=yes, location=yes, resizable=yes, scrollbars=yes, status=yes");
	}

	function openSub2 () {
		var w = window.open("sub2.html", "sub2", "width=400, height=350, menubar=yes, location=yes, resizable=yes, scrollbars=yes, status=yes");
	}
}