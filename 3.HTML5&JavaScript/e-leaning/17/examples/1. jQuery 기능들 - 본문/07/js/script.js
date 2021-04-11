$(function() {
	$("#policeStation_img").bind("click", function(event) { $("#console").html("<p>첫 번째 이미지를 클릭하였습니다.</p>") });
	
//	$(".illust").bind("click", function(event) { $("#console").html("<p>" + event.target.getAttribute("title") + "를 클릭하였습니다.<p>") });

//	$(".illust").bind("mouseover", function(event) { $("#console").html("<p>" + event.target.getAttribute("alt") + "<p>") }).bind("click", function(event) { $("#console").append("<p>" + event.target.getAttribute("title") + "를 클릭하였습니다.<p>") });

/*
	var handler = function(event) { 
		$("#console").html("<p>" + event.target.getAttribute("title") + "를 클릭하였습니다.<p>") 
	}
	$(".illust").one("click",  handler);
*/
});