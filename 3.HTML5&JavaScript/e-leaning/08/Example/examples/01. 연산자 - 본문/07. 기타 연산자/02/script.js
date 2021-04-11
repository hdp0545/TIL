var a = [123, "orange", "pink"];
if (2 in a) {
	document.writeln("orange는 배열 a에 존재합니다.");
} else {
	document.writeln("orange는 배열 a에 존재하지 않습니다.");
}

/*
var o = { a: 123, b: "orange", c: "pink"};
if ("b" in o) {
	document.writeln("orange는 객체 o의 프로퍼티 값 입니다.");
} else {
	document.writeln("orange는 객체 o의 프로퍼티 값이 아닙니다.");
}
*/