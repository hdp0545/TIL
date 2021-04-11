/* SuperClass */
function Character(name, title, level) {
	var name = name;
	var title = title;
	
	this.level = level || 1;
	this.power = 10;
	this.experience = 10;
	this.arms = ['검'];
	
	this.getName = function() {
		return name;
	};
	
	this.getTitle = function() {
		return title;
	};
}

Character.prototype.toString = function() {
	return this.getTitle() + " " + this.getName();
}

Character.prototype.valueOf = function() {
	return this.power + this.experience + this.arms.length * 5;
}

Character.prototype.levelup = function(up) {
	if (up) {
		this.level = this.level + up;
	} else {
		this.level = this.level + 1;
	}
}

Character.prototype.powerup = function(up) {
	this.power = this.power + up;
}

Character.prototype.expup = function(up) {
	this.experience = this.experience + up;
}

Character.prototype.addArms = function(arms){
	this.arms.push(arms);
}


/* Inheritance STEP04 */
/* 프로토타입 공유 */

// SuperClass 생성자가 두 번 호출되는 것을 방지하기 위한 방법
function Orc(name, title, level) {
	Character.apply(this, arguments);
	this.arms = ['도끼'];
}

Orc.prototype = Character.prototype;

// 이 방식의 단점은 프로토타입이 객체이므로 superclass와 subclass의 프로토타입이 참조로 연결된다는 것 입니다.
// subclass의 프로토타입을 변경하면 superclass의 프로토토입도 변경됩니다.

// 다음과 같이 subclass의 프로토타입의 메소드를 수정합니다.
document.write("오크족의 레벨업 메소드 기본 수치를 1에서 0.5로 수정합니다.<br>");
Orc.prototype.levelup = function(up) {
	if (up) {
		this.level = this.level + up;
	} else {
		this.level = this.level + 0.5;
	}
}

// superclass의 객체를 생성합니다.
var myChar = new Character("Dr.NO", "연금술사", 2);
// subclass의 객체를 생성합니다.
var orc01 = new Orc("venom", "전사", 3);

document.write("새로운 휴먼족 케릭터는 ");
document.write(myChar.toString() + "입니다.<br>");

document.write("새로운 휴먼족 케릭터의 레벨은 ");
document.write(myChar.level + "입니다.<br>");

// superclass의 레벨업 메소드를 적용하였지만 결과는 오크족 레벨업 변경한 것이 적용되었다.
orc01.levelup();
myChar.levelup();

document.write("오크족 케릭터의 레벨을 한 단계 올려 ");
document.write(orc01.level + "가 되었습니다.<br>");

document.write("새로운 휴먼족 케릭터의 레벨을 한 단계 올려 ");
document.write(myChar.level + "가 되었습니다.<br>");