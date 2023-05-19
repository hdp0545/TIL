package TVUser;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
//import org.springframework.context.support.GenericXmlApplicationContext;

//import com.rubypaper.tv.LGTV;
//import com.rubypaper.tv.SamsungTV;
import com.rubypaper.tv.TV;
//import com.rubypaper.tv.TVConfiguration;

public class TVUser {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		TV tv	= new SamsungTV();
		
		// 1. Spring 컨테이너를 구동한다.(여기서 컨테이너가 객체들을 생성한다.)(Inversion of control)
		// GenericXmlApplicationContext container = new GenericXmlApplicationContext("context.xml");
//		AnnotationConfigApplicationContext container = new AnnotationConfigApplicationContext(TVConfiguration.class);
		// 아래 코드는 여러개의 설정을 불러올수있다.
		AnnotationConfigApplicationContext container = new AnnotationConfigApplicationContext("com.rubypaper.tv");

		
//		  2. Spring 컨테이너로부터 테스트할 객체를 Lookup 한다.(조건 TV타입의 id가 tv인 Bean 탐색)
		TV tv = (TV) container.getBean("tv");
		
		// 3. lookup한 객체의 메소드 사용
		tv.powerOn();
		tv.volumeUp();
		tv.volumeDown();
		tv.powerOff();
		
		// 4. Spring 컨테이너를 종료한다.
		container.close();
	}

}
