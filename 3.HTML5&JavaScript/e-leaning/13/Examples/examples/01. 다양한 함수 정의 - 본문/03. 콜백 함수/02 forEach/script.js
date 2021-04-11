function hiUser(element, index, array) {
    document.write("<p>Hi " + element + "!</p>");
}

var user = ["jerry", "tom", "steve"];
user.forEach(hiUser);