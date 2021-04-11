var testArray = [1, "two", {three:3}, [4, 5], function(){ return "six";}, 3+4, true];

document.writeln("<p>" + testArray[0] + "</p>");
document.writeln("<p>" + testArray[1] + "</p>");
document.writeln("<p>" + testArray[2].three + "</p>");
document.writeln("<p>" + testArray[3][0] + "</p>");
document.writeln("<p>" + testArray[3][1] + "</p>");
document.writeln("<p>" + testArray[4]() + "</p>");
document.writeln("<p>" + testArray[5] + "</p>");
document.writeln("<p>" + testArray[6] + "</p>");

document.writeln("<p>" + testArray[4]() + "</p>");

var callSix = testArray[4];
document.writeln(callSix());
