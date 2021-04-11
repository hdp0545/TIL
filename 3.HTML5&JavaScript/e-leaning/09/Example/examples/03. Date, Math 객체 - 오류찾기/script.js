// 배열을 이용한 요일 생성
var weekday = ["일", "월", "화", "수", "목", "금", "토"];
var today = new Date();
document.writeln("<p>오늘은 " + weekday[today.getDay()] + "요일 입니다.</p>")

// 
var sin30 = Math.sin(toRadian(30));
sin30 = sin30.toFixed(1);
document.writeln("<p>sin30도는 " + sin30 + "입니다.</p>");

function toRadian(deg) {
	return deg * (Math.PI/180);
}

