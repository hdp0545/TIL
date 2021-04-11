var numberArray = [1,2,3,4,5,6,7,8,9];
var newArray1 = numberArray.slice(4);
var newArray2 = numberArray.slice(4, 6)
var newArray3 = numberArray.slice(4, -2);

document.writeln("<p>" + newArray1.join(', ') + "</p>");
document.writeln("<p>" + newArray2.join(', ') + "</p>");
document.writeln("<p>" + newArray3.join(', ') + "</p>");