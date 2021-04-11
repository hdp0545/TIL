function toCelsius(fahr) {
	var celsius = Math.floor(5 * (fahr - 32) / 9);
	return celsius;
}

document.writeln(toCelsius(100));

var newFun = toCelsius;
document.writeln(newFun(100));