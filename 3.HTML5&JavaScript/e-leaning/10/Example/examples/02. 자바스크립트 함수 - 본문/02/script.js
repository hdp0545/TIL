function copyArray(arr, addEle) {
	var tempArray = [];
	for(var i in arr) tempArray[i] = arr[i];
	if (addEle) tempArray.push(addEle);
	return tempArray;
}


var testArray = [1,2,3];
var a = copyArray(testArray);
var b = copyArray(testArray, 4);

document.writeln("<p>testArray의 값은 " + testArray.toString() + "입니다.</p>");
document.writeln("<p>copyArray(testArray)의 값은 " + a.toString() + "입니다.</p>");
document.writeln("<p>copyArray(testArray, 4)의 값은 " + b.toString() + "입니다.</p>");