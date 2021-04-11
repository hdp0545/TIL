window.addEventListener('load', init, false);

function init(event) {
	var dataClass = document.getElementsByClassName("data");
	var toggleTextClass = document.getElementsByClassName("toggleText");
	var carsClass = document.getElementsByClassName("cars");

	for (var i = 0; i < dataClass.length; i++) {
		dataClass[i].style.display = "none"
		toggleTextClass[i].innerHTML = "Show Data";
		carsClass[i].addEventListener('click', targeting, false);
		toggleTextClass[i].addEventListener('click', folding, false)
	}
}

function folding (event) {
	event.preventDefault();
	init.onToggleText = true;
}

function targeting (event) {
	event.stopPropagation();
	if (init.onToggleText == true) {
		var subNode = event.currentTarget.childNodes[3];
		if (subNode.style.display == "none") {
			subNode.style.display = "block";
			event.target.innerHTML = "Hide Data";
		} else {
			subNode.style.display = "none";
			event.target.innerHTML = "Show Data";
		}
		init.onToggleText = false;
	}
}