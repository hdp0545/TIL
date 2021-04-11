$(function() {
	// 선택된 과일 카운트 - 과일이 선택되면 count 변수가 1씩 증가합니다.
	var count = 1;
	// 아이디가 'basket'인 요소와 클래스가 'fruit'인 요소를 선택 후 변수에 할당합니다.
	// 한 번 이상 사용되는 셀렉터는 속도 향상을 위해 반드시 변수에 할당하세요.
	var basket = $("#basket");
	var fruits = $(".fruit")
	// 과일을 클릭했을 때 호출되는 이벤트 핸들러 함수
	var clickFruit = function(event) {
		// 선택된 과일의 id 속성 값을 변수에 할당
		var selectedFruit = event.target.getAttribute("id");
		// 선택된 과일 id 속성 값으로 이미지 코드 생성 후 basket에 추가
		basket.append("<img src='images/" + selectedFruit + ".png'>");
		
		// 만일 count가 3인지 검사 후 count 변수 1증가
		if (count++ == 3) {
			// count가 3이면 basket의 보더 색을 빨간색으로 변경
			basket.css("border", "1px solid red");
			// fruits에 바인딩 된 이벤트 핸들러를 언바인딩
			fruits.unbind("click", clickFruit);
		}
		
	};
	
	// fruits에 클릭 이벤트 핸들러 바인딩
	fruits.bind("click", clickFruit);
});