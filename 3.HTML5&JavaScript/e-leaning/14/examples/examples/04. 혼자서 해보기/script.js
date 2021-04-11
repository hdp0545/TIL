// 사각형을 생성하는 생성자 함수입니다.
// 중점은 배열로 받습니다.
// 마지막 height 전달인자가 없다면 width 길이의 정사각형입니다.
function Rectangle(origin, width, height) {
	this.originX = origin[0];
	this.originY = origin[1];
	this.width = width;
	if (height) {
		this.height = height;
	} else {
		this.height = width;
	}
}

// 0점이 원점이고 크기가 10인 정사각형 객체를 생성하는 클래스 프로퍼티
Rectangle.SQUARE10 = new Rectangle([0,0], 10);

// 문자열로 변경할 때 직사각형과 정사각형을 구분하여 반환
Rectangle.prototype.toString = function() {
	if (this.width != this.height) {
		return this.width + "x" + this.height + "인 직사각형";
	} else {
		return this.width + "x" + this.height + "인 정사각형";
	}
};

// 크기를 가늠할 수 있는 valueOf 메소드는 사각형의 면적을 반환
Rectangle.prototype.valueOf = function() {
	return this.area();
};

// 면적을 반환하는 메소드
Rectangle.prototype.area = function() {
	return this.width * this.height;
};

var myRect = new Rectangle([10,20], 200, 300);
document.write(myRect.toString());
document.write("의 면적은 " + myRect.area() + "입니다.<br>");

var mySqu = Rectangle.SQUARE10;
document.write(mySqu.toString());
document.write("의 면적은 " + mySqu.area() + "입니다.<br>");