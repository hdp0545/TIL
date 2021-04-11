function multiplicationSign (x) {
	var htmlOutput = "<p class='multiplicationSign' id='sign" + x + "'>";
	for (var i=1; i < 10; i++) {
		htmlOutput += (x + " x " + i + " = " + i*x + "<br>");
	}
	document.write(htmlOutput + "</p>");
}

multiplicationSign (2);
multiplicationSign (3);
multiplicationSign (4);
multiplicationSign (5);
multiplicationSign (6);
multiplicationSign (7);
multiplicationSign (8);
multiplicationSign (9);