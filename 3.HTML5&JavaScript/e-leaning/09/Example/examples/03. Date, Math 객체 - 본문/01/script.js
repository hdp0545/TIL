var today = new Date();
document.writeln("<p>" + today + "</p>");

var someday = new Date(2010,9,23,06,30,0,0);
document.writeln("<p>" + someday + "</p>");

var someday2 = new Date(1348918854110);
document.writeln("<p>" + someday2 + "</p>");

var today2 = Date.now();
document.writeln(today2);