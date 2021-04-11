// 생성자 함수는 maker와 name을 필수 전달인자로 받아야 합니다.
// 나머지 프로퍼티는 옵션으로 전달인자로 전달하지 않으면 초기 값이 설정됩니다.
function Pen(maker, name, type, tipSize, color) {
	this.maker = maker;
	this.name = name;
	this.type = type || "볼펜";
	this.tipSize = tipSize || "0.7";
	this.color = color || "검정";
}

// 펜의 굵기 종류를 모아 놓은 프로퍼티 입니다.
// 모든 펜에 동일한 값으로 프로토타입으로 작성합니다.
Pen.prototype.tipSizeArray = ["0.3", "0.5", "0.7", "0.9", "1.0", "2.0"];

// toString 메소드 재설정은 메이커와 펜 이름 그리고 펜의 종류를 반환합니다.
Pen.prototype.toString = function() {
	return this.maker + " " + this.name + " " + this.type;
}

// valueOf 메소드 재설정하여 펜의 굵기를 반환합니다.
Pen.prototype.valueOf = function() {
	return this.tipSize;
}

// 펜의 굵기 값 설정 메소드
Pen.prototype.tipSizeSet = function(tip) {
	// 전달인자 tip이 tipSizeArray에 있는지 확인합니다.
	// indexOf() 메소드의 결과가 -1이면 같은 값이 없음을 의미합니다.
	if(this.tipSizeArray.indexOf(tip) == -1) {
		// 배열에 같은 값이 없으면 배열에 팁 굵기를 추가하고 정렬합니다.
		this.tipSizeArray.push(tip);
		this.tipSizeArray.sort();
		// 그런 후 팁 사이즈를 설정합니다.
		this.tipSize = tip;
	} else {
		// 배열에 있는 사이즈를 설정하면 그냥 팁 사이즈만 변경합니다.
		this.tipSize = tip;
	}
}

// 팁의 굵기를 증가 시키는 메소드
// up 전달인자는 증가시킬 단계입니다. 옵션으로 설졍하지 않으면 1단계 증가를 의미합니다.
Pen.prototype.tipSizeUp = function(up) {
	// 전달인자 up이 없으면 up을 1로 설정
	var up = up || 1;
	// 현재 팁 사이즈를 tipSizeArray에서 검색 후 인덱스를 tipPosition에 할당
	var tipPosition = this.tipSizeArray.indexOf(this.tipSize);
	// tipPosition이 tipSizeArray의 최고 값보다 크면 최고 값의 위치를 
	// 그렇지 않으면 숫자를 하나 증가하여 tipPosition을 재설정합니다.
	tipPosition = (tipPosition + up >= this.tipSizeArray.length) ? (this.tipSizeArray.length - 1) : (tipPosition + up);
	// 팁 사이즈를 tipSizeArray의 tipPosition으로 설정
	this.tipSize = this.tipSizeArray[tipPosition];
}

// 팁의 굵기를 감소 시키는 메소드
Pen.prototype.tipSizeDown = function(down) {
	// 전달인자가 없으면 down을 1로 설정
	var down = down || 1;
	// 현재 팁 사이즈를 tipSizeArray에서 검색 후 인덱스를 tipPosition에 할당
	var tipPosition = this.tipSizeArray.indexOf(this.tipSize);
	// tipPosition이 0보다 작다면 0으로 크다면 tipPosition에서 down을 빼고 tipPosition에 재설정합니다.
	tipPosition = (tipPosition - down < 0) ? 0 : (tipPosition - down);
	// 팁 사이즈를 tipSizeArray의 tipPosition으로 설정
	this.tipSize = this.tipSizeArray[tipPosition];
}


// 송곳 객체를 리터럴 방식으로 생성합니다.
var awl = {tipSize: "6.0", tipSizeArray: ["6.0", "8.0"]};

// 메소드를 가져올 Pen 클래스의 인스턴스 객체를 생성합니다.
var myPen = new Pen("모나미", "153");

// Pen의 메소드인 tipSizeSet를 송곳(awl)객체의 메소드로 적용합니다.
myPen.tipSizeSet.call(awl, "7.0");


document.write("송곳의 팁 크기는 ");
document.write(awl.tipSize + "입니다.<br>");

document.write("송곳 팁 크기 배열은 ");
document.write(awl.tipSizeArray + "입니다.<br>");
