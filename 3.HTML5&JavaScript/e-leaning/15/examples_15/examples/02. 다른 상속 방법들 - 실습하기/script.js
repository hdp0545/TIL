// 함수의 전달인자는 두 개 이상 받습니다.
// 첫 번째 전달인자는 프로퍼티를 받을 객체이고 두 번째 이상 부터는 프로퍼티를 빌려올 객체들입니다.
// 함수 정의에는 첫 번째 프로퍼티만 정의해 놓았으나 함수 내부에서 arguments 객체를 이용해 모든 전달인자에 접근합니다.
function mixInProperty(obj) {
	// 함수 내부에서 사용할 지역 변수 설정
	var arg, prop;
	// 첫 번째 for 문은 두 번째 전달인자 부터 받는 객체를 순환합니다.
	for (arg = 1; arg < arguments.length; arg++) {
		// 두 번째 for 문은 객체의 모든 프로퍼티에 접근하기 위해 순환합니다.
		for (prop in arguments[arg]) {
			// 객체의 프로퍼티라면 첫 번째 전달인자에 객체에 넣습니다.
			if (arguments[arg].hasOwnProperty(prop)) {
				obj[prop] = arguments[arg][prop];
			}
		}
	}
}

/*
var firstObj = { a:"I", b:"II" };
var secondObj = { c:"III", d:"IV"};
var childObj = {e:"V"};

mixInProperty(childObj, firstObj, secondObj);

document.write(childObj.a + " ");
document.write(childObj.c + " ");
document.write(childObj.e);
*/

// 이 함수도 두 개 이상의 전달인자를 받습니다.
// 첫 번째 전달인자는 메소드를 받을 클래스고
// 두 번재 이상 부터 메소드를 빌려줄 클래스들입니다.
function mixInMethod(cls) {
	var arg, method;;
	// 첫 번째 for문은 전달된 클래스를 순환합니다.
	for (arg = 0; arg < arguments.length; arg++) {
		// 두 번째 for 문은 클래스의 프로토타입에 있는 프로퍼티들을 순환합니다.
		for (method in arguments[arg].prototype) {
			// 프로퍼티가 메소드가 아니면 다음 라인을 해석하지 않고 for문을 진행시킵니다.
			if (typeof arguments[arg].prototype[method] != "function") continue;
			// 프로퍼티가 메소드이면 첫 번째 전달인자 클래스의 프로토타입에 메소드를 추가합니다.
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