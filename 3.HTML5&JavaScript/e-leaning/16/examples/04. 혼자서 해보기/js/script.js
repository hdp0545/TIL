$(function() {
	// 속도 향상을 위해서 제이쿼리 선택자로 선택한 요소 객체를 변수에 할당합니다.
	var button = $('#button');
	// 버튼의 on/off 상태를 나타내는 변수, 초기값은 off입니다.
	var buttonState = 'off';
	
	// 아래 4개의 함수 리터럴은 bind 메소드에서 사용될 이벤트 핸들러 함수 입니다.
	// 마우스가 버튼 위로 올라갔을 때 호출되는 이벤트 핸들러 함수
	var mouseover = function(event) {
		// 마우스 커서 스타일을 손 모양으로 변경합니다.
		document.body.style.cursor = 'pointer';
		// 버튼이 off 일 때와 on 일때의 상태를 구분하여 처리
		if (buttonState == 'off') {
			// 버튼이 off 이면 버튼 이미지 소스 속성을 다음과 같이 변경
			button.attr('src', 'images/off_over.png');
		} else {
			// 버튼이 on 이면 버튼 이미지 소스 속성을 다음과 같이 변경
			button.attr('src', 'images/on_over.png');
		}
	}
	
	// 마우스가 버튼에서 벗어났을 때 호출되는 이벤트 핸들러 함수
	var mouseout = function(event) {
		// 마우스 커서 스타일을 기본 스타일로 되돌린다.
		document.body.style.cursor = 'normal';
		if (buttonState == 'off') {
			button.attr('src', 'images/off_normal.png');
		} else {
			button.attr('src', 'images/on_normal.png');
		}
	}
	
	// 마우스 버튼을 눌렀을 때 호출되는 이벤트 핸들러 함수
	var mousedown = function(event) {
		if (buttonState == 'off') {
			button.attr('src', 'images/off_pressed.png');
		} else {
			button.attr('src', 'images/on_pressed.png');
		}
	}
	
	// 마우스 버튼을 누른 후 떼었을 때 호출되는 이벤트 핸들러 함수
	var mouseup = function(event) {
		if (buttonState == 'off') {
			// 버튼을 on 이미지로 바꿉니다.
			button.attr('src', 'images/on_normal.png');
			// 버튼 상태를 on으로 바꿉니다.
			buttonState = 'on';
		} else {
			// 만일 버튼 상태가 on 이면 버튼 이미지를 off로 바꿉니다.
			button.attr('src', 'images/off_normal.png');
			// 버튼의 상태도 off로 변경합니다.
			buttonState = 'off';
		}
	}
	
	// 버튼에 마우스를 버튼 위로 올라갔을 때, 마우스가 버튼에서 벗어났을 때
	// 버튼을 눌렀을 때, 누른 버튼을 떼었을 때 각각 발생하는 이벤트를 바인딩 합니다.
	button	.bind('mouseover', mouseover)
			.bind('mouseout', mouseout)
			.bind('mousedown', mousedown)
			.bind('mouseup', mouseup);
});