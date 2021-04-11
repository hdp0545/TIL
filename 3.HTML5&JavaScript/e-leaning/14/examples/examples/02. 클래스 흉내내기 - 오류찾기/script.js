// 게임 케릭터 객체를 생성하는 생성자 함수
// 케릭터 이름, 타이틀(직업), 레벨을 전달 받아 게임 케릭터를 생성합니다.
function Character(name, title, level) {
	// 케릭터 이름 비공개 프로퍼티 - 이름은 변경이 불가능함
	var name = name;
	// 케릭터 타이틀 비공개 프로퍼티 - 타이틀은 변경이 불가능함
	var title = title;
	
	// 레벨을 지정하면 지정한 레벨로 초기화 하고
	// 레벨이 지정되지 않았다면 1로 초기화 합니다.
	if (level) {
		this.level = level;
	} else {
		this.level = 1;
	}
	// 케릭터의 파워 프로퍼티를 초기화 합니다.
	this.power = 10;
	// 케릭터의 경험치 프로퍼티를 초기화 합니다.
	this.experience = 10;
	// 케릭터가 가지고 있는 무기를 초기화 합니다.
	// 무기는 배열로 추가됩니다.
	this.arms = ['검'];
	
	// 비공개 프로퍼티인 name의 값을 반환하는 특권 메소드
	this.getName = function() {
		return name;
	};
	
	// 비공개 프로퍼티인 title의 값을 반환하는 특권 메소드
	this.getTitle = function() {
		return title;
	};
}

// 오크족 일꾼을 만들어 내는 클래스 메소드
// 오크족 일꾼은 기본 무기가 도끼입니다.
Character.orcs = function() {
	var newOrc = new Character('orc', '일꾼');
	newOrc.arms = ['도끼'];
	return newOrc;
}

// 객체를 문자열로 표현하는 toString 메소드 재설정
// 타이틀과 이름을 반환
Character.prototype.toString = function() {
	return this.getTitle() + " " + this.getName();
}

// 객체를 수치로 표현하는 valueOf 메소드 재설정 
// 객체의 수치는 파워와 경험치 그리고 가지고 있는 무기의 갯수에 따라 결정 됩니다.
Character.prototype.valueOf = function() {
	return this.power + this.experience + this.arms.length * 5;
}

// 케릭터 레벨업을 위한 메소드
// 레벨 업 될 숫자를 전달인자로 받아 레벨을 높입니다.
Character.prototype.levelup = function(up) {
	// 전달인자로 높일 레벨을 받았다면 해당 레벨 만큼 높이고
	// 전달인자가 없다면 레벨을 1 높입니다.
	if (up) {
		this.level = this.level + up;
	} else {
		this.level = this.level + 1;
	}
}

// 파워를 증가하기 위한 메소드
Character.prototype.powerup = function(up) {
	this.power = this.power + up;
}

// 경험치를 증가하기 위한 메소드
Character.prototype.expup = function(up) {
	this.experience = this.experience + up;
}

// 케릭터가 수유하는 무기를 추가하는 메소드
Character.prototype.addArms = function(arms){
	// 전달인자로 받은 무기를 arms 프로퍼티 배열에 추가합니다.
	this.arms.push(arms);
}

/* 클래스 작성 완료 */

// 새로운 게임 케릭터를 생성합니다.
// 이름은 biggom이고 전사입니다. 레벨은 지정하지 않았습니다.
var gameChar01 = new Character('biggom', '전사');
var gameChar02 = new Character('loadnice', '기사', 2);

document.write("케릭터는 " + gameChar01.toString() + "입니다.<br>");
document.write(gameChar01.getName() + "의 레벨은 " + gameChar01.level + "이고 소유한 무기는 " + gameChar01.arms + "입니다.<br>")

// 무기를 추가하고 레벨을 2 올립니다.
gameChar01.addArms('활');
gameChar01.levelup(2);

document.write("변경 된 " + gameChar01.getName() + "의 레벨은 " + gameChar01.level + "이고 소유한 무기는 " + gameChar01.arms + "입니다.<br>")

if(gameChar01 > gameChar02) {
	document.write(gameChar01.toString() + "과 " + gameChar02.toString() + " 중 " + gameChar01.toString() + "(이)가 더 강력한 케릭터 입니다.<br>");
} else {
	document.write(gameChar01.toString() + "과 " + gameChar02.toString() + " 중 " + gameChar02.toString() + "(이)가 더 강력한 케릭터 입니다.<br>");
}

var orcman01 = Character.orcs();
var orcman02 = Character.orcs();
orcman01.addArms('곡괭이');
document.write("오크족 일꾼1의 도구는 " + orcman01.arms + "입니다.<br>");
document.write("오크족 일꾼2의 도구는 " + orcman02.arms + "입니다.<br>");
