// 생성자를 이용한 함수 정의
var toCelsius = new Function("fahr", "return Math.floor(5 * (fahr - 32) / 9);");

// 함수 리터럴 함수 정의
var toCelsius2 = function(fahr) {
	return Math.floor(5 * (fahr - 32) / 9);
};

var value = toCelsius2(100);
document.write("화시 100도는 섭시 "+ value + "도 입니다.<br>");

// 콜백 함수
function isBigEnough(element, index, array) {
  return (element >= 10);
}
var filtered = [12, 5, 8, 130, 44].filter(isBigEnough);

document.write("12, 5, 8, 130, 44 중 10 이상은 " + filtered.toString() + "입니다.<br>");

// 재귀 함수
var factorialFunc = function factorial(n) {
	if(n > 1) {
		return n * factorial(n-1);
	} else {
		return 1;
	} 
}

var factorial10 = factorialFunc(10);
document.write("10 펙토리얼은 " + factorial10 + "입니다.");