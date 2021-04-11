$(function() {
	$(".album ol li p:last-child").addClass("select1");		// red border
	$(".album ol li p:first").addClass("select2");			// pink background color
	$(".album ol li:nth-child(2) p:first-child").addClass("select3");	// greenyellow background color
	$(".album ol li:lt(3)").addClass("select4");			// blue dotted border
	$(".album ol li:nth-child(3n+1)").addClass("select5");	// lightgray background color
});