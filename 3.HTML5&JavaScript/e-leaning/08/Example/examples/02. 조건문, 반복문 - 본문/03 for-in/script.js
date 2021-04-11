/*
var fruits = ["apple", "orange", "melon", "cherry"];

for (var n in fruits) {
	document.writeln(fruits[n] + "는 맛있는 과일입니다.<br>");
}
*/

var fruits = { green:"apple", orange:"orange", yellow:"melon", red:"cherry"};

for (var prop in fruits) {
	document.writeln(fruits[prop] + "는 맛있는 과일입니다.<br>");
}