// 원 객체를 생성하는 생성자 함수
// 배열인 원점 좌표와 반지름을 전달인자로 받습니다.
function Circle(origin, radius) {
	// x축 원점과 y축 원점 그리고 반지름 프로퍼티를 초기화
	this.originX = origin[0];
	this.originY = origin[1];
	this.radius = radius;
}

// 원의 면적을 구하는 메소드
Circle.prototype.area = function() {
	return Circle.PI * Math.pow(this.radius, 2);
}

// 객체를 문자열로 표현하는 toString 메소드 재작성
Circle.prototype.toString = function() {
	return "[원점이 (" + this.originX + ", " + this.originY + ")이며 반지름이 " + this.radius + "인 원입니다. 넓이는 " + this.area() + "입니다.]";
}

// 객체를 문자열 이외의 데이터값으로 표현하는 valueOf 메소드 재작성
Circle.prototype.valueOf = function() {
	return this.area();
}

// 원주율을 나타내는 클래스 프로퍼티
Circle.PI = 3.14;

// 좌표가 10, 10이고 반지름이 10인 기본 원 객체를 생성하는 클래스 프로퍼티
Circle.DEFAULT = new Circle([10,10], 10);

// 두 개의 원 객체를 받아 둘 사이의 거리를 반환하는 클래스 메소드
Circle.dist = function(a, b) {
	var sideALength = Math.abs(a.originX - b.originX);
	var sideBLength = Math.abs(a.originY - b.originY);
	return Math.sqrt(Math.pow(sideALength, 2) + Math.pow(sideBLength, 2));
}

// 두 개의 원 객체를 받아 둘 중 큰 원 객체를 반환하는 클래스 메소드
Circle.max = function(a, b) {
	if (a.radius > b.radius) {
		return a;
	} else {
		return b;
	}
}

// 두 개의 원 객체를 받아 둘 중 작은 원 객체를 반환하는 클래스 메소드
Circle.min = function(a, b) {
	if (a.radius > b.radius) {
		return b;
	} else {
		return a;
	}
}

// 두 개의 원 객체를 생성, 하나는 기본 객체를 생성하는 클래스 프로퍼티로 생성
var circle001 = Circle.DEFAULT;
var circle002 = new Circle([20,20], 15);

// 생성 된 두 원 객체에 대한 정보 출력
document.write("circle001 원은 " + circle001.toString() + "<br>");
document.write("circle002 원은 " + circle002.toString() + "<br>");

// Circle.max 클래스 메소드를 이용하여 두 원 객체 중 큰 객체의 정보 출력
document.write("두 원 중에 큰 원은 " + Circle.max(circle001, circle002).toString() + "<br>");
// 두 원의 넓이 합을 출력
// circle001 + circle002 + 0 에서 마지막에 0을 더한 이유는 더하기(+)가 문자열 연결이 아닌 숫자 합으로 연산되게 하기 위함입니다.
document.write("두 원의 넓이의 합은 " + (circle001 + circle002 + 0));