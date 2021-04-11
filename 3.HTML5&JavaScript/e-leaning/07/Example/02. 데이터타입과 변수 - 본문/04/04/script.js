var scope = "global";
testScope1();
testScope2();

function testScope1() {
	document.writeln(scope);
}

function testScope2() {
	document.writeln(scope);
}
