function add(a, b) {
	return a + b;
}

document.write(add(1,2));
document.write(add.apply(null, [1, 2]));