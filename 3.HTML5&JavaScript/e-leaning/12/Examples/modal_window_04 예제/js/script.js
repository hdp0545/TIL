window.onload = modal;

function modal() {
    document.getElementById("modal").style.display = "block";
    document.getElementById("closeButton").onclick = closeButton;
}

function closeButton(event){
    document.getElementById("modal").style.display = "none";
}