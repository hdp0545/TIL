var pattern = new RegExp(/\w{1,}\s(fox|dog)/g);
var str = "The quick brown fox jumps over the lazy dog.";

document.writeln("<p>" + str.replace(pattern, "cat") + "</p>");