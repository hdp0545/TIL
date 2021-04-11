$(function() {
	// name 속성이 'gole_add'인 input 요소를 선택하여 클릭 이벤트 핸들러를 적용합니다.
	$('input[name="gole_add"]').bind('click', function(event) {
		// HTML 문서 중에 textarea 요소를 선택하여 변수 textArea에 할당합니다.
		var textArea = $('textarea')
		// textArea에 값이 있으면 다음을 처리합니다.
		if (textArea[0].value) {
			// 아이디 속성 값이 'gole'인 요소 내부에 목록 아이템(<li>)을 추가합니다.
			$('#gole').append('<li>' + textArea[0].value + '</li>');
			// 추가 된 후 textarea를 초기화 합니다.
			textArea[0].value = '';
		}
	});
});