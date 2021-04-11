var st = "이름:홍길동, 나이:30, 직업:의적";
var dataSplit = st.split(",");
for (var i in dataSplit) {
	var valueSplit = dataSplit[i].split(":");
	document.writeln("<p>" + i + "." + valueSplit[0] + " ==> " + valueSplit[1] + "</p>");
}
