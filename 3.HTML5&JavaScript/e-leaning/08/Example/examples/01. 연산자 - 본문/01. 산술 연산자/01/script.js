var n1 = 123;
var n2 = 456;
var zero = 0;
var s1 = "456";
var s2 = "string";
var result;

result = n1 + n2;
document.writeln(n1 + " + " + n2 + " = " + result + "<br>");
result = n1 + s1;
document.writeln(n1 + " + \"" + s1 + "\" = " + result + "<br>");
result = n1 + s2;
document.writeln(n1 + " + \"" + s2 + "\" = " + result + "<br><br>");


result = n2 - n1;
document.writeln(n2 + " - " + n1 + " = " + result + "<br>");
result = s1 - n1;
document.writeln("\"" + s1 + "\" - " + n1 + " = " + result + "<br>");
result = s2 - n1;
document.writeln("\"" + s2 + "\" - " + n1 + " = " + result + "<br><br>");


result = n1 * n2;
document.writeln(n1 + " * " + n2 + " = " + result + "<br>");
result = n1 * s1;
document.writeln(n1 + " * \"" + s1 + "\" = " + result + "<br>");
result = n1 * s2;
document.writeln(n1 + " * \"" + s2 + "\" = " + result + "<br><br>");


result = n2 / n1;
document.writeln(n2 + " / " + n1 + " = " + result + "<br>");
result = s1 / n1;
document.writeln("\"" + s1 + "\" / " + n1 + " = " + result + "<br>");
result = n2 / zero;
document.writeln(n2 + " / " + zero + " = " + result + "<br>");
result = n2 / s2;
document.writeln(n2 + " / \"" + s2 + "\" = " + result + "<br><br>");



result = n2 % n1;
document.writeln(n2 + " % " + n1 + " = " + result + "<br>");
result = s1 % n1;
document.writeln("\"" + s1 + "\" % " + n1 + " = " + result + "<br>");
result = n2 * s2;
document.writeln(n2 + " % \"" + s2 + "\" = " + result);