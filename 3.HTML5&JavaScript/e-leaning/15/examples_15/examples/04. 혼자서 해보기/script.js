function Circle(origin, radius) {
	this.originX = origin[0];
	this.originY = origin[1];
	this.radius = radius;
}

Circle.prototype.area = function() {
	return Math.PI * Math.pow(this.radius, 2);
}

Circle.prototype.toString = function() {
	return "[원점이 (" + this.originX + ", " + this.originY + ")이며 반지름이 " + this.radius + "인 원입니다. 넓이는 " + this.area() + "입니다.]";
}

Circle.prototype.valueOf = function() {
	return this.area();
}


// 이 부분 부터가 정답코드 입니다.
// Circle 클래스를 상속 받는 ColorCircle 클래스 입니다.
function ColorCircle(origin, radius, faceColor, borderSize, borderColor) {
	Circle.apply(this, arguments);
	this.faceColor = faceColor || "gray";
	this.borderSize = borderSize || 1;
	this.borderColor = borderColor || "black";
}

ColorCircle.prototype = Object.create(Circle.prototype);

var newCircle = new ColorCircle([10,10], 5);

document.write(newCircle.toString() + "<br>");
document.write("원의 색은 ");
document.write(newCircle.faceColor + "입니다.<br>");
document.write("원의 테두리는 두께가 ");
document.write(newCircle.borderSize + "이고 색이 " + newCircle.borderColor + "입니다.<br>");