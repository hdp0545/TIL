document.forms[0].okButton.addEventListener('click', checkName, false);

function checkName() {
	var userName = document.forms[0].username.value;

	userName ? console(userName + "님 안녕하세요.") : console("이름을 입력해 주세요.");
}

function console (outputString) {
	document.getElementById('console').innerHTML = outputString;
}