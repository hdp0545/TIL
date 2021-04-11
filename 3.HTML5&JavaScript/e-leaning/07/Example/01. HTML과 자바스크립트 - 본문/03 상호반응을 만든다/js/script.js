window.addEventListener('load', subMenu, false);

var menuState = {};

function subMenu() {
	menuState.menuItem = document.getElementsByClassName('menu');
	menuState.flag = false;	
	hideAllSubMenu();
	for(var i = 0; i < menuState.menuItem.length; i++) {
		menuState.menuItem[i].addEventListener('click', showSubMenu, false);
	}
}

function showSubMenu(event) {
	event.preventDefault();
	hideAllSubMenu();
	if (!menuState.flag & !(menuState.currentMenu == event.currentTarget)) {
		var targetSubMenu = event.currentTarget.childNodes[2];
		if (targetSubMenu) {
			targetSubMenu.style.display = "block";
			menuState.menuState = true;
			menuState.currentMenu = event.currentTarget;
		}
	} else {
		menuState.menuState.flag = false;
		menuState.currentMenu = undefined;
	}
}

function hideAllSubMenu() {	
	for(var i = 0; i < menuState.menuItem.length; i++) {
		if (menuState.menuItem[i].childNodes[2]) {
			menuState.menuItem[i].childNodes[2].style.display = "none";
		}
	}
}