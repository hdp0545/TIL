function isBigEnough(element, index, array) {
  return (element >= 10);
}
var filtered = [12, 5, 8, 130, 44].filter(isBigEnough);

document.write(filtered.toString());