var numberArray = [1,2,3,4,5,6,7,8,9];
var newArray = numberArray.splice(4);

document.writeln("<p>반환되는 값은 " + newArray.toString() + "</p>");
document.writeln("<p>numberArray 배열은 " + numberArray.toString() + "가 됩니다.</p>");


var numberArray = [1,2,3,4,5,6,7,8,9];
var sliceArray = numberArray.slice(4, 7);
var spliceArray = numberArray.splice(4, 3);

document.writeln("<p>" + sliceArray.toString() + "</p>");
document.writeln("<p>" + spliceArray.toString() + "</p>");
document.writeln("<p>" + numberArray.toString() + "</p>");


var numberArray = [1,2,3,4,5,6,7,8,9];
var spliceArray = numberArray.splice(4, 3, 'five', ['six', 'seven']);

document.writeln("<p>" + spliceArray.join(', ') + "</p>");
document.writeln("<p>" + numberArray.join(', ') + "</p>");
document.writeln("<p>" + numberArray[5] + "</p>");