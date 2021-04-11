// Dustin Diaz의 커링 함수
// curry 함수는 전달인자로 함수와 
// 함수가 어떤 객체의 메소드로 호출되게 하고자 할때의 메소드를 받는다.
function curry(fn, scope) {
	// 논리 OR를 이용하여 만일 scope가 null이 아니라면 scope를
	// null이나 false이면 window를 변수 scope에 할당
	// 논리 OR는 둘 중에 하나 이상이 참이면 참이 반환됩니다.
	// 또는 좌항이 참이면 좌항의 식이 거짓이면 우항의 식이 반환됩니다. 
	var scope = scope || window;
	// 함수의 전달인자를 저장할 배열 변수 생성
	var args = [];
	// 변수 i가 2부터 시작하는 것은 curry 함수의 0번째와 1번째는 fn과 scope이기 때문
	// 자바스크립트 함수는 함수 정의에 없는 전달인자를 사용할 수 있음.
	for(var i=2; i<arguments.length; i++) {
		// 세번째 전달인자부터 args 배열에 넣는다.
		args.push(arguments[i]);
	};
	// 클로저 함수를 반환한다.
	return function() {
		// 이 클로저 함수의 전달인자를 저장할 배열 변수 생성
		var args2 = [];
		for(var i=0; i<arguments.length; i++) {
			args2.push(arguments[i]);
		}
		// 호출함수의 args와 현재 함수의 args2를 concat으로 합친다.
		var argsTotal = args.concat(args2);
		// 수집된 전달인자 함수에 적용하여 결과를 반환한다.
		return fn.apply(scope, argsTotal);
	};
}

// curry 함수 테스트 1
function addAll (a, b, c, d, e) {
	return a + b + c + d + e;
}
var newAddAll = curry(addAll, null, 2, 3);
var result = newAddAll(4, 5, 6);

document.write(result + "<br>");	// 20이 출력

// curry 함수 테스트 2
function multipleTri (a, b, c) {
	return a*b*c;
}
var newMultipleTri = curry(multipleTri, null, 2);
var result2 = newMultipleTri(3,4);
document.write(result2 + "<br>");	// 24가 출력