// 재귀함수로 구현한 펙토리얼 함수
function factorial(n) {
	if(n > 1) {
		return n * factorial(n-1);
	} else {
		return 1;
	} 
}

/*
// 반복문으로 구현한 펙토리얼 함수
function factorial(n) {
	var result = 1;
	while(n > 1) {
		result = result * n--;
	}
	return result;
}

alert(factorial(5));
*/



/*
// 함수 리터럴을 이용한 재귀함수
var factorialFunc = function(n) {
	if(n > 1) {
		return n * factorialFunc(n-1);
	} else {
		return 1;
	} 
}
*/

// 함수 리터럴에 함수 이름을 지정하면 함수 내부에서만 접근할 수 있다. 그렇기 때문에 재귀함수 구현에 적합하다.
var factorialFunc = function factorial(n) {
	if(n > 1) {
		return n * factorial(n-1);
	} else {
		return 1;
	} 
}

alert(factorialFunc(10));