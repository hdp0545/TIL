document.forms[0].button.addEventListener('click', quizCheck, false);

/*
	퀴즈에 입력된 값들을 체크하여 틀린 답과 맞은 답을 체크합니다.
	오늘 날짜를 생성하고 입력된 이름과 함께 퀴즈 점수를 알려줍니다.
	예) 각시탈님의 2012년 8월 26일 계산 퀴즈 결과는 100점 입니다.
*/

function quizCheck() {
	// 시험 응시자의 이름을 변수 examineeName에 넣습니다.
	var examineeName = document.forms[0].examinee.value;
	// 시험 문제의 정답을 answer 배열에 넣습니다. 간단한 계산 문제이므로 정답을 수식으로 넣어도 됩니다.
	var answer = [5+6, 8-3, 7*6, 15/3, 8+6-3*2/2];
	// 변수 corrent는 정답을 맞춘 갯수를 카운드 합니다.
	var correct = 0;
	// 5개의 문제가 차례로 들어가 변수
	var questionElement;
	// today 변수에 Date 객체를 생성
	var today = new Date;
	// 최종 출력될 HTML 문자열을 위한 변수
	var outputString = "";
	
	// for문을 이용하여 1부터 5(6이하)까지 반복하여 5개의 문제의 정답을 맞췄는지 확인한다.
	for (var i=1; i < 6; i++) {
		// 변수 questionElement에 문제의 정답 입력폼을 차례대로 넣는다.
		// eval 함수는 문자열을 자바스크립트 코드처럼 실행하라는 의미
		questionElement = eval("document.forms[0].question0" + i);
		// 정답 입력폼을 입력 불가능 상태로 변환 (정답 입력 완료 후 수정 불가능하게)
		questionElement.disabled = true;
		// 정답 확인. 정답이면 correct 변수에 1 증가, 오답이면 incorrectMark(오답 입력폼) 함수 실행
		// answer 배열에 1을 뺀 이유는 배열의 인덱스는 0부터 시작하기 때문임
		if (questionElement.value == answer[i-1]) {
			correct += 1;
		} else {
			incorrectMark(questionElement);
		}
	}
	
	// 문제의 답이 오답이었을 경우 실행되는 함수
	// 오답 입력폼을 절달인자로 받아 배경색을 빨간색으로 글씨를 흰색으로 변경한다.
	function incorrectMark(target) {
		target.style.backgroundColor = 'red';
		target.style.color = 'white';
	}
	
	// 출력될 HTML 코드를 생성하기 위한 코드
	// 날짜 객체의 toLocaleDateString() 메소드는 현지화된 날짜를 보여준다.
	// 한 문제 당 20점씩 계산하여 최종 점수를 계산한다.
	outputString += "<p id='result'>" + examineeName + "님의 " + today.toLocaleDateString() + " 계산 퀴즈 결과<br>";
	outputString += "총 " + answer.length + "문제 중 " + (answer.length - correct) +" 문제를 틀렸습니다.</p>"
	outputString += "<p>틀린 답은 빨간색으로 표시 하였습니다.</p>"
	outputString += "<p>최종 점수는 <span id='score'>" + (correct * 20) + "점</span> 입니다.</P>"
	
	// 가려져 있던 아이디가 resultarea인 요소에 outputString을 출력한다.
	document.getElementById('resultarea').innerHTML = outputString;
	document.getElementById('resultarea').style.visibility = 'visible';
}