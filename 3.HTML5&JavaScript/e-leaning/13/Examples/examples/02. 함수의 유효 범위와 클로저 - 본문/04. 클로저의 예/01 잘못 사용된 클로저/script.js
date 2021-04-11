function marker(correctList) {
	var rtnResult = [];
	for (var i=0; i<correctList.length; i++) {
		var questionNum = "문제 " + (i+1) + "의 정답: ";
		rtnResult.push(function() {
				document.write(questionNum + correctList[i] + "<br>");
			}
		);
	}
	return rtnResult;
}

function printCorrectList() {
	var tempFuncList = marker([3,1,3,4,2]);
	for (var i=0; i<tempFuncList.length; i++) {
		tempFuncList[i]();
	}
}

printCorrectList();