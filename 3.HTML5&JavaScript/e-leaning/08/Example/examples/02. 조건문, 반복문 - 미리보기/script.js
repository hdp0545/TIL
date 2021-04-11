// 버튼을 누르면 checkSelect 함수가 호출됩니다.
document.forms[0].button.addEventListener('click', checkSelect, false);

function checkSelect() {
	// HTML 코드의 background 이름을 가진 폼 요소의 값을 변수 schoolBG에 넣는다.
	var schoolBG = document.forms[0].background.value;
	
	// 변수 schoolBG의 값에 따라 switch 문이 분기한다.
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
		case "university":	// "university" 와 "graduate" 부분은 같은 코드로 처리한다.
		case "graduate":
			console ("대학교 이상의 학력입니다.");
			break;
	}
}

/*
function checkSelect() {
	// HTML 코드의 background 이름을 가진 폼 요소의 값을 변수 schoolBG에 넣는다.
	var schoolBG = document.forms[0].background.value;
	
	// if ~ else if ~ 문을 이용하여 변수 schoolBG의 값에 따라 다른 문장 출력
	if (schoolBG == "primary") {
		console ("초등학교를 졸업하셨습니다.");
	} else if (schoolBG == "middle") {
		console ("중학교를 졸업하셨습니다.");
	} else if (schoolBG == "high") {
		console ("고등학교를 졸업하셨습니다.");
	// "university" 와 "graduate" 부분은 같은 코드로 처리한다.
	} else if (schoolBG == "university" || schoolBG == "graduate") {
		console ("대학교 이상의 학력입니다.");
	}
}
*/

function console (outputString) {
	document.getElementById('console').innerHTML = outputString;
}

