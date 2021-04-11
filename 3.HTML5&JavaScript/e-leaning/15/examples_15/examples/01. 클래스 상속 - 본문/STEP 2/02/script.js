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


/* Inheritance STEP02 */
/* 생성자 빌려쓰기 */

// 아래와 같이 apply 메소드로 super class를 실행하면
// 결과적으로 sub class의 생성자로 super class의 생성자를 실행하는 효과를 가져온다.
function Orc(name, title, level) {
	Character.apply(this, arguments);
	// sub class에서 변경되는 프로퍼티는 반드시 apply 뒤에 와야 한다.
	this.arms = ['도끼'];
}

// 이번에는 sub class의 전달인자를 사용할 수 있다.
var orc01 = new Orc("venom", "전사", 3);

document.write("새로운 오크족의 이름은 ");
document.write(orc01.getName() + "입니다.<br>");
document.write("캐릭터 레벨은 " + orc01.level + "입니다.<br>");
document.write("캐릭터의 무기는 " + orc01.arms + "입니다.<br>");
// 이 방식의 단점은 프로토타입의 상속이 안된다는 것 입니다.
// 아래 addArms 메소드의 사용은 에러를 발생합니다.
orc01.addArms("망치");
document.write(orc01.arms);

// 프로토타입에 재설정되었던 toString 메소드도 무시됩니다.
// 아래 toString 메소드는 Object객체의 toString이 출력됩니다.
document.write(orc01.toString());