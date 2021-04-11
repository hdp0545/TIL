var newElement = document.createElement("p");
var newTextNode = document.createTextNode("이것은 자바스크립트에 의해 생성된 단락입니다.");
document.getElementsByTagName("body")[0].appendChild(newElement).appendChild(newTextNode);