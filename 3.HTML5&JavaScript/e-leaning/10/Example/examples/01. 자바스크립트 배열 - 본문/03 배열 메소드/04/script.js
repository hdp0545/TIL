var numberArray = [1,2,3];
var newArray = numberArray.concat(4,5);

document.writeln("<p>" + newArray.join(', ') + "</p>");


var numberArray = [1,2,3];
var newArray = numberArray.concat([4,5], [6,7]);

document.writeln("<p>" + newArray.join(', ') + "</p>");


var numberArray = [1,2,3];
var addArray = [4,5];
var newArray = numberArray.concat(addArray);

document.writeln("<p>" + newArray.join(', ') + "</p>");