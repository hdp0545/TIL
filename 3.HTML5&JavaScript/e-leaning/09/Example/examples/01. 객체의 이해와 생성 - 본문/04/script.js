function square( w, h ) {
	this.width = w;
	this.height = h;
	this.faceColor = "yellow";
	this.borderColor = "black";
	this.position = { x: 100, y: 100 };
}

var mysquare = new square( 20, 30 );

for (var p in mysquare) {
	document.writeln(p + "<br>");
}


if ( "depth" in mysquare ) {
	mysquare.depth = 10;
}


if ( mysquare.depth != undefined ) {
	mysquare.depth = 10;
}