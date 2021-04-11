window.onload = init;
document.getElementById("html").onclick = toggleSublist;

function init (event) {
	document.getElementById("sublist").style.display = "none";
}

function toggleSublist (event) {
	this.nextSibling.nextSibling.style.display = (this.nextSibling.nextSibling.style.display == "none") ? "block" : "none";
}