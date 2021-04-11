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



/* SubClass - 클래스 상속*/
function Orc(name, title, level) {
	Character.apply(this, arguments);
	this.arms = ['도끼'];
}

Orc.prototype = copyObject(Character.prototype);
Orc.prototype.constructor = Orc;

// 객체를 복사해 반환하는 함수
function copyObject(obj) {
	var TempFunc = function() {};
	TempFunc.prototype = obj;
	return new TempFunc();
}


/* 클래스 상속 결과 확인 */
var orc01 = new Orc("venom", "전사", 3);
document.write("새로운 오크족 캐릭터는 ");
document.write(orc01.toString() + "입니다.<br>");

document.write("새로운 오크족 캐릭터의 강력함 수치는 ");
document.write(orc01.valueOf() + "입니다.<br>");

orc01.addArms("곡괭이");
document.write("오크족 캐릭터에 새로운 무기를 추가했습니다. 이제 무기가  ");
document.write(orc01.arms + "입니다.<br><br>");

document.write("새로운 오크족 캐릭터는 파워는 ");
document.write(orc01.power + "입니다.<br>");

// 생성자 함수에 정의 되었던 프로퍼티가 중복되는 현상이 있는지 검사합니다.
delete orc01.power;
document.write("파워 프로퍼티를 삭제한 후 파워는 ");
document.write(orc01.power + "입니다.<br><br>");

// 프로토타입 객체의 참조 공유 부분의 수정이 제대로 이루어졌는지 확인합니다.
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

document.write("새로운 휴먼족 케릭터의 레벨은 ");
document.write(myChar.level + "입니다.<br>");
myChar.levelup();
document.write("새로운 휴먼족 케릭터의 레벨을 한 단계 올려 ");
document.write(myChar.level + "가 되었습니다.<br><br>");

document.write("오크족 케릭터의 레벨은 ");
document.write(orc01.level + "입니다.<br>");
orc01.levelup();
document.write("오크족의 케릭터의 레벨을 한 단계 올려 ");
document.write(orc01.level + "가 되었습니다.<br><br>");

document.write("오크족의 케릭터의 constructor는 <br>");
document.write(orc01.constructor);