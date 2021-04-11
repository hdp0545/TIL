window.addEventListener('load', init, false);

function init() {
	document.forms[0].button.addEventListener('click', calc, false);
}

function calc() {
	var firstNum = document.forms[0].firstnumber.value;
	var secondNum = document.forms[0].secondnumber.value;
	var operator = document.forms[0].operator.value;
	var oppValue;

	if (firstNum == "") {
		alert("첫 번째 숫자를 입력하세요.");
		document.forms[0].firstnumber.focus();
	} else if (secondNum == "") {
		alert("두 번째 숫자를 입력하세요.");
		document.forms[0].secondnumber.focus();
	}
	
	switch(operator) {
		case "add":
			oppValue = Number(firstNum) + Number(secondNum);
			break;
		case "subtract":
			oppValue = firstNum - secondNum;
			break;
		case "multiply":
			oppValue = firstNum * secondNum;
			break;
		case "divide":
			if (secondNum == 0) {
				alert("0으로 나누는 것은 허용되지 않습니다.");
				document.forms[0].secondnumber.focus();
				oppValue = ""
				break;
			}
			oppValue = firstNum / secondNum;
			break;
		case "multiplication":
			oppValue = 1;
			while(secondNum > 0) {
				secondNum = secondNum - 1;
				// secondNum --; 
				oppValue = oppValue * firstNum;
			}
			break;
	}
	
/* 	document.forms[0].value.setAttribute('value', oppValue); */
		document.forms[0].value.value = oppValue;

}