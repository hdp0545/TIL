testScope1();

function testScope1() {
	var scope = "local_A";
	document.writeln(scope);
	testScope2();
	
	function testScope2() {
		var scope = "local_B";
		document.writeln(scope);
	}
}