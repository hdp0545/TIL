window.addEventListener('load', dataTypeAdd, false);

function dataTypeAdd() {
	var testA = "1000" + "1";
	var testB = "1000" - "1";
	var testC = "10" * "20";
	var testD = "20" / "5";
	
	var outputHTML = "\"1000\" + \"1\" = " + testA + "<br>";
	outputHTML += "\"1000\" - \"1\" = " + testB + "<br>";
	outputHTML += "\"10\" * \"20\" = " + testC + "<br>";
	outputHTML += "\"20\" / \"5\" = " + testD;
	
	console (outputHTML);
}

function console (outputString) {
	document.getElementById('console').innerHTML = outputString;
}