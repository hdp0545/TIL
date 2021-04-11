window.addEventListener('load', init, false);

function init(event) {
	var dataClass = document.getElementsByClassName("data");
	var toggleTextClass = document.getElementsByClassName("toggleText");
	var html1Class = document.getElementsByClassName("html1");
	var windowTextClass = document.getElementsByClassName("windowText");

	for (var i = 0; i < dataClass.length; i++) {
		dataClass[i].style.display = "none";
		toggleTextClass[i].innerHTML = "OPEN";
		windowTextClass[i].innerHTML= "OPEN";
		html1Class[i].addEventListener('click', targeting, false);
		toggleTextClass[i].addEventListener('click', folding, false);
		windowTextClass[i].addEventListener('click', openContents,false);
	}
}

function folding (event) {
	event.preventDefault();
	init.onToggleText = true;
	init.onwindowText = true;
}

function targeting (event) {
	event.stopPropagation();
	if (init.onToggleText == true) {
		var subNode = event.currentTarget.childNodes[3];
		if (subNode.style.display == "none") {
			subNode.style.display = "block";
			event.target.innerHTML = "CLOSE";
		} else {
			subNode.style.display = "none";
			event.target.innerHTML = "OPEN";
		}
		init.onToggleText = false;
	}
}

function openContents(event){
	var w;
	event.stopPropagation();
	if(init.onwindowText == true){
		w = window.open("contents.html","contents","width=500, height=350, menubar=yes, location=yes, resizable=yes, scrollbars=yes, status=yes");
	}else{
		w.close();
	}
}