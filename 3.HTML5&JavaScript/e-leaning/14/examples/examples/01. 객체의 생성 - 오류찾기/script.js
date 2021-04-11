// 게임 케릭터 객체를 생성하는 생성자 함수
// 케릭터 이름, 타이틀(직업), 레벨을 전달 받아 게임 케릭터를 생성합니다.
function Character(name, title, level) {
	// 케릭터 이름 프로퍼티
	this.name = name;
	// 케릭터 타이틀(전사, 기사, 연금술사, 승려...) 프로퍼티
	this.title = title;
	
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
	this.arms = ['sword'];
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

// 케릭터가 수유하는 무기를 추가하는 메소드
Character.prototype.addArms = function(arms){
	// 전달인자로 받은 무기를 arms 프로퍼티 배열에 추가합니다.
	this.arms.push(arms);
}

// 새로운 게임 케릭터를 생성합니다.
// 이름은 biggom이고 전사입니다. 레벨은 지정하지 않았습니다.
var gameChar01 = new Character('biggom', 'warrior');

document.write("케릭터의 이름은 " + gameChar01.name + "입니다.<br>");
document.write(gameChar01.name + "의 레벨은 " + gameChar01.level + "이고 소유한 무기는 " + gameChar01.arms + "입니다.<br>")

// 무기를 추가하고 레벨을 2 올립니다.
gameChar01.addArms('bow');
gameChar01.levelup(2);

document.write("변경 된 " + gameChar01.name + "의 레벨은 " + gameChar01.level + "이고 소유한 무기는 " + gameChar01.arms + "입니다.<br>")
