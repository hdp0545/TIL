function add(x, y) {
	return x + y;
}


var sum = add(2, 3);

// var sum = add.apply(null, [2, 3]);

// var sum = add.call(null, 2, 3);

document.write(sum + "<br>");



// 다음 예제는 함수를 어떤 객체의 메소드 처럼 호출하는 방법입니다.
function add2(x, y) {
	return x + y + this.x + this.y;
}

var testObj = {x:10, y:20};

var sum2 = add2.apply(testObj, [2, 4]);
document.write(sum2);	// 36이 출력 됨.