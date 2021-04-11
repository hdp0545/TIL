var numberArray = [1,2,3];
var arrayLength = numberArray.push(4,5);

document.writeln("<p>" + numberArray.join(', ') + "</p>");
document.writeln("<p>" + arrayLength + "</p>");


var numberArray = [1,2,3];
var removeElement = numberArray.pop();

document.writeln("<p>" + numberArray.join(', ') + "</p>");
document.writeln("<p>" + removeElement + "</p>");


var numberArray = [1,2,3];
var arrayLength = numberArray.unshift('one', 'two');

document.writeln("<p>" + numberArray.join(', ') + "</p>");
document.writeln("<p>" + arrayLength + "</p>");