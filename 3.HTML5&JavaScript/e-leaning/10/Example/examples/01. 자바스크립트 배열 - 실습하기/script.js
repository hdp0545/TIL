// 배열의 생성과 접근
var testArray = [1, "two", {three:3}, [4, 5], function(){ return "six";}, 3+4, true];

document.writeln("<p>" + testArray[0] + "</p>");
document.writeln("<p>" + testArray[1] + "</p>");
document.writeln("<p>" + testArray[2].three + "</p>");
document.writeln("<p>" + testArray[3][0] + "</p>");
document.writeln("<p>" + testArray[3][1] + "</p>");
document.writeln("<p>" + testArray[4]() + "</p>");
document.writeln("<p>" + testArray[5] + "</p>");
document.writeln("<p>" + testArray[6] + "</p>");


// 원소의 개수가 정해진 배열 생성
// 원소의 개수가 3개인 비어있는 배열 생성
var fixedEmpty = [ , , , ];
// 원소의 개수가 10개인 비어 있는 배열 생성
var myArray = new Array(10);

document.writeln("<p>" + fixedEmpty.length + "</p>");
document.writeln("<p>" + myArray.length + "</p>");

// 다차원 배열의 생성과 접근
var overlapArray = [ 1, 2, 3, [4, 5, 6], 7 ];
document.writeln("<p>" + overlapArray[3][1] + "</p>");

// join 메소드 - 배열 원소 출력
var numberArray = [1,2,3,4,5];
document.writeln(numberArray.toString());
// join 메소드 전달인자가 없을 시
document.writeln("<p>" + numberArray.join() + "</p>");
// join 메소드 전달인자가 있을 시
document.writeln("<p>" + numberArray.join('/ ') + "</p>");

// sort 메소드 - 배열 원소의 정렬
var randomArray = [45,23,5,3,1];
// 문자 정렬
randomArray.sort();

document.writeln("<p>" + randomArray.toString() + "</p>");

// 숫자 정렬
randomArray.sort(function(a, b) {
					return a-b;
				 });

document.writeln("<p>" + randomArray.toString() + "</p>");

// splice 메소드
var numberArray = [1,2,3,4,5,6,7,8,9];
// 4번째 인덱스 부터 3개의 문자를 잘라서 반환하고 'five', ['six', 'seven']를 삽입
var spliceArray = numberArray.splice(4, 3, 'five', ['six', 'seven']);

// 문자를 잘라 반환한 결과
document.writeln("<p>" + spliceArray.join(', ') + "</p>");
// 배열에 'five', ['six', 'seven']를 삽입한 결과
document.writeln("<p>" + numberArray.join(', ') + "</p>");
// slice와 같이 배열을 풀어 삽입하지 않는다.
document.writeln("<p>" + numberArray[5] + "</p>");

// push 메소드
var numberArray = [1,2,3];
var arrayLength = numberArray.push(4,5);

// 배열의 끝에 원소 추가
document.writeln("<p>" + numberArray.join(', ') + "</p>");
// 원소가 추가된 배열의 길이 반환
document.writeln("<p>" + arrayLength + "</p>");