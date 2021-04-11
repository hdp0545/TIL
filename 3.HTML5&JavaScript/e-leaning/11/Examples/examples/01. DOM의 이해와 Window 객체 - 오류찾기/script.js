// 웹 문서 로딩이 완료 된 후 init 함수를 호출한다.
window.addEventListener('load', init, false);

// init 함수
function init () {
	// tag명이 p인 요소를 배열로 변수 p에 할당
	var p = document.getElementsByTagName("p");
	// window.open 메소드로 연 윈도우 객체를 담을 변수 정의
	// 창을 여는 함수와 닫는 함수 두 군데 함수에서 사용해야 하기 때문에
	// 함수 외부에 정의 함
	var w;
	// 각각의 단락에 click 이벤트 할당
	p[0].addEventListener('click', openSub, false);
	p[1].addEventListener('click', closeSub, false);

	function openSub () {
		// 새로운 창을 연다.
		// 창에서 열린 웹 문서는 sub.html이고 창을 구분할 이름은 'sub'이다.
		// 넓이 500픽셀, 높이 350픽셀이고 모든 브라우저 창의 UI 요소를 포함한다.
		// 생성된 window 객체는 변수 w에 할당된다.
		w = window.open("sub.html", "sub", "width=500, height=350, menubar=yes, location=yes, resizable=yes, scrollbars=yes, status=yes");
	}

	function closeSub () {
		// 생성되어 할당된 윈도우 객체를 닫는다.
		w.close();
	}
}