document.getElementById("gold").addEventListener('click', changeGold, true);

function changeGold(event) {
	event.preventDefault();
	this.setAttribute("src", "img/lead.png");
	document.getElementById("console").innerHTML = "금이 납으로 변했습니다.";
	document.getElementById("gold").removeEventListener('click', changeGold, true);
}
