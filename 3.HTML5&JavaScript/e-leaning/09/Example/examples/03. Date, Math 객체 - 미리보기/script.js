var today = new Date();
document.writeln("<p>" + today + "</p>");

var today = new Date(2012,8,2,12,30,30,30);
var cFullYear = today.getFullYear();
var cMonth = today.getMonth();
var cDay = today.getDate();
var cDayOfWeek = today.getDay();
var cHour = today.getHours();
var cMin = today.getMinutes();
var cSec = today.getSeconds();
var cMilSec = today.getMilliseconds();

switch (cDayOfWeek) {
	case 0:
		cDayOfWeek = "일요일";
		break;
	case 1:
		cDayOfWeek = "월요일";
		break;
	case 2:
		cDayOfWeek = "화요일";
		break;
	case 3:
		cDayOfWeek = "수요일";
		break;
	case 4:
		cDayOfWeek = "목요일";
		break;
	case 5:
		cDayOfWeek = "금요일";
		break;
	case 6:
		cDayOfWeek = "토요일";
		break;
}


document.writeln("<p>" + today + "</p>");

document.writeln("<p>" + cFullYear + "년 " + cMonth + "월 " + cDay + "일 " + cDayOfWeek + "</p>");
document.writeln("<p>" + cHour + "시 " + cMin + "분 " + cSec + "초 " + cMilSec + "</p>");
document.writeln("<p>" + today.toLocaleString() + "</p>");

var n1 = 123.456;
var n2 = 345.678;
var n3 = 567.891;

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