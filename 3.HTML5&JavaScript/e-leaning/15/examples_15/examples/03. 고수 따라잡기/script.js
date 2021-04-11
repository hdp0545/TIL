// 여러객체의 모든 메소드를 전달하기 위한 믹스인 함수 입니다.
function mixInMethod(cls) {
	var arg, method;;
	for (arg = 0; arg < arguments.length; arg++) {
		for (method in arguments[arg].prototype) {
			if (typeof arguments[arg].prototype[method] != "function") continue;
			cls.prototype[method] = arguments[arg].prototype[method];
		}
	}
}


// 여러 클래스에서 공통적으로 사용할만한 믹스인 클래스를 작성합니다.
// 아래 코드는 다양한 클래스에서 공통으로 쓸 수 있는 toString 메소드를 담고 있는 믹스인 클래스입니다.
// 필요한 것은 메소드이므로 어떤 프로퍼티도 없는 생성자 함수를 작성합니다.
function SetToString() {};
// 공유하고자 하는 메소드(toString)를 프로토타입에 작성합니다.
SetToString.prototype.toString = function() {
	// 객체의 모든 프로퍼티를 순환하여 프로퍼티 이름이 'name'이고 값의 종류가 문자열인 값을 반환합니다.
	for(var prop in this) {
		if (!this.hasOwnProperty(prop)) continue;
		if (prop == "name" && ((typeof this[prop]) == "string"))  {
			return this[prop];
		}
	}
	// 만일 문자열인 name 프로퍼티를 발견하지 못하면 Object에서 상속받은 toString을 반환합니다.
	return Object.prototype.toString.call(this);
}


// 결과를 확인해 봅니다.
// 테스트 클래스를 작성합니다.
function Test(arg1, arg2, name) {
	this.arg1 = arg1;
	this.arg2 = arg2;
	this.name = name;
}

// 믹스인 함수를 사용해서 SetToString 클래스의 메소드를 Test 클래스가 빌려옵니다.
mixInMethod(Test, SetToString);

// Test 클래스의 인스턴스 객체를 생성합니다.
var test = new Test("This ", "is ", "TEST class.");

// test객체에 toString 메소드를 적용합니다.
// 믹스인 클래스의 메소드를 사용하여 출력됩니다.
document.write(test.toString());