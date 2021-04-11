function isBigEnough(element, index, array) {
  return (element >= 10);
}
var passed = [2, 5, 8, 1, 4].some(isBigEnough);
document.write(passed);

// passed = [12, 5, 8, 1, 4].some(isBigEnough);