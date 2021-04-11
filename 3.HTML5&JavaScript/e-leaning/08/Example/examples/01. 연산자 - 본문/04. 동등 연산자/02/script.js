var a = [1,2,3,4];
var b = [1,2,3,4];
var c = a;

if (a == b) {
	document.writeln("같은 값의 배열 a와 b는 동등합니다.<br>");
} else {
	document.writeln("같은 값의 배열 a와 b는 동등하지 않습니다.<br>");
}

if (a == c) {
	document.writeln("같은 값의 배열 a와 c는 동등합니다.");
} else {
	document.writeln("같은 값의 배열 a와 c는 동등하지 않습니다.");
}