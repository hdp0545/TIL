// var habit3 = document.querySelectorAll(".listTitle")[2].nextSibling.textContent;

var habit3 = document.querySelector("#habit").querySelectorAll("li")[2].lastChild.textContent;

console("세 번째 습관은 \"" + habit3 + "\"입니다.");

function console (outputString) {
	document.getElementById("console").innerHTML = outputString;
}