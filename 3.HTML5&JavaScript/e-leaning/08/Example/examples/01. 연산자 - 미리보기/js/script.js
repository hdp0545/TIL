var n1 = 123;
var s1 = "456";
var result;

result = n1 + s1;
document.writeln(n1 + " + \"" + s1 + "\" = " + result + "<br>");

result = s1 - n1;
document.writeln("\"" + s1 + "\" - " + n1 + " = " + result + "<br>");

result = n1 * s1;
document.writeln(n1 + " * \"" + s1 + "\" = " + result + "<br>");

result = s1 / n1;
document.writeln("\"" + s1 + "\" / " + n1 + " = " + result + "<br>");

result = s1 % n1;
document.writeln("\"" + s1 + "\" % " + n1 + " = " + result + "<br><br>");

result = -n1;
document.writeln("양수 123에 단항 마이너스 연산자 적용: " + result + "<br><br>");

var i = 1;
var k = 1;

var j = ++i;
var y = k++;

document.writeln("i = 1, k = 1<br>");
document.writeln("j = ++i<br>");
document.writeln("j = " + j + "<br>");
document.writeln("i = " + i + "<br>");

document.writeln("y = k++<br>");
document.writeln("y = " + y + "<br>");
document.writeln("k = " + k + "<br><br>");

var a = [1,2,3,4];
var b = [1,2,3,4];
var c = a;

if (a == b) {
	document.writeln("같은 값의 배열 a와 b는 동등합니다.<br>");
} else {
	document.writeln("같은 값의 배열 a와 b는 동등하지 않습니다.<br>");
}

if (a == c) {
	document.writeln("같은 값의 배열 a와 c는 동등합니다.<br><br>");
} else {
	document.writeln("같은 값의 배열 a와 c는 동등하지 않습니다.<br><br>");
}

var testArray = [123, "orange", "pink"];
if (2 in testArray) {
	document.writeln("orange는 배열 a에 존재합니다.");
} else {
	document.writeln("orange는 배열 a에 존재하지 않습니다.");
}