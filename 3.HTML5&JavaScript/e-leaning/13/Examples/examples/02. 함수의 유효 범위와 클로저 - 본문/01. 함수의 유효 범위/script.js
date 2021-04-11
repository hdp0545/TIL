function functionA() {
	var innerVar = 100;
	return innerVar;
}

function functionB() {
	return innerVar;
}
var result = functionB();
document.write(result);


/*
var globalVar = 100;

function functionC() {
	return globalVar;
}

var result = functionC();

document.write(result);
*/


/*
function wrapperFunc() {
	var wrapperVar = 100;
	var sum = innerFunc();
	return sum;
	
	function innerFunc() {
		var innerVar = 50;
		return wrapperVar + innerVar;
	}
}

var result = wrapperFunc();

document.write(result);
*/




