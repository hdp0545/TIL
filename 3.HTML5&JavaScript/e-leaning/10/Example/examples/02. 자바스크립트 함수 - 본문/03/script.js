function copyArray(arr) {
	var tempArray = [];
	for(var i in arr) tempArray[i] = arr[i];
	return tempArray;
}

var firstArray = [1,2,3];
var secondArray = copyArray(firstArray);
secondArray.push(4);
document.writeln(firstArray.toString());