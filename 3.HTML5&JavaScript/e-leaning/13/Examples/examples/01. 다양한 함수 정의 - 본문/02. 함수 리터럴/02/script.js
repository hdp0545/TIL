// 숫자 리터럴
var originNum = 1234.567;
// 문자 리터럴
var originStr = "Hello World!";

var originNum2 = originNum.toFixed(1);
var originStr2 = originStr.replace("Hello", "Hi");

document.write(originNum2 + "<br>");
document.write(originStr2 + "<br>");

// 선언적 함수 정의
function sayHi(name) {
	return 'Hi ' + name + '!';
}

// 선언적 함수 정의로 정의된 함수도 객체와 같이 메소드와 프로퍼티를 적용
var sayHiArgLength = sayHi.length;
document.write(sayHiArgLength + "<br>");

// 함수 리터럴 표현
var toCelsius = function(fahr) {
	return Math.floor(5 * (fahr - 32) / 9);
};
var value = toCelsius(100);
document.write(value + "<br>");

// 함수 리터럴은 정의 후 바로 호출되어 실행하거나 다른 함수의 전달인자로 전달될 수도 있다.
var tempFahr = 100;
document.write("화시 " +  tempFahr + "도는 섭시 " + (function(fahr) { return Math.floor(5 * (fahr - 32) / 9); })(tempFahr) + "입니다.<br>");

// 아래 코드는 위 함수 리털러 코드의 선언적 함수 버전이다.
var TempFahr = 100;
function toCelsius(fahr) {
	var celsius = Math.floor(5 * (fahr - 32) / 9);
	return celsius;
}

var temp = toCelsius(TempFahr);

document.write("화시 " +  tempFahr + "도는 섭시 " +  temp + "입니다.");


/*
// 선언적 함수 정의로 정의된 함수는 함수 정의 위치와 상관 없이 함수 호출이 가능하다.
var temp = toCelsius(100);

document.write("화시 100도는 섭시 " +  temp + "입니다.");


function toCelsius(fahr) {
	var celsius = Math.floor(5 * (fahr - 32) / 9);
	return celsius;
}
*/

// 다음 코드는 함수 리털러 정의 보다 함수 호출이 앞서 있기 때문에 에러를 발생하고 실행되지 않는다.
var temp = toCelsius(100);

document.write("화시 100도는 섭시 " +  temp + "입니다.");

var toCelsius = function(fahr) { return Math.floor(5 * (fahr - 32);