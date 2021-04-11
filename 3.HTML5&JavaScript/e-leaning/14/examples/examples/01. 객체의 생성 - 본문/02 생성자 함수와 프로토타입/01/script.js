var varA = "test01";

var funcA = function() {
	var varA = "test02";
	return this.varA;
}

document.write(funcA());


/*
// 결과로 global이 출력된다.

var testVar = "global";

function testThis() {
	var testVar = "outter local";
	var testVarCheck = function() {
		var testVar = "inner local";
		return this.testVar;
	}
	document.write(testVarCheck());
}

testThis();
*/

/*
// 결과로 property가 출력된다.

var testVar = "global";

function testThis() {
	var testVar = "local";
	var myObj = new Object;
	myObj.testVar = "property";
	myObj.testVarCheck = function() {
		return this.testVar;
	}
	document.write(myObj.testVarCheck());
}

testThis();
*/