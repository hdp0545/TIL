// 일반적인 함수 유효범위를 가지는 예
function wrapperFunc() {
	var wrapperVar = 100;
	var sum = innerFunc();
	return sum;
	
	function innerFunc() {
		var innerVar = 50;
		return wrapperVar + innerVar;
	}
}

var result = wrapperFunc();

document.write(result + "<br>");


// 어휘적 유효 범위와 클로저 예
// hiFunc 함수는 내부 함수를 반환하고 종료되어야 합니다.
// 하지만 내부 함수는 호출함수인 hiFunc(이미 종료되어야 했던)의
// 지역 변수인 point를 참조합니다.
// 자바스크립트는 어휘적 유효 범위를 가져 함수가 정의 되었을 때
// 유효 범위을 유지하기 때문에 이와 같은 코드는 유효합니다.
function hiFunc() {
	var point = "!";
	return function(s) {
		return "Hi " + s + point;
	}
}

var temp = hiFunc();
var result2 = temp("James");
document.write(result2 + "<br>");


// 이번 예도 앞서와 같이 호출함수의 유효범위 밖에서 실행된 함수가
// 호출함수의 지역변수를 참조합니다.
// 이렇게 함수가 자신의 유효범위 밖에 있는 
// 데이터에 접근할 수 있는 함수를 클로저라 합니다.
var globalVar;

function wrapperFunc2() {
	var innerVar = 100;
	globalVar = function(n) {
		return n + innerVar;
	}
}

wrapperFunc2();

var result3 = globalVar(50);
document.write(result3 + "<br>");