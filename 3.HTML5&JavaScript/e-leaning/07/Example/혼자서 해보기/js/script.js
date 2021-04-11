window.addEventListener('load', tempList, false);

function tempList() {
	var listArea = document.getElementsByTagName("pre")[0];
	var outputHTML = "";
	var fahr, celsius;
	var lower = 0;
	var upper = 300;
	var step = 20;
	
	fahr = lower;
	while ( fahr <= upper ) {
		celsius = 5 * (fahr - 32) / 9;
		outputHTML += fahr + "\t\t" + Math.round(celsius) + "<br>";
		fahr = fahr + step;
	}
	listArea.innerHTML = outputHTML;
}