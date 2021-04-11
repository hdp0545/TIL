window.addEventListener('load', init, false);

function init() {
	document.forms[0].button.addEventListener('click', saleCal, false);
}

function saleCal() {
	var productName = document.forms[0].productname.value;
	var originalPrice = document.forms[0].price.value;
	var discountRate = document.forms[0].discountrate.value;
	var discountPrice
	
	if (discountRate >= 0 && discountRate <= 100) {
		discountPrice = originalPrice - (originalPrice * (discountRate * 0.01));
		console (productName + " 상품의 " + discountRate + "% 할인된 가격은 " + discountPrice + "입니다.");
	} else {
		alert("할인률은 0 ~ 100 사이의 숫자를 입력해야 합니다.")
		document.forms[0].discountrate.value = "";
		document.forms[0].discountrate.focus();
	}
}

function console (outputString) {
	document.getElementById('console').innerHTML = outputString;
}