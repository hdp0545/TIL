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


/* Inheritance STEP03 */
/* 생성자를 빌려쓰고 프로토타입을 지정 */

// 위 두 단계를 하나로 합치겠습니다. 

function Orc(name, title, level) {
	Character.apply(this, arguments);
	this.arms = ['도끼'];
}

Orc.prototype = new Character();

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

// 이 방식의 단점은 생성자의 내부 프로퍼티가 두 번 상속된다는 것 입니다.
// 생성자를 빌려 올 때 한 번 그리고 super class의 객체를 프로토타입으로 받을 때 한 번
// 결과적으로 생성자에는 새로운 name, title, level, arms가 있고
// 프로토타입에는 super class의 그것이 들어 있게된다.

// 아래 코드는 생성자의 level을 삭제한다.
delete orc01.level;

// 생성자에 level이 없으므로 프로토타입에서 검색한다.
// 프로토타입에는 super class의 level이 있으므로 1이 출력된다.
document.write("레벨을 삭제한 후 레벨은 ");
document.write(orc01.level + "입니다.<br>");