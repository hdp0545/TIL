var stringObject = new String("JavaScript was originally developed in Netscape, by Brendan Eich.");
document.writeln("<p>" + stringObject.indexOf("Netscape") + "</p>");

var stringObject = new String("the quick brown fox jumps over the lazy dog");
document.writeln("<p>" + stringObject.indexOf("the") + "</p>");
document.writeln("<p>" + stringObject.lastIndexOf("the") + "</p>");
document.writeln("<p>" + stringObject.substr(4, 5) + "</p>");
document.writeln("<p>" + stringObject.slice(4, 10) + "</p>");