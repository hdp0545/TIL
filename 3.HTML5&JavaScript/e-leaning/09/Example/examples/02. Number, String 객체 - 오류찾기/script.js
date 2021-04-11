// 숫자를 천단위마다 쉼표로 자릿수를 표시한다.
var num = 3485729353458;
var numString = num.toString();
var newNumString = "";

for (var i=numString.length; i>=0; i-=3) {
	if ((i-3)<0) {
		newNumString = numString.substr(0, i) + newNumString;
	} else {
		newNumString = "," + numString.substr(i-3, 3) + newNumString;
	}
}

document.writeln(newNumString);


//문자열에서 콜론과 마침표 사이의 문자열 가져오기
var textLine = "당신이 길렀던 애완용 동물들을 나열하시오: 개, 고양이, 햄스터, 거북이.";
var startChar = textLine.indexOf(":");
var endChar = textLine.lastIndexOf(".");
var animals = textLine.slice(startChar+1, endChar);

document.writeln("<p>" + animals + "</p>");