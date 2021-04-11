// 페이지 로딩이 완료된 후 init 함수 콜백
window.addEventListener('load', init, false);

function init() {
	// '추첨하기' 단추가 눌려지면 drawing 함수 콜백
	document.forms[0].button.addEventListener('click', drawing, false);
	
	// 설정된 숫자 볌위 안에서 입력한 갯수의 겹치지 않은 숫자 무작위 추출 함수
	function drawing() {
		// 입력 폼의 값을 변수에 할당
		// startNum과 endNum은 랜덤코드에서 더하기를 하게 됩니다. 
		// 폼으로 입력받은 값이 더하기 할때 문자로 자동변환 될 가능성이 있으므로 Number 객체로 만들어 숫자연산이 되게 합니다.
		var startNum = Number(document.forms[0].start_num.value);
		var endNum = Number(document.forms[0].end_num.value);
		var selectNum = document.forms[0].select_num.value;
		
		// 선택된 숫자들을 넣을 배열을 생성
		var numArray = new Array;
		// 최종 아웃풋 될 HTML 코드를 위한 빈 문자열 생성
		var outputHTML = "";
		// 발생한 난수를 위한 변수
		var randomNum;
		// 생성된 난수가 기존에 생성된 난수와 겹치는지를 표시할 부울 변수, true이면 겹치는것임.
		var overlappingFlag;
		
		// selectNum이 0이 아니면 게속 반복 - 적합한 난수가 발생될 때마다 selectNum을 1씩 줄일것임
		while(selectNum) {
			// 특정 범위 내에서 변수를 구하는 공식 (Math.random() * (최대수  + 1 - 최소수)) + 최소수
			// Math.floor를 이용하여 소수점 이하의 수를 버려 정수만 취함
			// randomNum은 while문이 반복될 때마다 초기화 됨
			randomNum = Math.floor((Math.random() * (endNum + 1 - startNum)) + startNum);
			// 생성된 난수가 기존 생성된 난수와 겹치는지를 표시하는 변수의 초기화 - '안겹친다'로 초기화
			overlappingFlag = false;
			// 생성되어 저장된 난수 중에 지금 생성된 난수와 같은 것이 있는지 검사
			for (var a in numArray) {
				// 만일 같은 것이 있다면
				if (numArray[a] == randomNum) {
					// overlappingFlag를 true로 설정한 후 for 순환문을 벗어난다.
					overlappingFlag = true;
					break;
				}
			}
			// overlappingFlag 가 fasle이면 - 새로 생성된 난수가 기존 생성된 난수와 겹치는 것이 없다면
			if (!overlappingFlag) {
				// 배열 numArray의 마지막에 새로운 난수를 추가
				numArray.push(randomNum);
				// 출력 HTML에도 새로운 난수를 추가한다.
				outputHTML += randomNum + ", ";
				// 겹치지 않은 난수의 설정이 끝났다면 selectNum의 숫자를 하나 줄인다.
				// 만일 overlappingFlag가 true였다면 selectNum은 출어들지 않는다.
				selectNum--;
			}
		}
		// 최종 결과를 출력한다.
		document.getElementById('console').innerHTML = outputHTML
	}
}