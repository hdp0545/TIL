function Circle(origin, radius) {
	this.originX = origin[0];
	this.originY = origin[1];
	this.radius = radius;
}

Circle.prototype.area = function() {
	return Math.PI * Math.pow(this.radius, 2);
}

var myCircle = new Circle([0,0], 10);
var yourCircle = new Circle([10,10], 5);

document.write(myCircle.radius + "<br>");
document.write(yourCircle.radius);