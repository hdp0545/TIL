var myComputer = { maker: "dell", cpu: "intel core i5", ram: 4, hd: 500, unit: "GB"};

document.write("내 컴퓨터의 램은 " + myComputer.ram + myComputer.unit +"입니다.<br>");

myComputer.ram = 8;
myComputer.bluetooth = true;

myComputer.getRAM = function() {
	return this.ram + this.unit;
}

document.write("내 컴퓨터의 램은 " + myComputer.getRAM() +"입니다.<br>");

/*
var myComputer = { maker: "dell", cpu:"intel core i5", ram: 4, hd: 500, unit: "GB", getRAM: function() { return this.ram + this.unit; } };

document.write("내 컴퓨터의 램은 " + myComputer.getRAM() +"입니다.");
*/