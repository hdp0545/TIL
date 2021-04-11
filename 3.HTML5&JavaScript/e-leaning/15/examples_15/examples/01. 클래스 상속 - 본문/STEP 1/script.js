/* Super Class */
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


/* Inheritance STEP01 */
/* 프로토타입 지정으로 상속 구현하기 */

function Orc() {
	// super class와 다른 프로퍼티를 지정한다.
	this.arms = ['도끼'];
}

// sub class의 프로토타입으로 super class의 객체를 지정
Orc.prototype = new Character("orc", "일꾼");

var orc01 = new Orc();
document.write("새로운 ORC족의 캐릭터의 이름은 ");
document.write(orc01.getName() + "입니다.<br>");

document.write("새로운 ORC족은 ");
document.write(orc01.toString() + "입니다.<br>");

document.write("새로운 ORC족의 강력함 수치는 ");
document.write(orc01.valueOf() + "입니다.<br>");

document.write("새로운 ORC족의 레벨은 ");
document.write(orc01.level + "입니다.<br>");

document.write("새로운 ORC족의 무기는 ");
document.write(orc01.arms + "입니다.<br>");

// 이 방식의 단점은 sub class 객체를 만들 때 전달인자를 지정하지 못한다.
// 다음과 같이 레벨 3의 전사 venom 오크족 객체를 생성하지 못한다.
var orc02 = new Orc("venom", "전사", 3);
document.write("또다른 ORC족은 '전사 venom'이어야 하지만 '")
document.write(orc02.toString() + "'로 출력됩니다.<br>");