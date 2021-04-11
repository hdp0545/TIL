// 텍스트 폼에 입력된 값이 문자열인지 숫자인지 판단하는 코드
// 같은 기능을 하는 세 개의 코드 입니다.
// 자바스크립트의 유연한 형변환을 보여줍니다.
// 유연한 형변환이 혼란을 가져오는 경우도 있습니다.

// 버튼을 클릭하면 checkName 함수를 호출
document.forms[0].button.addEventListener('click', checkName, false);

// checkName 함수는 텍스트 입력폼에 텍스트가 입력되면 텍스트를 출력하고
// 숫자가 입력되면 다시 입력을 받는다.
function checkName() {
	// 입력폼에 입력된 값을 name 변수에 넣는다.
	var name = document.forms[0].inputname.value;
	
	// name이 숫자가 아니면 "당신의 이름은 홍길동입니다"와 같이 출력
	// 숫자면 "숫자 말고 이름을 넣으세요!!" 출력과 재입력 받는다.
	
	// 입력 폼은 텍스트를 입력받는다. 만일 "123"과 같이 숫자 형태의 문자열이 입력되었다면
	// NaN인지를 확인하는 isNaN()는 숫자 형태의 문자열을 숫자로 형변환하여 테스트 한다.
	// 만일 숫자로 자동 형변환 하지 않는다면 "123"은 숫자가 아니라 문자열이기에  "당신의 이름은 123입니다." 출력
	// if (name != NaN) 형태로 사용 못함 NaN은 자신과도 같지 않음. isNaN() 함수로 확인해야 함
	if (isNaN(name)) {
		alert("당신의 이름은 " + name + "입니다.");
	} else {
		alert("숫자 말고 이름을 넣으세요!!");
		document.forms[0].inputname.focus();
	}
}


/*
function checkName() {
	var name = document.forms[0].inputname.value;
	// 변수 name을 숫자로 변환하여 변수 tempName에 넣는다.
	var tempName = Number(name);
	
	// 숫자나 문자열은 참조 타입이 아니므로 다음과 같은 비교가 가능하다.
	// name과 숫자로 변환한 tempName이 다른지 비교한다.
	
	// 이 비교문도 자동 형변환으로 가능
	// 문자열 "123"과 숫자 123을 비교할 수 있음.
	// 만일 문자가 입력되었다면 "홍길동"과 
	// Number(name)으로 변환 된 값 NaN과 비교함
	if (name != tempName) {
		alert("당신의 이름은 " + name + "입니다.");
	} else {
		alert("숫자 말고 이름을 넣으세요!!");
		document.forms[0].inputname.focus();
	}
}
*/


/*
function checkName() {
	var name = document.forms[0].inputname.value;
	// 문자열에 0을 곱하면 숫자형 문자열이라면 결과는 0
	// 문자열과 숫자를 곱하면 숫자로 자동 형변환
	var tempName = name * 0;
	
	if (tempName != 0) {
		alert("당신의 이름은 " + name + "입니다.");
	} else {
		alert("숫자 말고 이름을 넣으세요!!");
		document.forms[0].inputname.focus();
	}
}
*/
