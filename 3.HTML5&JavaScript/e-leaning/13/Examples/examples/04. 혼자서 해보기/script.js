// HTML 문서 로딩이 완료된 후 init 함수 콜백
window.addEventListener('load', init, false);

function init() {
	// id 가 box인 노드객체 변수 box에 할당
	var box = document.getElementById("box");
	// 상자의 초기 사이즈 지정
	var boxSize = 50;
	// 애니메이션을 위한 함수리터럴, 콜백함수, 클로저
	var biggerBox = function() {
    	box.style.width = boxSize + "px";
    	box.style.height = boxSize + "px";
        if (boxSize <= 200) {
            boxSize += 3;
            setTimeout(biggerBox, 10);
	    };
	};
	
	// 상자 초기 크기 설정
	box.style.width = boxSize + "px";
	box.style.height = boxSize + "px";
	// 상자에 클릭 이벤트 연결
	box.addEventListener('click', biggerBox, false);
}