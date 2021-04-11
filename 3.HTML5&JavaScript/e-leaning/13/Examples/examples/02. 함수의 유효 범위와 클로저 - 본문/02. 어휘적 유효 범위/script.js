function functionD() {
	return function(s) {
		return "Hi " + s + "!";
	}
}

var temp = functionD();
var result = temp("James");

document.write(result);


/*
function functionD() {
	var point = "!";
	return function(s) {
		return "Hi " + s + point;
	}
}

var temp = functionD();
var result = temp("James");

document.write(result);
*/