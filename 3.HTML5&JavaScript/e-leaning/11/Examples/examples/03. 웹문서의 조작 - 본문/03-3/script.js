var newElement = document.createElement("p");
var newTextNode = document.createTextNode("이것은 자바스크립트에 의해 생성된 단락입니다.");

var h3Element = document.getElementsByTagName("h3")[0];
var newHTMLCode = newElement.appendChild(newTextNode);

document.getElementsByTagName("body")[0].replaceChild(newHTMLCode, h3Element);