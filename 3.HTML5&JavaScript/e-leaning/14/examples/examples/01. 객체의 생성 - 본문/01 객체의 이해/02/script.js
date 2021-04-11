var myApp = {};
myApp.num = 10;
myApp.str = "sample";
myApp.plus = function(a, b) {
	return a + b;
}

document.write(myApp.plus(1,2) + "<br>");

var MYSPACE = {};
MYSPACE.num = new Number(1234.567);
MYSPACE.str = new String("Hello World!");
MYSPACE.sayHi = function(name) {
	return 'Hi ' + name + '!';
};

document.write(MYSPACE.num + "<br>");
document.write(MYSPACE.str + "<br>");
var hi = MYSPACE.sayHi("홍길동");
document.write(hi + "<br>");

var num = new Number(1234.567);
var today = new Date();
document.write(today);