package com.rubypaper;

import static org.junit.Assert.assertTrue;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.core.env.Environment;

import com.rubypaper.persistence.BoardDAO;

@SpringBootTest(properties = {"author.name=gugu", "author.age=28", "author.nation=KOREA"}, 
                classes = BoardDAO.class)
class PropertiesTest {
	
	//외부 프로퍼티 추출
//	@Value("${author.name}")
//	private String name;
//	
//	@Value("${author.age}")
//	private int age;
	
	@Autowired
	private Environment env;
	
	@Test
	void testMethod() {
//		assertTrue(true);
		System.out.println("이름 : " + env.getProperty("author.name"));
		System.out.println("나이 : " + env.getProperty("author.age"));
		System.out.println("국가 : " + env.getProperty("author.nation"));
	}

}
