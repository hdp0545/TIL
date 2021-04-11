// 성과 이름을 입력 받아 "홍길동님 반갑습니다" 형태로 출력하는 함수
function fullName() {
	// 첫 번째 입력 폼과 두 번째 입력 폼의 값을 변수에 넣는다.
	// 문서에 있는 첫 번째(배열의 0번째) 폼요소의 입력폼 이름으로 입력 값에 접근한다.
	var firstName = document.forms[0].familyName.value;
	var secondName = document.forms[0].name.value;
	
	// 텍스트 값을 더하면 텍스트를 연결합니다.
	var fullname = firstName + secondName + "님 반갑습니다.";
	// 입력 폼 helloMsg 값으로 fullname 변수 값을 출력한다.
	document.forms[0].helloMsg.value = fullname;
}