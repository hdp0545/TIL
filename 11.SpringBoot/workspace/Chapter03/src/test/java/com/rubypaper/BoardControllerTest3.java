package com.rubypaper;

import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import java.util.HashMap;
import java.util.Map;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest.WebEnvironment;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;

import com.rubypaper.service.BoardService;

@SpringBootTest(webEnvironment = WebEnvironment.MOCK) // Tomcat 을 구동하지 않는다.
@AutoConfigureMockMvc
class BoardControllerTest3 {

	@Autowired
	private MockMvc mockMvc; //목킹된 객체를 목업한다.
	
	@MockBean
	private BoardService boardService;
	
	@Test
	void testHello() throws Exception {
		// 모킹된 비즈니스 객체의 메소드를 호출했을 때, 리턴될 결과값을 설정한다.
		when(boardService.hello("gugu")).thenReturn("hello : gugu");

		
		// HTTP 요청 (http://localhost:8080/hello?name=gugu) 을 전송한다.
		mockMvc.perform(MockMvcRequestBuilders.get("/hello").param("name", "gugu"))
		
		//  가짜 서블릿 컨테이너가 리턴한 HTTP 응답결과를 검증한다.
		.andExpect(MockMvcResultMatchers.status().isOk())
	    .andExpect(MockMvcResultMatchers.status().is(200))
		.andExpect(MockMvcResultMatchers.content().string("hello : gugu"));
//		mockMvc.perform(get("/hello").param("name", "gugu")).andExpect(status().isOk()).andExpect(content().string("hello : gugu"));
	}
	
	@Test
	void testGetBoard() throws Exception {
		// 모킹된 비즈니스 객체의 메소드를 호출했을 때, 리턴될 결과값을 설정한다.
		Map<String, Object> board = new HashMap<String, Object>();
		board.put("SEQ", 1);
		board.put("WRITER", "gugu");
		when(boardService.getBoard(1)).thenReturn(board);

		
		// HTTP 요청 (http://localhost:8080/hello?name=gugu) 을 전송한다.
		mockMvc.perform(MockMvcRequestBuilders.get("/getBoard").param("seq", "1"))
		
		//  가짜 서블릿 컨테이너가 리턴한 HTTP 응답결과를 검증한다.
		.andExpect(MockMvcResultMatchers.status().isOk())
	    .andExpect(MockMvcResultMatchers.status().is(200))
		.andExpect(MockMvcResultMatchers.jsonPath("$.WRITER").isNotEmpty())
		.andExpect(MockMvcResultMatchers.jsonPath("$.WRITER").value("gugu"));
//		mockMvc.perform(get("/hello").param("name", "gugu")).andExpect(status().isOk()).andExpect(content().string("hello : gugu"));
	}
	
	
}