function PrivateJS() {
	var privateProperty = ['melon', 'orange', 'apple'];
	this.openProperty = 'Open Property';
	this.getPrivate = function() {
		return privateProperty;
	};
}

PrivateJS.prototype.testMethod = function(a) {
	return this.getPrivate() + a;
}

var obj = new PrivateJS();

document.write(obj.getPrivate() + '<br>');
var privateP = obj.getPrivate();
privateP[0] = 'water melon';
document.write(obj.getPrivate() + '<br><br>');



function PrivateJS() {
	var privateProperty = ['melon', 'orange', 'apple'];
	this.openProperty = 'Open Property';
	this.getPrivate = function() {
		var copiedProperty = [];
		for (var i=0; i<privateProperty.length; i++) {
			copiedProperty.push(privateProperty[i]);
		}
		return copiedProperty;
	};
}

PrivateJS.prototype.testMethod = function(a) {
	return this.getPrivate() + a;
}

var obj = new PrivateJS();

document.write(obj.getPrivate() + '<br>');	// melon,orange,apple
var privateP = obj.getPrivate();
privateP[0] = 'water melon';
document.write(obj.getPrivate() + '<br>');	// melon,orange,apple
document.write(privateP + '<br>');			// water melon,orange,apple