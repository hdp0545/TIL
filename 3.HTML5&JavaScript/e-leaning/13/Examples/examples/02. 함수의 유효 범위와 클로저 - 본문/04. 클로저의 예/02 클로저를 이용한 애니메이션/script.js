var moveRight = function (node) {
    var positionX = 20;
    var positionY = 20;
    node.style.left = positionX + "px";
    node.style.top = positionY + "px";
    
    var movingX = function (  ) {
    	 node.style.left = positionX + "px";
        if (positionX <= 300) {
            positionX += 1;
            setTimeout(movingX, 10);
        }
    };
    setTimeout(movingX, 100);
};

var node = document.getElementsByTagName("h3")[0];
moveRight(node);

