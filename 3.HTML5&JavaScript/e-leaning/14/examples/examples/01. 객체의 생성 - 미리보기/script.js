function Circle(origin, radius) {
	this.originX = origin[0];
	this.originY = origin[1];
	this.radius = radius;
}

Circle.prototype.area = function() {
	return Math.PI * Math.pow(this.radius, 2);
}

var myCircle = new Circle([5,15], 10);

document.write("원 myCircle의 면적은"  + myCircle.area() + "입니다.");