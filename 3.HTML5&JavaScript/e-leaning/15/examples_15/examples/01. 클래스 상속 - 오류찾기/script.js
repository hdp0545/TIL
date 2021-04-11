/* Superclass 정의 시작 */
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
/* Superclass 정의 끝 */

/* Subclass 정의 시작 */
// 나사못 클래스 정의에 Pen 클래스를 상속 받습니다..
// type과 tipSize는 나사못에 맞게 재설정합니다.
function Screw(maker, name, type, tipSize) {
	Pen.apply(this, arguments);
	this.type = type || "접시머리";
	this.tipSize = tipSize || "1.1";
}

// Screw 생성자의 프로토타입으로 Pen의 프로토타입을 복사해 옵니다.
// Screw의 constructor를 Screw로 설정합니다.
Screw.prototype = Object.create(Pen.prototype);
Screw.prototype.constructor = Screw;

// 모든 Screw 객체가 공유하는 프로퍼티 tipSizeArray를 재설정합니다.
// Screw의 toString 메소드를 메이거와 이름 타입 그리고 팁사이즈가 나타나도록 재설정합니다.
Screw.prototype.tipSizeArray = ["0.75", "0.95", "1.1", "1.35", "1.6", "1.9", "2.4"];
Screw.prototype.toString = function() {
	return this.maker + " " + this.name + " " + this.type + " " + this.tipSize + "mm";
}
/* Subclass 정의 끝 */

// Screw 클래스로 새로운 객체를 만듭니다.
var screwNasa = new Screw("제일", "tp135", "둥근머리");
// 생성된 객체를 문자열로 나타낸다.
document.write(screwNasa.toString() + "<br>");

// Screw 인스턴스 객체에 Pen 클래스의 메소드를 적용합니다.
screwNasa.tipSizeUp();
// 메소드 적용 결과를 확인합니다.
document.write(screwNasa.toString());
