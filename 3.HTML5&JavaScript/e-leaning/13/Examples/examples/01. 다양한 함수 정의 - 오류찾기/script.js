// 배열에 있는 원소들의 펙토리얼을 구해 새로운 배열을 만든 후
// 'n!(펙토리얼)은 m입니다.' 형식으로 출력합니다.

// 재귀함수로 구현한 펙토리얼입니다.
// 함수 리터럴로 정의 되었기 때문에 호출 전에 정의 되어야 합니다.
// 이 함수는 배열 원소에 하나씩 적용되어 결과를 새로운 배열을 생성하기 위한 콜백함수로 사용될 것 입니다.
var factorialFunc = function factorial(n) {
	if(n > 1) {
		return n * factorial(n-1);
	} else {
		return 1;
	} 
}

// 펙토리얼 배열을 출력하기 위한 콜백함수 입니다.
var printFactorialArr = function(element, index, array) {
	// element 전달인자는 배열 원소를 의미합니다.
	// index 전달인자 배열을 인덱스를 의미합니다.
	document.write("<p>" + (index+1) + "!(펙토리얼)은 " + element + "입니다.</p>");
}

// 펙토리얼을 구하기 위한 배열
var arr = [1,2,3,4,5,6,7,8,9,10];
// 위 배열 원소들의 펙토리얼을 구하기 위해 map 메소드를 사용하여 factorialFunc 콜백함수를 호출
// 결과는 factorialArr 변수에 배열로 할당
var factorialArr = arr.map(factorialFunc);

// 결과를 출력하기 위해 forEach 메소로 printFactorialArr 콜백함수 호출
factorialArr.forEach(printFactorialArr);