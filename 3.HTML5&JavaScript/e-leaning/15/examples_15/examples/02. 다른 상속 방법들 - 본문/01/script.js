var myPen = { type:"볼펜", tipSize:0.7, color:"검정" };
myPen.maker = "모나미"
myPen.toString = function() {
	return this.maker + " " +this.type;
}

var subMyPen = copyObject(myPen);
// var subMyPen = Object.create(myPen);

function copyObject(obj) {
	var TempFunc = function() {};
	TempFunc.prototype = obj;
	return new TempFunc();
}


document.write("subMyPen의 촉은 ");
document.write(subMyPen.color + subMyPen.tipSize + "입니다.<br>");
document.write(subMyPen.toString() + "<br>");


subMyPen.name = "153";
subMyPen.toString = function() {
	return this.maker + " " + this.name + " " + this.type;
}

document.write(subMyPen.toString());