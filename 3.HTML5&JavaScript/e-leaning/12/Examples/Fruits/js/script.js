window.addEventListener('load', init, false);

function init (event) {
	document.getElementById("apple").addEventListener('click', bang, false);
	document.getElementById("lemon").addEventListener('click', bang, false);
	document.getElementById("strawberry").addEventListener('click', bang, false);
}

function bang (event) {
	var targetName = event.currentTarget.getAttribute("id");
	if (targetName == 'lemon') event.stopPropagation();
	var eventTime = new Date(event.timeStamp).toLocaleTimeString();

	var outputString = "현재 이벤트가 도착한 객체는 " + targetName + "입니다.\n"
	outputString += targetName + "은 " + event.eventPhase + "번째 이벤트 전파 단계입니다.\n"
	outputString += "이벤트 발생시간은" + eventTime + "입니다.";

	alert(outputString);
}