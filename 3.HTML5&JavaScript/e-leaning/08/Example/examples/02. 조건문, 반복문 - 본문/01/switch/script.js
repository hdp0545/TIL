document.forms[0].button.addEventListener('click', checkSelect, false);

function checkSelect() {
	var schoolBG = document.forms[0].background.value;
	
	switch (schoolBG) {
		case "primary":
			console ("초등학교를 졸업하셨습니다.");
			break;
		case "middle":
			console ("중학교를 졸업하셨습니다.");
			break;
		case "high":
			console ("고등학교를 졸업하셨습니다.");
			break;
		case "university":
		case "graduate":
			console ("대학교 이상의 학력입니다.");
			break;
	}
}

function console (outputString) {
	document.getElementById('console').innerHTML = outputString;
}