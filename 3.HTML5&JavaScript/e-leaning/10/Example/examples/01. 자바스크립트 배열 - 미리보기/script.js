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
var fixedEmpty = [ , , , ];
var myArray = new Array(10);

document.writeln("<p>" + fixedEmpty.length + "</p>");
document.writeln("<p>" + myArray.length + "</p>");

// 다차원 배열
var overlapArray = [ 1, 2, 3, [4, 5, 6], 7 ];
document.writeln("<p>" + overlapArray[3][1] + "</p>");

// join 메소드 - 배열 원소 출력
var numberArray = [1,2,3,4,5];
document.writeln(numberArray.toString());
document.writeln("<p>" + numberArray.join() + "</p>");
document.writeln("<p>" + numberArray.join('/ ') + "</p>");

// sort 메소드 - 배열 원소의 정렬
var randomArray = [45,23,5,3,1];
randomArray.sort();

document.writeln("<p>" + randomArray.toString() + "</p>");


var randomArray2 = [45,23,5,3,1];
randomArray2.sort(function(a, b) {
					return a-b;
				 });

document.writeln("<p>" + randomArray2.toString() + "</p>");

// splice 메소드
var numberArray = [1,2,3,4,5,6,7,8,9];
var spliceArray = numberArray.splice(4, 3, 'five', ['six', 'seven']);

document.writeln("<p>" + spliceArray.join(', ') + "</p>");
document.writeln("<p>" + numberArray.join(', ') + "</p>");
document.writeln("<p>" + numberArray[5] + "</p>");

// push 메소드
var numberArray = [1,2,3];
var arrayLength = numberArray.push(4,5);

document.writeln("<p>" + numberArray.join(', ') + "</p>");
document.writeln("<p>" + arrayLength + "</p>");