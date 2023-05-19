package com.rubypaper.controller;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.rubypaper.domain.BoardVO;

//@Controller
@RestController
public class BoardController {
	public BoardController() {
		System.out.println("===> BoardController 생성");
	}
	
//	@RequestMapping(value="/hello", method = RequestMethod.GET)
	@GetMapping("/hello")
	public String hello(String name) {
		return "hello : " + name;
	}
	
	@GetMapping("/getBoard")
	public BoardVO getBoard() {
		BoardVO board = new BoardVO();
		board.setSeq(1);
		board.setTitle("테스트제목...");
		board.setWriter("테스터");
		board.setContent("테스트 내용");
		board.setRegDate(new Date());
		board.setCnt(0);
				
		return board;
	}
	
	@GetMapping("/getBoardList")
	public List<BoardVO> getBoardList() {
		List<BoardVO> boardList = new ArrayList<>();
		
		for (int i=1; i <= 10; i++) {
			BoardVO board = new BoardVO();
			board.setSeq(i);
			board.setTitle("테스트제목..."+i);
			board.setWriter("테스터");
			board.setContent("테스트 내용"+i);
			board.setRegDate(new Date());
			board.setCnt(0);
			boardList.add(board);
		}

				
		return boardList;
	}
}
