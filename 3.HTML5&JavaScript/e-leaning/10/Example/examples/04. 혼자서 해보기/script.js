// 숫자 야구게임 판결함수
// 하나의 배열과 길이가 정해지지 않은 숫자를 전달인자로 받는다.
function numberBall (arr) {
	// 첫 번째 전달인자인 배열의 길이를 loopLength 변수에 할당한다.
	var loopLength = arr.length;
	// 스트라이크와 볼을 저장할 변수 생성 및 초기화
	var strike = 0;
	var ball = 0;
	
	// 배열의 길이만큼 반복
	for (var i=0; i<loopLength; i++) {
		// 두 번째 전달인자 부터 검사 배열의 길이만큼 전달인자 순회
		// 전달인자의 길이가 아니라 배열의 길이인 이유는 
		// 배열의 길이 이상되는 전달인자는 검사할 필요가 없으므로
		for (var arg=1; arg<loopLength; arg++) {
			// 현재 배열 원소와 전달인자의 값을 비교해 같으면
			if (arr[i]==arguments[arg]) {
				// 만인 위치까지 같다면 strike 변수에 1 추가
				if ((i+1)==arg) strike++;
				// 그렇지 않다면 ball 변수에 1추가
				else ball++;
				// 배열 원소와 같은 전달인자를 발견했기 때문에 
				// 더이상 남은 전달인자를 검사할 필요가 없으므로 
				// 내부 for 문을 벗어난다.
				break;
			}
		}
	}
	// 결과 값으로 스트라이크와 볼으로 이루어진 배열을 반환
	return result = [strike, ball];
}

// 함수 테스트
// guard 배열의 값과 numberBall 함수의 전달인자를 비교하면
// 결과로 1 STRIKE / 2 BALL 이 웹 브라우저에 출력되어야 한다.
var guard = [6,2,9,2,3];
var result = numberBall(guard, 3, 2, 4, 5, 7);
document.writeln(result[0] + " STRIKE / " + result[1] + " BALL");