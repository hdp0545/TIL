var num = new Number(1234.567);
var str = new String("Hello World!");
var func = new Function("name", "return 'Hi ' + name + '!';");

/*
document.write(num + "<br>");
document.write(str + "<br>");
var hi = func("홍길동");
document.write(hi);
*/

var num2 = num.toFixed(1);
document.write(num2 + "<br>");

var str2 = str.replace("Hello", "Hi");
document.write(str2 + "<br>");

var funcArgLength = func.length;
document.write(funcArgLength + "<br>");