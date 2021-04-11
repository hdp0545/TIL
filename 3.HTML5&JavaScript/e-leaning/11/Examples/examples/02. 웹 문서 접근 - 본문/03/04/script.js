var habit3 = document.getElementsByClassName("listTitle")[2].nextSibling.textContent;

console("세 번째 습관은 \"" + habit3 + "\"입니다.");

function console (outputString) {
	document.getElementById("console").innerHTML = outputString;
}