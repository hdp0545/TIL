function trisum (a, b, c) {
	// 전달인자가 3개인지 검사
	if (arguments.length != 3) {
		throw new Error("trisum 함수는 3개의 전달인자가 필요합니다.");
	}
	// 모든 전달인자의 타입이 숫자 타입인지 검사
	for (var i=0; i < 3; i++) {
		if (typeof arguments[i] != "number") {
			throw new Error("trisum 함수의 전달인자는 모두 숫자여야 합니다.");
		}
	}
	
	// 에러가 발생하지 않았으면 전달인자 3개의 합을 반환
	return a + b + c;
}

var result = trisum (2, 5, 1);
document.writeln(result);


/* var test = {one:1, two:2, three:3}; */
var test = [1,2,3]; 
/* var test = 123; */


function objType(test) {
	if ((test instanceof Array) || (typeof test == "object" && "length" in test)) {
		return "배열";
	} else if(typeof test == "object") {
		return "객체";
	} else {
		return "배열이나 객체 아님";
	}
}

document.writeln("<p>" + objType(test) + "</p>");


function copyArray(arr) {
	if (!((arr instanceof Array) || (typeof arr == "object" && "length" in arr))) {
		throw new Error("copyArray 함수는 전달인자로 배열이 필요합니다.");
	} 
	
	var tempArray = [];
	for(var i in arr) tempArray[i] = arr[i];
	
	for (var a=1; a < arguments.length; a++) {
		tempArray.push(arguments[a]);
	}
	return tempArray;
}

var testArray = [1,2,3];
var a = copyArray(testArray);
var b = copyArray(testArray, 4, 5, 6);

document.writeln("<p>testArray의 값은 " + testArray.toString() + "입니다.</p>");
document.writeln("<p>copyArray(testArray)의 값은 " + a.toString() + "입니다.</p>");
document.writeln("<p>copyArray(testArray, 4, 5, 6)의 값은 " + b.toString() + "입니다.</p>");