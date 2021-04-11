var n = 1234.5678;
var result;
result = n.toString()
document.writeln("<p>n = " + result + "</p>");
document.writeln("<p>변수 n의 데이터 타입은 " + typeof n + "입니다.</p>");
document.writeln("<p>n.toString()의 데이터 타입은 " + typeof result + "입니다.</p>");

result = n.toFixed(2);
document.writeln("<p>n.toFixed(2)의 결과는 " + result + "</p>");

result = n.toExponential(3);
document.writeln("<p>n.toExponential(3)의 결과는 " + result + "</p>");

result = n.toPrecision(5);
document.writeln("<p>n.toPrecision(5)의 결과는" + result + "</p>");

var stringObject = new String("the quick brown fox jumps over the lazy dog");
document.writeln("<p>" + stringObject + "</p>");

result = stringObject.indexOf("the");
document.writeln("<p>위 문장에서 첫 번째 the의 시작위치는 " + result + "</p>");

result = stringObject.lastIndexOf("the");
document.writeln("<p>위 문장에서 마지막 the의 시작위치는 " + result + "</p>");

result = stringObject.substr(4, 5);
document.writeln("<p>위 문장에서 5번째 부터 5개의 문자는 " + result + "</p>");