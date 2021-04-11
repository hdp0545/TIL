$(function() {
	// 마우스오버 이벤트에 바인딩 될 이벤트 핸들러 함수
	var mouseOverHandler = function(event) {
		// 아이디가 'console'인 요소에 html을 다음 코드로 재설정합니다.
		// 이벤트가 발생한 요소의 alt 속성 값을 가져와 재설정합니다.
		$("#console").html("<p>" + event.target.getAttribute("alt") + "<p>");
	};
	
	// 클릭 이벤트에 바인딩 될 이벤트 핸들러 함수
	var clickHandler = function(event) { 
		// 아이디가 'console'인 요소에 다음 코드로 덧붙입니다.
		// 이벤트가 발생한 요소의 title 속성 값을 가져와 덧붙입니다.
		$("#console").append("<p>" + event.target.getAttribute("title") + "를 클릭하였습니다.<p>");
	};
	
	// 클래스가 'illust' 인 요소를 선택하여 마우스오버와 클릭 이벤트 핸들러를 바인딩 합니다.
	$(".illust").bind("mouseover", mouseOverHandler).bind("click", clickHandler);
});