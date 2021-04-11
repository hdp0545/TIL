// HTML 문서 로딩이 완료되면 init 함수 콜백
window.addEventListener('load', init, false);

function init() {
	// 버튼 클릭하면 multipleCalc 함수 콜백
	document.forms[0].button.addEventListener('click', multipleCalc, false);
}

// multipleCalc 함수
function multipleCalc() {
	// 배수 입력 폼의 값을 변수 multipleNumber에 넣는다.
	var multipleNumber = document.forms[0].multiplenumber.value;
	// 결과를 보여줄 폼을 변수 resultArea가 가리킨다.
	var resultArea = document.forms[0].result;
	// 합계를 저장할 sum 변수를 선언 한 후 0으로 초기화 한다.
	var sum = 0;
	// for 문을 사용하여 1부터 100까지 반복한다.
	for (var i=1; i <= 100; i++) {
		// 반복문의 현재 숫자가 입력된 숫자로 나눠서 나머지가 0인지 평가한다.
		// 평가 결과 0이면 배수이므로 합계에 포함시킨다.
		if (i % multipleNumber == 0) {
			sum += i;
		}
	}
	
	// 1에서 100까지 반복하여 특정 수의 배수 합을 구했다.
	// 웹 브라우저에 출력하기 위해 출력 폼의 value를 지정한다.
	resultArea.value = sum;
}