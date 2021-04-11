window.addEventListener("load", startScript, false);

function startScript() {
	var toCelsius = new Function("fahr", "return Math.floor(5 * (fahr - 32) / 9);");
	var value = toCelsius(100);
	
	alert("화시 100도씨는 섭시 " + value + "입니다.");
}