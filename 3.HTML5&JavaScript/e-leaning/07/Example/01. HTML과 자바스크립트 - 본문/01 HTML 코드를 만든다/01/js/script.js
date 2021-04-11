function multiplicationSign (x) {
	var htmlOutput = "<p class='multiplicationSign' id='sign" + x + "'>";
	for (var i=1; i < 10; i++) {
		htmlOutput += (x + " x " + i + " = " + i*x + "<br>");
	}
	document.write(htmlOutput + "</p>");
}

multiplicationSign (2);