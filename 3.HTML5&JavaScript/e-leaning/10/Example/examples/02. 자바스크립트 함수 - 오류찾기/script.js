// 전달인자를 배열로 받아 배열의 원소가 어떤 데이터 타입인지 알아내어 배열로 반환하는 함수
function getElementsTypeArray(arr) {
	// 전달인자는 반드시 배열이어야 함으로 배열인지 검사하여 배열이 아니면 에러를 발생한다.
	if (!((arr instanceof Array) || (typeof arr == "object" && "length" in arr))) {
		throw new Error("getArrayElementsType 함수는 전달인자로 배열이 필요합니다.");
	}
	
	// 배열의 데이터 타입을 저장할 배열 생성
	var typeArray = [];
	
	// for 문에 (var i in arr)를 사용하지 않은 이유는 
	// var testArray = new Array(10); 과 같이 길이가 지정된 빈 배열을
	// (var i in arr)에서 감지를 못하기 때문
	// 0 부터 배열의 길이만큼 반복 실행
	for (var i=0; i < arr.length; i++) {
		// 만일 배열 원소가 null이거나 undefined이며 typeArray에 "없음"을 추가
		if ((arr[i] == null) || (typeof arr[i] == "undefined")) typeArray.push("없음");
		// 만일 원소 데이터 타입이 "number"이면 typeArray에 "숫자" 추가
		else if (typeof arr[i] == "number") typeArray.push("숫자");
		// 만일 원소 데이터 타입이 "string"이면 typeArray에 "문자열" 추가
		else if (typeof arr[i] == "string") typeArray.push("문자열");
		// 만일 원소 데이터 타입이 "function"이면 typeArray에 "함수" 추가
		else if (typeof arr[i] == "function") typeArray.push("함수");
		// 만일 원소가 Array의 인스턴스이거나 원소 데이터 타입이 "object"이며 length 프로퍼티가 있다면
		// typeArray에 "배열" 추가
		else if ((arr[i] instanceof Array) || (typeof arr[i] == "object" && "length" in arr[i])) typeArray.push("배열");
		// 원소 데이터 타입이 "object"이면 typeArray에 "객체" 추가
		// 객체 검사 앞에 배열 검사가 반드시 있어야 한다.
		// 객체 중에서 배열인 객체를 제외한 나머지 객체만이 진짜 객체이다.
		else if (typeof arr[i] == "object") typeArray.push("객체");
		// 위 검사에 모두 해당되지 않는 경우라면 typeArray에 "미상"을 추가한다.
		// 만일을 위한 대책일 뿐 "미상"이 나올 가능성은 거의 없다.
		else typeArray.push("미상");
	}
	
	// 배열의 데이터 타입이 들어 있는 typeArray를 반환한다.
	return typeArray;
}

// 객체 검사를 위해 Date 객체 생성
var today = new Date();

// 다양한 데이터 타입을 가진 배열 생성
var testArray = [1, 2, 'three', null, [1,2,3], today, function(a,b){return a+ b}];
// getElementsTypeArray 함수 실행, testArray 배열의 원소 데이터 타입을 분석 함
var testArrayType = getElementsTypeArray(testArray);

// 배열과 타입 배열을 동시에 웹 브라우저에 출력한다.
for (var i=0; i < testArray.length; i++) {
	document.writeln("<p>" + testArray[i] + ": ");
	document.writeln(testArrayType[i] + "</p>");
}
