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


today.setFullYear(2011);
document.writeln("<p>" + today.getFullYear() + "</p>");

document.writeln("<p>" + today.toUTCString() + "</p>");
document.writeln("<p>" + today.toLocaleString() + "</p>");
document.writeln("<p>" + today.toLocaleDateString() + "</p>");
document.writeln("<p>" + today.toLocaleTimeString() + "</p>");
