var randomArray = [4,2,5,3,1];
randomArray.sort();

document.writeln("<p>" + randomArray.toString() + "</p>");

var randomArray = [45,23,5,3,1];
randomArray.sort();

document.writeln("<p>" + randomArray.toString() + "</p>");

var randomArray = [45,23,5,3,1];
randomArray.sort(function(a, b) {
					return a-b;
				 });

document.writeln("<p>" + randomArray.toString() + "</p>");