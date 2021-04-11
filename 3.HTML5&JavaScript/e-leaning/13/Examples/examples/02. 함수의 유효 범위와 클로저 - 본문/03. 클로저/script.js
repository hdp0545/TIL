function closureFunc(argA) {
	return function(argB) {
		return argA + argB;
	}
}
var temp = closureFunc(100);
document.write(temp(50));


/*
function wrapperFunc() {
	var innerVar = 100;
	var innerFunc = function(n) {
		return n + innerVar;
	}
	
	var result = innerFunc(50);
	document.write(result);
}

wrapperFunc();
*/


/*
var globalVar;

function wrapperFunc() {
	var innerVar = 100;
	globalVar = function(n) {
		return n + innerVar;
	}
}

wrapperFunc();

var result = globalVar(50);
document.write(result);
*/