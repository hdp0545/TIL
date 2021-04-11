document.forms[0].button.addEventListener('click', multi, false);
function multi() {
	var firstNum = document.forms[0].firstnumber.value;
	var secondNum = document.forms[0].secondnumber.value;

	var multiValue = firstNum * secondNum;
	document.forms[0].value.setAttribute('value', multiValue);
}