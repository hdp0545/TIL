// 화시 온도를 섭시 온도로 변환하는 함수
// 일반적인 선언적 함수 정의
function toCelsius(fahr) {
	var celsius = Math.floor(5 * (fahr - 32) / 9);
	return celsius;
}

document.writeln("<p> 화시 100도는 섭시 " + toCelsius(100) + "입니다.</p>");


// 전달인자 중 가장 큰 수를 반환하는 함수
// 전달인자를 정의하지 않았지만 arguments 객체를 이용하여 전달인자를 비교
function max() {
	// max는 전달 인자 중 가장 큰 수를 담을 변수이다.
	// max를 초기화 하지 않으면 메모리상의 임의 수치로 초기화 될 수 있으므로
	// 음의 무한대 값으로 초기화 한다.
	var max = Number.NEGATIVE_INFINITY;
	// 첫 번째 전달인자 부터 전달인자 길이 만큼 반복한다.
	for (i=0; i < arguments.length; i++) {
		// 변수 max와 전달인자를 비교하여 전달인자가 크면 맥스에 전달인자를 할당한다.
		if (arguments[i] > max) max = arguments[i];
	}
	
	// 모든 전달인자의 크기 비교가 끝났으면 가장 큰 수가 들어있는 변수 max를 반환
	return max;
}

var maxNumber = max(23,11,42,52,34,75,33);
document.writeln("<p>23,11,42,52,34,75,33 중 가장 큰 수는 " + maxNumber + "입니다.</p>");


// 배열을 복사하는 함수, 두 번째 전달인지 부터는 복사한 배열에 추가하는 원소 값
function copyArray(arr) {
	// 배열을 복사할 임시 배열 초기화
	var tempArray = [];
	// 첫 번째 전달인자인 배열의 모든 값을 tempArray에 복사
	for(var i in arr) tempArray[i] = arr[i];
	
	// 두 번째 전달인자 부터 마지막 전달인자까지는 tempArray에 추가
	for (var a=1; a < arguments.length; a++) {
		tempArray[tempArray.length] = arguments[a];
	}
	// 복사된 tempArray를 반환
	return tempArray;
}

var testArray = [1,2,3];
var a = copyArray(testArray);
var b = copyArray(testArray, 4, 5, 6);

document.writeln("<p>testArray의 값은 " + testArray.toString() + "입니다.</p>");
document.writeln("<p>copyArray(testArray)의 값은 " + a.toString() + "입니다.</p>");
document.writeln("<p>copyArray(testArray, 4, 5, 6)의 값은 " + b.toString() + "입니다.</p>");