var originalObj = {a:"original", b:1};
document.write("originalObj: ");
document.write(originalObj.a);
document.write(originalObj.b + "<br>");

/*
var duplicatedObj = originalObj;
duplicatedObj.a = "duplicated";
duplicatedObj.b = 2;

document.write("originalObj: ");
document.write(originalObj.a);
document.write(originalObj.b);
*/

/*
var TempFunc = function() {};
TempFunc.prototype = originalObj;
var duplicatedObj = new TempFunc();

duplicatedObj.a = "duplicated";
duplicatedObj.b = 2;

document.write("originalObj: ");
document.write(originalObj.a);
document.write(originalObj.b + "<br>");

document.write("duplicatedObj: ");
document.write(duplicatedObj.a);
document.write(duplicatedObj.b + "<br>");
*/


function copyObject(obj) {
	var TempFunc = function() {};
	TempFunc.prototype = obj;
	return new TempFunc();
}

var duplicatedObj = copyObject(originalObj);

duplicatedObj.a = "duplicated";
duplicatedObj.b = 2;

document.write("originalObj: ");
document.write(originalObj.a);
document.write(originalObj.b + "<br>");

document.write("duplicatedObj: ");
document.write(duplicatedObj.a);
document.write(duplicatedObj.b + "<br>");