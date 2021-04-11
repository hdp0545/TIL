// 자바스크립트가 시작되면 함수 countClick()을 실행한다.
countClick();

// 딸기, 사과, 포도를 클릭할 때마다 클릭 숫자를 업데이트하는 함수
function countClick() {
	// 변수 anchorElements는 문서 내의 모든 a요소의 배열이다.
	var anchorElements = document.getElementsByTagName("a");
	// fruits라는 객체를 생성한다.
	var fruits = new Object;
	// 변수 flash에 fruits 객체의 참조를 할당
	var flash = fruits;
	
	// 객체 fruits의 strawberry, apple, grape 프로퍼티 초기화
	fruits.strawberry = 0;
	fruits.apple = 0;
	fruits.grape = 0;
	
	// 딸기, 사과, 포도에 클릭 이벤트 등록 클릭이 일어나면 clickCheck 함수 호출
	for( var i = 0; i < anchorElements.length; i++){
		anchorElements[i].addEventListener("click", clickCheck, false);
	}
	
	// 클릭 했을 때 호출되는 함수, addEventListener가 호출하면 event객체를 전달인자로 받는다.
	function clickCheck(event) {
		// 이벤트가 일어난 객체를 clickFruit 변수에 할당
		var clickFruit = event.target;
		// flash 변수 재선언, 이제 부모 함수의 flash 변수와 이 함수에서의 flash 변수는 다름
		var flash;
		// switch 문을 이용하여 클릭된 과일마다 카운드 증가하기
		switch(clickFruit.getAttribute("title")) {
			case "strawberry":
				// fruits객체의 strawberry 프로퍼티의 값을 1증가한다.
				fruits.strawberry++;
				// 출력을 위해 updateString() 함수를 실행
				updateString();
				break;
			case "apple":
				fruits.apple++;
				updateString();
				break;
			case "grape":
				fruits.grape++;
				updateString();
				break;
		}	
	}
	
	function updateString() {
		// flash.strawberry는 이 함수에서 fruits.strawberry와 같다. - 객체는 참조타입이므로
		// clickFruit 함수에서는 flash.strawberry와 fruits.strawberry는 다르다.
		var outputHTML = "딸기 " + flash.strawberry + "클릭, 사과 " + fruits.apple + "번 클릭, 포도 " + flash.grape + "번 클릭";
		// 두번째 p요소 내부에 outputHTML 변수 값 출력
		document.getElementsByTagName("p")[1].innerHTML = outputHTML;
	}
}

