function Circle(origin, radius) {
	this.originX = origin[0];
	this.originY = origin[1];
	this.radius = radius;
}

Circle.prototype.area = function() {
	return Circle.PI * Math.pow(this.radius, 2);
}

Circle.prototype.toString = function() {
	return "[원점이 (" + this.originX + ", " + this.originY + ")이며 반지름이 " + this.radius + "인 원입니다. 넓이는 " + this.area() + "입니다.]";
}

Circle.prototype.valueOf = function() {
	return this.area();
}

Circle.PI = 3.14;

Circle.DEFAULT = new Circle([10,10], 10);

Circle.dist = function(a, b) {
	var sideALength = Math.abs(a.originX - b.originX);
	var sideBLength = Math.abs(a.originY - b.originY);
	return Math.sqrt(Math.pow(sideALength, 2) + Math.pow(sideBLength, 2));
}

Circle.max = function(a, b) {
	if (a.radius > b.radius) {
		return a;
	} else {
		return b;
	}
}

Circle.min = function(a, b) {
	if (a.radius > b.radius) {
		return b;
	} else {
		return a;
	}
}



var myCircle = new Circle([0,0], 10);
document.write(myCircle / 2);