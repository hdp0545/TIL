var varA = "global";

function testFunc() {
	var varA = "test";
	var varB = "string";
	var makeString = function() { 
		document.write(varA + " " + varB);
	};
	makeString();
}

testFunc();


var varA = "global";

function testFunc() {
	this.varA = "local";
	this.varB = "string";
	this.makeString = function() { 
		document.write(this.varA + " " + this.varB);
	};
}

var myObj = new testFunc();
myObj.makeString();