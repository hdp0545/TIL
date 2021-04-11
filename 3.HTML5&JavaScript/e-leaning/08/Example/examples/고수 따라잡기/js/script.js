// name 속성이 emailtype인 select 요소의 변화가 있을 때 emailSelect 함수가 콜백된다.
document.forms[0].emailservice.addEventListener('change', emailSelect, false);

// emailSelect 함수
function emailSelect() {
	// 변수 emailType에는 이메일 종류 선택 값이 들어간다.
	var emailService = document.forms[0].emailservice.value;
	// 이메일 도메인 부분 입력폼은 변수 emailDomain이 가리킨다.
	var emailDomain = document.forms[0].emaildomain;
	
	// 변수 emailType의 값에 따라 분기되는 switch 문
	switch(emailService) {
		// 변수 emailType의 값이 "hanmail"이면 emailDomain 입력 폼에 "hanmail.net"이 보이게 한다.
		// 입력폼을 수정하지 못하게 만든다.
		case "hanmail":
			emailDomain.value = "hanmail.net";
			emailDomain.disabled = true;
			break;
		case "naver":
			emailDomain.value = "naver.com";
			emailDomain.disabled = true;
			break;
		// 만일 "직접입력"을 선택했다면 이메일 도메일 입력폼의 내용을 지우고 입력가능한 상태로 만든 후 포커스한다.
		case "user":
			emailDomain.value = "";
			emailDomain.disabled = false;
			emailDomain.focus();
			break;
		// 위 모든 case가 아닌 경우 이메일 도메일 입력폼을 지우고 수정하지 못하게 한다.
		default:
			emailDomain.value = "";
			emailDomain.disabled = true;
	}
}