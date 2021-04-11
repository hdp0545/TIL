function PrivateJS() {
	var privateProperty = 'Private Property';
	this.openProperty = 'Open Property';
}

var obj = new PrivateJS();
document.write(obj.privateProperty + '<br>');
document.write(obj.openProperty + '<br><br>');




function PrivateJS() {
	var privateProperty = 'Private Property';
	this.openProperty = 'Open Property';
	this.getPrivate = function() {
		return privateProperty;
	};
}

PrivateJS.prototype.testMethod = function(a) {
	return this.getPrivate() + a;
}

var obj = new PrivateJS();
document.write(obj.privateProperty + '<br>');
document.write(obj.openProperty + '<br>');
document.write(obj.getPrivate() + '<br>');
document.write(obj.testMethod(' test'));