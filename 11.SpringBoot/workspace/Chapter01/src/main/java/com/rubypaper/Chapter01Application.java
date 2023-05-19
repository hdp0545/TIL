package com.rubypaper;

import org.apache.catalina.LifecycleException;
import org.apache.catalina.startup.Tomcat;
import org.springframework.boot.Banner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.SpringBootConfiguration;
import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.AutoConfigurationExcludeFilter;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.TypeExcludeFilter;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.FilterType;
import org.springframework.context.annotation.ComponentScan.Filter;
import org.springframework.context.annotation.Configuration;

//@SpringBootApplication
@Configuration
@EnableAutoConfiguration
@ComponentScan(excludeFilters = { @Filter(type = FilterType.CUSTOM, classes = TypeExcludeFilter.class),
		@Filter(type = FilterType.CUSTOM, classes = AutoConfigurationExcludeFilter.class) },
		basePackages =  {"com.rubypaper", "com.ruby"})
public class Chapter01Application {

	public static void main(String[] args) throws LifecycleException {
//		SpringApplication.run(Chapter01Application.class, args);
		SpringApplication application = new SpringApplication(Chapter01Application.class);
		// 어플리케이션을 웹 어플리케이션으로 설정함
		application.setWebApplicationType(WebApplicationType.SERVLET); // web 어플리케이션 타입 설정
		// 콘솔에 배너를 출력하지 않게 설정함
		application.setBannerMode(Banner.Mode.OFF);
		application.run(args);
		
		Tomcat server = new Tomcat();
		server.start();
		
	}

}
