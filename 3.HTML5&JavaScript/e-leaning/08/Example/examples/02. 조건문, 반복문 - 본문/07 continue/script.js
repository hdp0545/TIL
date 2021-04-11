var total = 0;

oddAdd:
	for(var i = 0; i <= 10; i++) {
		if ((i%2) == 0) {
			continue oddAdd;
		}
		total += i;
	}
document.writeln("1에서 10까지의 홀수의 합은 " + total + "입니다");