testScope1();
testScope2();

function testScope1() {
	var scope = "local_A";
	document.writeln(scope);
}

function testScope2() {
	document.writeln(scope);
}