function copyArray(arr, addEle) {
	var tempArray = [];
	for(var i in arr) tempArray[i] = arr[i];
	
	for (var a=1; a < arguments.length; a++) {
		tempArray[tempArray.length] = arguments[a];
	}
	return tempArray;
}

var testArray = [1,2,3];
var a = copyArray(testArray);
var b = copyArray(testArray, 4, 5, 6);

document.writeln("<p>testArray의 값은 " + testArray.toString() + "입니다.</p>");
document.writeln("<p>copyArray(testArray)의 값은 " + a.toString() + "입니다.</p>");
document.writeln("<p>copyArray(testArray, 4, 5, 6)의 값은 " + b.toString() + "입니다.</p>");


function max() {
	var max = Number.NEGATIVE_INFINITY;
	for (i=0; i < arguments.length; i++) {
		if (arguments[i] > max) max = arguments[i];
	}
	return max;
}

var maxNumber = max(23,11,42,52,34,75,33);
document.writeln(maxNumber);