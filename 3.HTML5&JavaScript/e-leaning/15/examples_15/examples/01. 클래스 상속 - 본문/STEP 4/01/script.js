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

var orc01 = new Orc("venom", "전사", 3);

document.write("새로운 오크족 캐릭터는 ");
document.write(orc01.toString() + "입니다.<br>");

document.write("새로운 오크족 캐릭터의 강력함 수치는 ");
document.write(orc01.valueOf() + "입니다.<br>");
orc01.addArms("곡괭이");
document.write("오크족 캐릭터에 새로운 무기를 추가했습니다. 이제 무기가  ");
document.write(orc01.arms + "입니다.<br>");
document.write("새로운 오크족 캐릭터는 레벨이 ");
document.write(orc01.level + "입니다.<br>");

// 아래 코드는 생성자의 level을 삭제한다.
/* delete orc01.level; */
// 생성자에 level이 없으므로 프로토타입에서 검색한다.
// 프로토타입에도 level이 없으므로 undefined가 반환된다.

document.write("레벨을 삭제한 후 레벨은 ");
document.write(orc01.level + "입니다.<br>");