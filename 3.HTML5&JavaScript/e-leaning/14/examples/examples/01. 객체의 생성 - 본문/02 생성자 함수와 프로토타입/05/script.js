function Circle(origin, radius) {
	this.originX = origin[0];
	this.originY = origin[1];
	this.radius = radius;
}

Circle.prototype.area = function() {
	return Math.PI * Math.pow(this.radius, 2);
}

var myCircle = new Circle([5,15], 10);

document.write(myCircle.area() + "<br>");	// 314.1592653589793

myCircle.area = function() {
	return "myCircle AREA";
}

document.write(myCircle.area());			// myCircle AREA