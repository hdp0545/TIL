function isBigEnough(element, index, array) {
  return (element >= 10);
}
var passed = [12, 5, 8, 130, 44].every(isBigEnough);
document.write(passed.toString())

// var passed = [12, 54, 18, 130, 44].every(isBigEnough);
