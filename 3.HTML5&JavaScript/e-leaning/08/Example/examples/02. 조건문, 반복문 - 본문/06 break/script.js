var fruits = ["apple", "orange", "melon", "cherry", "melon"];

findElement ("melon", fruits);

function findElement (target, arr) {
	for (var n in arr) {
		if (arr[n] == target) {
			document.writeln((Number(n)+1) + "번째에서 발견되었습니다");
			break;
		}
	}
}