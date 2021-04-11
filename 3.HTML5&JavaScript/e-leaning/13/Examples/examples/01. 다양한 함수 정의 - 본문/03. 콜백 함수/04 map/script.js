function sayBabyAnimal(animal) {
	var result;
  	switch (animal) {
  		case "개": 
  			result = "강아지";
  			break;
  		case "닭":
  			result = "병아리";
  			break;
  		default:
  			result = "새끼 " + animal;
  }
  return result; 
}

var animals = ["고양이", "개", "다람쥐", "닭", "여우"];
var baby = animals.map(sayBabyAnimal);
document.write(baby.toString());