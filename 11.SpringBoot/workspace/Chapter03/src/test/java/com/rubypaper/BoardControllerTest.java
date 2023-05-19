package com.rubypaper;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;

@WebMvcTest
class BoardControllerTest {

	@Autowired
	private MockMvc mockMvc;
	
	@Test
	void testHello() throws Exception {
//		// HTTP 요청 (http://localhost:8080/hello?name=gugu) 을 전송한다.
//		mockMvc.perform(MockMvcRequestBuilders.get("/hello").param("name", "gugu"))
//		
//		//  가짜 서블릿 컨테이너가 리턴한 HTTP 응답결과를 검증한다.
//		.andExpect(MockMvcResultMatchers.status().isOk())
//		.andExpect(MockMvcResultMatchers.status().is(200))
//		.andExpect(MockMvcResultMatchers.content().string("hello : gugu"));
		

		mockMvc.perform(get("/hello").param("name", "gugu")).andExpect(status().isOk()).andExpect(content().string("hello : gugu"));
	}
}
	