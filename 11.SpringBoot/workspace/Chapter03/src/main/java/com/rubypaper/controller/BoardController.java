package com.rubypaper.controller;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.rubypaper.domain.BoardVO;
import com.rubypaper.service.BoardService;

//@Controller
@RestController
public class BoardController {
	
	@Autowired
	private BoardService boardService;
	
	public BoardController() {
		System.out.println("===> BoardController 생성");
	}
	
//	@RequestMapping(value="/hello", method = RequestMethod.GET)
	@GetMapping("/hello")
	public String hello(String name) {
		return boardService.hello(name);
	}
	
	@GetMapping("/getBoard")
	public Map<String, Object> getBoard(int seq) {
		return boardService.getBoard(seq);
	}
	
	@GetMapping("/getBoardList")
	public List<Map<String, Object>> getBoardList() {
		return boardService.getBoardList();
	}
}
