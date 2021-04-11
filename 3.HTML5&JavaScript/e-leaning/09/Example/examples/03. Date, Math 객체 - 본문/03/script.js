
var n1 = 123.456;
var n2 = 345.678;
var n3 = 567.891;

document.writeln("<p>123.456의 반올림값은 " + Math.round(n1) + "입니다.</p>");
document.writeln("<p>345.678의 반올림값은 " + Math.round(n2) + "입니다.</p>");

document.writeln("<p>123.456의 올림값은 " + Math.ceil(n1) + "입니다.</p>");
document.writeln("<p>345.678의 버림값은 " + Math.floor(n2) + "입니다.</p>");


function circelArea (radius) {
	var area = Math.pow(radius, 2) * Math.PI;
	return Math.round(area);
}

var r = 123;
var result = circelArea (r);
document.writeln("<p>반지름이 " + r + "cm인 원의 넓이는 " + result + "cm<sup>2</sup>입니다.</p>");

var smaller = Math.min(n1, n2, n3);
var bigger = Math.max(n1, n2, n3);

document.writeln("<p>" + smaller + "</p>");
document.writeln("<p>" + bigger + "</p>");

var randomNum = Math.floor(Math.random() * 6) + 1;
document.writeln(randomNum);

document.writeln("<p>" + Math.sin(30) + "</p>");


var sin30 = Math.sin(toRadian(30));
var sin30 = sin30.toFixed(1);	// 소숫점 이하 한자리만 보이게 한다.
document.writeln("<p>" + sin30 + "</p>");

function toRadian(deg) {	// 각도를 레디안 값으로 변환하는 함수
	return deg * (Math.PI/180);
}

function toDegree(rad) {	// 레디안 값을 각도로 변환하는 함수
	return rad * (180/Math.PI);
}