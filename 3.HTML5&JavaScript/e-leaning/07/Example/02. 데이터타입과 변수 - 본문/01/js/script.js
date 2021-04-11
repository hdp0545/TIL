window.addEventListener('load', integerTest, false);

function integerTest() {
	var integerMax = 9007199254740992;
	var integerMin = -integerMax;
	var outputHTML = "";
	
	outputHTML += "9007199254740992 + 1 = " + (integerMax + 1) + "<br>";
	outputHTML += "-9007199254740992 - 1 = " + (integerMin - 1);
	
	console (outputHTML);
}

function console (outputString) {
	document.getElementById('console').innerHTML = outputString;
}