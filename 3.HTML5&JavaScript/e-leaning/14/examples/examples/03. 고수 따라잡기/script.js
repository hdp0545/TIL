// 제품코드를 전달인자로 받아 제품 객체를 만드는 생성자 함수 입니다.
// 전달인자로 받은 제품코드는 비공개 프로퍼티로 외부 코드에서 수정할 수 없습니다.
// 이것은 일단 설정된 제품객체의 제품코드는 수정이 불가능하다는 의미입니다.
function Product(code) {
	// 아래와 같이 전달인자로 받는 그러니까 각각의 Product 객체마다 다른 비공개 프로퍼티는
	// 생성자 함수 내부에 작성하는 것이 옳습니다.
	var code = code;
	// code 비공개 프로퍼티를 읽어오는 특권 메소드
	this.getCode = function() {
		return code;
	};
}

// 프로토타입은 생성자 함수의 프로퍼티 입니다.
// 프로토타입은 값은 객체 입니다.
// 그렇기 때문에 프로토타입에 프로토 타입 값인 객체를 직접 작성해도 됩니다.
// 아래 코드는 프로토타입 프로퍼티에 객체가 할당됩니다.
// prototype은 메소드가 아니고 프로퍼티이므로 함수에 괄호를 감싸
// 먼저 함수가 실행 되어 결과로 객체를 반환되도록 합니다.
// 함수 뒤에 괄호()를 붙이면 함수가 바로 실행됩니다.
// 결국 아래 코드는 메소드 정의 같아 보이지만 프로퍼티 입니다.
Product.prototype = (function() {
	// 아래 지역변수가 비공개 프로퍼티입니다.
	var preCode = "HY35-";
	var tailCode = "LHB"
	// 비공개 프로퍼티를 읽어오는 특권 메소드는 객체로 작성합니다.
	// 특권 메소드가 아닌 일반 프로토타입 메소드도 이런 방식으로 정의 가능합니다.
	return {
		getPreCode: function() {
			return preCode;
		},
		getTailCode: function() {
			return tailCode;
		},
		productCode: function() {
			return this.getPreCode() + this.getCode() + this.getTailCode();
		}
	};
}());

// 만일 프로토타입 메소드인 productCode 메소드를 기존 형식대로 작성한다면 다음과 같이 작성합니다.
// 위에서 작성한 내용과 결국 같고 동일하게 작동합니다.
/*
Product.prototype.productCode = function() {
	return this.getPreCode() + this.getCode() + this.getTailCode();
}
*/

// 새로운 Product 객체를 생성합니다.
var newProduct = new Product("mk123");

//아래 코드로 프로토타입에 작성한 preCode와 tailCode는 비공개 프로퍼티임을 확인할 수 있습니다.

// 비공개 함수이므로 바로 접근할 수 없습니다.
document.write(newProduct.preCode + "<br>");		// undefined

// 비공개 함수이므로 바로 접근할 수 없습니다.
document.write(newProduct.tailCode + "<br>");		// undefined

//프로토타입에 정의한 비공개 프로퍼티는 특권 메소드로 접근 가능합니다.
document.write(newProduct.getPreCode() + "<br>");	// HY35-

// 생성자 함수에 정의한 비공개 프로퍼티는 특권 메소드로 접근 가능합니다.
document.write(newProduct.getCode() + "<br>");		// mk123

// 프로토타입에 정의한 비공개 프로퍼티는 특권 메소드로 접근 가능합니다.
document.write(newProduct.getTailCode() + "<br>");	// LHB

// 프로토타입에 정의한 메소드
document.write("Product Code: " + newProduct.productCode());