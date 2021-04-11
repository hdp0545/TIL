function mixInProperty(obj) {
	var arg, prop;
	for (arg = 1; arg < arguments.length; arg++) {
		for (prop in arguments[arg]) {
			if (arguments[arg].hasOwnProperty(prop)) {
				obj[prop] = arguments[arg][prop];
			}
		}
	}
}

function mixInMethod(cls) {
	var arg, method;;
	for (arg = 0; arg < arguments.length; arg++) {
		for (method in arguments[arg].prototype) {
			if (typeof arguments[arg].prototype[method] != "function") continue;
			cls.prototype[method] = arguments[arg].prototype[method];
		}
	}
}



function Test1(a, b) {
	this.a = a;
	this.b = b;
}

Test1.prototype.addAB = function() {
	return this.a + " and " + this.b;
}

function Test2(c, d) {
	this.c = c;
	this.d = d;
}

Test2.prototype.addCD = function() {
	return this.c + " and " + this.d;
}

var test1Obj = new Test1("I", "II");
var test2Obj = new Test2("III", "IV");

function ChildClass() { };

mixInMethod(ChildClass, Test1, Test2);

var childObj = new ChildClass();

mixInProperty(childObj, test1Obj, test2Obj);

document.write(childObj.a + " ");
document.write(childObj.b + " ");
document.write(childObj.c + " ");
document.write(childObj.d + "<br>");
document.write(childObj.addAB() + "<br>");
document.write(childObj.addCD());