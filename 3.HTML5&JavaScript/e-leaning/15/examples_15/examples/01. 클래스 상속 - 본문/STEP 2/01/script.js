/*
var pet = "햄스터";
var fruit = "귤"

function ownFavor(a, b) {
	var ownPet = a + "마리의 " + this.pet;
	var ownFruit = b + "개의 " + this.fruit;
	var totalFavor = "나는 " + ownPet + "와 " + ownFruit + "를 가지고 있습니다.<br>";
	return totalFavor;
}

document.write(ownFavor(4, 20));
*/

var pet = "햄스터";
var fruit = "귤"

function Favor(pet, fruit) {
	this.pet = pet;
	this.fruit = fruit;
}


function ownFavor(a, b) {
	var ownPet = a + "마리의 " + this.pet;
	var ownFruit = b + "개의 " + this.fruit;
	var totalFavor = "나는 " + ownPet + "와 " + ownFruit + "를 가지고 있습니다.<br>";
	return totalFavor;
}

var favorObj1 = new Favor("개","사과");
var favorObj2 = new Favor("고양이","딸기");

var myFavor1 = ownFavor.apply(null, [4, 20]);
var myFavor2 = ownFavor.apply(favorObj1, [2, 3]);
var myFavor3 = ownFavor.apply(favorObj2, [3, 10]);


document.write(myFavor1);
document.write(myFavor2);
document.write(myFavor3);


/*
// 다음 코드는 call 메소드 버전입니다.
var pet = "햄스터";
var fruit = "귤"

function Favor(pet, fruit) {
	this.pet = pet;
	this.fruit = fruit;
}


function ownFavor(a, b) {
	var ownPet = a + "마리의 " + this.pet;
	var ownFruit = b + "개의 " + this.fruit;
	var totalFavor = "나는 " + ownPet + "와 " + ownFruit + "를 가지고 있습니다.<br>";
	return totalFavor;
}

var favorObj1 = new Favor("개","사과");
var favorObj2 = new Favor("고양이","딸기");

var myFavor1 = ownFavor.call(null, 4, 20);
var myFavor2 = ownFavor.call(favorObj1, 2, 3);
var myFavor3 = ownFavor.call(favorObj2, 3, 10);


document.write(myFavor1);
document.write(myFavor2);
document.write(myFavor3);
*/