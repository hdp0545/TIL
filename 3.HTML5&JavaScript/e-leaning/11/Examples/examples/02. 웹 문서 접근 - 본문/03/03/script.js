var habit3 = document.getElementById("habit").childNodes[5].lastChild.textContent;

console("세 번째 습관은 \"" + habit3 + "\"입니다.");

function console (outputString) {
	document.getElementById("console").innerHTML = outputString;
}