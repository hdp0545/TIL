// 객체 리터럴 문법으로 객체 생성
var circle = { 
	position: { x: 100, y: 100}, 
	radius: 10, 
	faceColor: "white", 
	borderColor: "black", 
	area: 	function() { 
				return this.radius * this.radius * Math.PI; 
			}
}

// 생성된 객체에 프로퍼티 추가
circle.borderSize = 1;

// 객체의 프로퍼티 나열 (for/in 문 사용)
document.writeln("<p>객체 circle의 프로퍼티는 다음과 같습니다.</p>");
for (var p in circle) {
	document.writeln(p + "<br>");
}

// 객체의 area 메소드 사용
document.writeln("<p>반지름이 " + circle.radius + "cm<sup>2</sup>인 원의 면적은 " + circle.area() + "cm<sup>2</sup> 입니다.</p>");

// 객체 radius 프로퍼티 값 변경
circle.radius = 15;
// area 메소드로 변경된 값 확인
document.writeln("<p>반지름이 " + circle.radius + "cm<sup>2</sup>인 원의 면적은 " + circle.area() + "cm<sup>2</sup> 입니다.</p>");



// 생성자 함수를 통해 모조 클래스 작성
var Circle = function(r) {
	this.position = { x: 100, y: 100}
	this.radius = r;
	this.faceColor = "white";
	this.borderColor = "black";
	this.borderSize = 1;
}


// new 연산자를 이용하여 myCircle 객체 생성 - 인스턴스화
var myCircle = new Circle(25);

document.writeln("<p>생성자 함수를 이용하여 반지름이 25cm<sup>2</sup>인 myCircle 객체를 생성하였습니다.</p>");

// 프로퍼티 추가 방식으로 메소드 추가
myCircle.area = function(){
	return this.radius * this.radius * Math.PI;
}

// 추가된 메소드 이용
document.writeln("<p>myCircle 객체의 면적은 " + myCircle.area() + "cm<sup>2</sup> 입니다.</p>");

// 메소드 삭제
delete myCircle.area;

// in 연산자를 이용하여 area 메소드가 myCircle 객체에 프로퍼티인지 확인
if (!("area" in myCircle)) {
	document.writeln("myCircle 객체의 area 메소드는 삭제되었습니다.");
}