window.addEventListener("load", startScript, false);

function startScript() {
	function toCelsius(fahr) {
		return Math.floor(5 * (fahr - 32) / 9);
	}
	
	var tempConvert = toCelsius;
	
	var value = tempConvert(100);
	
	alert("화시 100도씨는 섭시 " + value + "입니다.");
}