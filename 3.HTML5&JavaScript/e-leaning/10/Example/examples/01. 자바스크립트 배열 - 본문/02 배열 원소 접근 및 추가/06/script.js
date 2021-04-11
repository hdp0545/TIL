var testArray = [1,2,3,4,5]; 

testArray[-1] = "zero"; 
document.writeln(testArray[-1]); 


for (var a in testArray) {
	document.writeln("<p>" + testArray[a] + "</p>");
}

document.writeln(testArray.toString()); 