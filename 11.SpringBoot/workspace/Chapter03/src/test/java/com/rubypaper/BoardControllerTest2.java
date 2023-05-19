package com.rubypaper;

import static org.junit.Assert.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import java.util.List;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest.WebEnvironment;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;

import com.rubypaper.domain.BoardVO;

@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT	)
class BoardControllerTest2 {

	@Autowired
	//TestRestTemplate 객체는 웹 브라우저를 모킹한 객체이다.
	private TestRestTemplate restTemplate;
	
//	@Test
	void testHello() throws Exception {
		String result = restTemplate.getForObject("/hello?name=gugu", String.class);
		assertEquals("hello : gugu", result);
	}
	
//	@Test
	void getBoard() throws Exception {
		BoardVO result = restTemplate.getForObject("/getBoard", BoardVO.class);
		assertNotNull(result);
		assertEquals("테스터",result.getWriter());
	}
	
	@Test
	void getBoardList() throws Exception {
		assertEquals(2, restTemplate.getForObject("/getBoardList", List.class).size());
	}
}
	