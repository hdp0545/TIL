 var numberString = [ "one", "two", "three", "four", "five" ]; 
 document.writeln(numberString.length); 


for (var i=0; i < numberString.length; i++) {
	document.writeln("<p>" + numberString[i] + "</p>");
}


var bigArray = new Array(256);

for (var i=0; i < bigArray.length; i++) {
	bigArray[i] = i + 1;
}

document.writeln(bigArray[200]);