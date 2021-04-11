// 두 배열을 전달인자로 받아 교집합 배열을 반환하는 함수
// 교집합 중 중복되는 원소는 하나로 처리
function getIntersection(a, b) {
	// 함수의 두 전달인자가 모두 배열이기 때문에 배열 검사를 한다.
	// 전달인자가 한 개 이상이기 때문에 arguments 객체를 사용하여 반복 처리하였음
	// arguments.length: 함수에 전달된 전달인자가 몇 개인지 알아낸다.
	for (var arg=0; arg < arguments.length; arg++) {
		if (!((arguments[arg] instanceof Array) || (typeof arguments[arg] == "object" && "length" in arguments[arg]))) {
				throw new Error("getIntersection 함수는 전달인자로 배열이 필요합니다.");
		} 
	}
	// 교집합 결과를 담을 배열 생성
	var intersection = [];
	// 두 배열을 비교하기 위해 다중 for 문을 사용하였다.
	// 첫 번째 배열의 원소들을 하나하나 두 번재 배열의 원소들과 비교한다.
	for (var i in a) {
		for (var j in b) {
			// 만인 현재 비교하고 있는 두 원소가 같다면
			if (a[i] == b[j]) {
				// findElements()함수를 이용해 배열 내 원소 검사.
				// intersection 배열(현재가지의 교집합 결과)에 원소가 있는지 확인하여
				// 원소가 있다면(0이 아닌 숫자가 반환되면) 아래 있는 코드를 실행하지 않고
				// 다음 순환문을 수행한다.
				if (findEmements(a[i], intersection)) continue;
				// intersecion 배열에 원소를 추가한다.
				intersection.push(a[i]);
				// 같은 원소가 발견되었기 때문에 내부의 for문을 더이상 실행할 필요가 없음
				// 내부 for문 탈출
				break;
			}
		}
	}
	// 교집합 결과 배열을 반환한다.
	return intersection;
}

// findElements 함수는 특정 배열에 특정 원소가 존재하는지 확인하는 용도로 사용되는 함수
// 만일 배열에 검색하고자 하는 원소가 들어 있지 않다면 0을 반환
// 배열에 검색하고자 하는 원소가 들어 있으면 몇 번 들어 있는지 숫자를 반환
// 전달인자 ele는 검색하고자 하는 원소 값, arr은 검색되는 배열
// if문에서 반환 값 0은 false의 의미, 0 이상의 숫자는 true의 의미로 사용될 수 있다.
function findEmements(ele, arr) {
	// 두 번째 전달인자 arr은 반드시 배열이여야 함으로 배열 검사를 한다.
	if (!((arr instanceof Array) || (typeof arr == "object" && "length" in arr))) {
			throw new Error("findEmements 함수는 전달인자로 배열이 필요합니다.");
	}
	// 검색 되어진 횟수를 저장하는 변수 선언과 초기화
	var elementsCount = 0;
	// 배열을 순환하면서...
	for(var i in arr) {
		// 전달인자가 배열 원소에 존재하는지 확인
		if (arr[i] == ele) {
			// 존재하면 elementsCount 변수를 증가시킨다.
			elementsCount++;
		}
	}
	// 결과 반환
	return elementsCount;
}

var firstArray = [3,6,2,7,9,11,3,16];
var secondArray = [8,6,4,16,6,1,12,3];
// firstArray와 secondArray의 교칩합을 intersection 변수에 할당
var intersection = getIntersection(firstArray, secondArray);

document.writeln("<p>첫 번째 배열 [" + firstArray + "]</p>");
document.writeln("<p>두 번째 배열 [" + secondArray + "]</p>");
document.writeln("<p>두 배열의 교집합 [" +intersection + "]</p>");