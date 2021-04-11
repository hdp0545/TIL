window.addEventListener('load', init, false);

function init () {
	document.getElementsByTagName('a')[0].addEventListener('click', popAlert, false);

	function popAlert () {
		window.alert("Hello World!");
	}
}