var square1 = {
	width: 100,
	height: 200,
	position: {x:10, y:10},
	face: true,
	color: "blue",
	border: true,
	borderColor: "black",
	borderSize: 2,
	area: 		function() {
					return this.width * this.height;
				},
	setPosition:function(x, y) {
					this.position.x = x;
					this.position.y = y;
				},
	setColor:	function(faceColor) {
					if(faceColor) {
						this.face = true;
						this.color = faceColor;
					} else {
						this.face = false;
						delete this.color;
					}
				},
	setBorder:	function(borderColor, borderSize) {
					if(borderColor && borderSize) {
						this.border = true;
						this.borderColor = borderColor;
						this.borderSize = borderSize;
					} else {
						this.border = false;
						delete this.borderColor;
						delete this.borderSize;
					}
				}
}

var square2 = new Object();
square2.width = 100;
square2.height = 200;
square2.position = {};
square2.area = function() {
	return this.width * this.height;
}
square2.setPosition = function(x, y) {
	this.position.x = x;
	this.position.y = y;
}
square2.setColor = function(faceColor) {
	if(faceColor) {
		this.face = true;
		this.color = faceColor;
	} else {
		this.face = false;
		delete this.color;
	}
}
square2.setBorder = function(borderColor, borderSize) {
	if(borderColor && borderSize) {
		this.border = true;
		this.borderColor = borderColor;
		this.borderSize = borderSize;
	} else {
		this.border = false;
		delete this.borderColor;
		delete this.borderSize;
	}
}

square2.setPosition(10, 10);
square2.setColor("blue");
square2.setBorder("black", 2);