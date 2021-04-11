// 페이지 로딩이 끝나면 init 함수를 콜백
window.addEventListener('load', init, false);

function init() {
	// Date 객체 today를 오늘 날짜로 생성
	var today = new Date();
	// 
	var countDayOutput = document.forms[0].today_count;
	var memorialCountOutput = document.forms[0].memorial_count;
	var memorialDayOutput = document.forms[0].memorial_date;
	// 사용자가 입력한 아기 생일과 생일이 셋팅되었는지에 대한 정보를 저장할 객체 생성
	var birth = new Object;
	
	// 오늘 날짜를 id가 today인 단락에 출력
	// toLocaleDateString() 메소드를 사용하여 지역 날짜 포맷으로 날짜를 출력 
	// 요일은 toWeekDay() 함수를 이용하여 문자열로 반환
	document.getElementById('today').innerHTML = "오늘은 " + today.toLocaleDateString() + " " + toWeekDay(today.getDay()) + " 입니다.";
	
	// name이 count_btn인 단추를 클릭하면 todayCounter 함수 콜백
	document.forms[0].count_btn.addEventListener('click', todayCounter, false);
	// name이 memorial_btn인 단추를 클릭하면 dayCounter 함수 콜백
	document.forms[0].memorial_btn.addEventListener('click', dayCounter, false);
	
	// 오늘이 아기 출생일로 부터 몇일 째인가를 구하는 함수
	function todayCounter() {
		// 사용자가 입력한 아기 생일 폼의 값으로 아기 생일 날짜 객체 생성하는 함수 호출
		setupBirthday();
		// 오늘날짜에 생일 날짜를 뺀다. 날짜의 연산은 밀리초로 결과나 반환된다.
		var days = today - birth.date;
		// 밀리초로 반환된 값을 날짜로 변환하여 출력
		// 값 올림 메소드인 ceil을 적용한 이유는 결과가 12.34 이며 12일과 그 다음날을 살고 있는 것이므로 소수점 이하자리는 올린다..
		countDayOutput.value = Math.ceil(days/1000/60/60/24);
	}
	
	function dayCounter() {
		// 사용자가 입력한 기념일 날짜를 가져온다. 예) 100일
		var memorialDay = document.forms[0].memorial_day.value;
		// 만일 생일 날짜 객체가 생성되지 않았다면 사용자의 입력 내용으로 생일 날짜 객체를 생성한다.
		if (!birth.setted) setupBirthday();
		
		// 계산된 결과 값을 넣을 날짜 객체 생성
		var targetDay = new Date();
		
		// 사용자 입력으로 생성된 생일 날짜 객체를 가리키는 birth.date에 getDate() 메소드로 생일 날짜 받아온다.
		var birthDay = birth.date.getDate();
		// birth.date 날짜를 targetDay에 복사하는 코드 - 알아두면 편함!!
		targetDay.setTime(birth.date.getTime());
		// 생일 날에 기념일 날짜를 더한다. 날짜 연산의 결과는 밀리초로 반환된다.
		// 결과에 1을 뺀 이유는 결과는 생일 다음날 부터 카운트 하여 기념일이 계산되었기 때문
		// 예를 들어 100일 계산이라면 태어난 날부터 세어야 함.
		// 밀리초로 계산된 날짜를 날짜 객체의 날짜로 갱신하면 원하는 기념일이 된다.
		targetDay.setDate(birthDay + Number(memorialDay) - 1);

		memorialCountOutput.value = memorialDay;
		// 날짜 객체에 toLocaleDateString()을 적용하면 지역포맷 날짜 문자열로 반환된다.
		memorialDayOutput.value = targetDay.toLocaleDateString() + " " + toWeekDay(targetDay.getDay());
	}
	
	// 사용자가 입력한 폼의 값을 가지고 아기 생일을 날짜 객체를 생성하여 birth 객체 프로퍼티로 설정한다.
	function setupBirthday() {
		// 사용자가 입력한 폼의 값을 변수에 지정
		var year = document.forms[0].baby_birth_year.value;
		var month = document.forms[0].baby_birth_month.value;
		var day = document.forms[0].baby_birth_day.value;
		// date 프로퍼티에 날짜 객체를 생성하여 넣는다.
		birth.date = new Date(year, month, day);
		// 생일 날짜 객체가 생성되었는지를 표시하는 부울 프로퍼티
		birth.setted = true;
	}
	
	// 날짜 객체의 요일 숫자 코드를 받아서 한글로 반환하는 함수
	function toWeekDay(dayNumber) {
		switch (dayNumber) {
			case 0:
				return "일요일";
			case 1:
				return "월요일";
			case 2:
				return "화요일";
			case 3:
				return "수요일";
			case 4:
				return "목요일";
			case 5:
				return "금요일";
			case 6:
				return "토요일";
		}
	}
}