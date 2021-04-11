function add(x, y) {
	if (typeof y == "undefined") {
		return function(y) {return x + y;};
	}
	return x + y;
}

var xVar = 2;
var newAdd = add.call(null, xVar);
var yVar = 3
var result = newAdd.call(null, yVar);
document.write(result);