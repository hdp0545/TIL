var n1 = 123456;
var n2;
var s1 = "123456"
var result;

result = -n1;
document.writeln("양수 123456에 단항 마이너스 연산자 적용: " + result + "<br>");

n2 = result;
result = +n2;
document.writeln("음수 -123456에 단항 플러스 연산자 적용: " + result + "<br>");

result = -n2;
document.writeln("음수 -123456에 단항 마이너스 연산자 적용: " + result + "<br>");
 
result = -s1;
document.writeln("문자열 \"123456\"에 단항 마이너스 연산자 적용: " + result + "<br>");