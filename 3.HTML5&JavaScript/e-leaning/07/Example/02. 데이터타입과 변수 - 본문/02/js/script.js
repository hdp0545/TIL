window.addEventListener('load', printMaxMin, false);

function printMaxMin() {
	var maxNumber = Number.MAX_VALUE;
	var minNumber = Number.MIN_VALUE;
	var outputHTML = "";
	
	outputHTML += "자바스크립트에서 표현할 수 있는 가장 큰 수는 " + maxNumber + "입니다.<br>";
	outputHTML += "자바스크립트에서 표현할 수 있는 가장 작은 수는 " + minNumber + "입니다.";
	
	document.getElementsByTagName('p')[0].innerHTML = outputHTML;
}