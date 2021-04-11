window.addEventListener("load", init, false);

function init () {
	document.personalInfo.button.addEventListener("click", validForm, false);
}

function validForm () {
	var genderEle = document.personalInfo.gender;
	var birthEle = document.personalInfo.birthday;
	var idCodeEle1 = document.personalInfo.IDcode1;
	var idCodeEle2 = document.personalInfo.IDcode2;
	var telCode1 = document.personalInfo.telCode;
	var telCode2 = document.personalInfo.telNum;

	if (genderEle[0].checked) {
		alert("남성이시군요.");
	} else if (genderEle[1].checked) {
		alert("여성이시군요.")
	}

	if (!(idCodeEle1.value && idCodeEle2.value)) {
		alert("주민번호는 반드시 입력해야 합니다.");
		idCodeEle1.focus();
	}
}