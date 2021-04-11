window.addEventListener("load", init, false);

function init() {
	document.getElementById("button").addEventListener("click", makeFunc, false);
}

function makeFunc() {
	var x = document.getElementsByName("x")[0].value;
	var y = document.getElementsByName("y")[0].value;
	var z = document.getElementsByName("z")[0].value;

	var func = document.getElementsByTagName("textarea")[0].value;
	
	var makedFunc = new Function("x", "y", "z", func);
	var runFunc = makedFunc(x, y, z);
	
	var outputHTML = "<pre>function yourFunction(";
	if (x) {
		var arg = "x";
		var realArg = x;
		if (y) {
			arg += ", y";
			realArg += ", " + y;
			if (z) {
				arg += ", z";
				realArg += ", " +z;
			}
		}
		outputHTML += arg;
	}
	outputHTML += ") {<br>";
	outputHTML += "<div class='funcBody'>" + func + "</div>}<br><br>";
	
	outputHTML += "yourFunction(" + realArg + ") => " + runFunc + "</pre>";
	
	document.getElementById("console").innerHTML = outputHTML;
}