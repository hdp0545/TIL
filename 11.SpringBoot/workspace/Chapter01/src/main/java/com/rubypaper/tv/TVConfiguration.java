package com.rubypaper.tv;

//import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan(basePackages = {"com.rubypaper.tv", "com.test"})
public class TVConfiguration {
	
//	@Bean
//	TV tv() {
////		LGTV tv = new LGTV();
////		tv.setSpeaker(speaker());
//		return new GoogleTV();
//	}
//	
//	@Bean
//	Speaker speaker() {
//		// TODO Auto-generated method stub
//		return new SonySpeaker();
//	}
}
