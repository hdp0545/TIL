function square( w, h ) {
	this.width = w;
	this.height = h;
	this.faceColor = "yellow";
	this.borderColor = "black";
	this.position = { x: 100, y: 100 };
	this.area = function() { return this.width * this.height; };
}

var mysquare = new square( 20, 30 );

document.writeln(mysquare.faceColor); 


if (mysquare instanceof square) {
	document.writeln("<p>mysquare는 square의 인스턴스 입니다.</p>");
}