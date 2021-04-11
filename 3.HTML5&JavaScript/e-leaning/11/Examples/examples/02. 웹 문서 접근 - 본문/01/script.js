window.addEventListener("load", init, false);

function init () {
	document.forms[0].elements[8].addEventListener("click", validForm, false);
}

function validForm () {
	var genderEle = document.forms[0].elements[0];
	var genderEle1 = document.forms[0].elements[1];
	var genderEle2 = document.forms[0].elements[2];
	var birthEle = document.forms[0].elements[3];
	var idCodeEle1 = document.forms[0].elements[4];
	var idCodeEle2 = document.forms[0].elements[5];
	var telCode1 = document.forms[0].elements[6];
	var telCode2 = document.forms[0].elements[7];

	if (!(idCodeEle1.value && idCodeEle2.value)) {
		alert("주민번호는 반드시 입력해야 합니다.");
		idCodeEle1.focus();
	}
}