package com.rubypaper.controller;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.rubypaper.domain.Board;
import com.rubypaper.service.BoardService;

@Controller
public class BoardController {
	
	@Autowired
	private BoardService boardService;
	
	@RequestMapping("/getBoardList")
	public String getBoardList(Board board, Model model) {
	
		// 검색결과를 모델에 저장한다.
		model.addAttribute("boardList", boardService.getBoardList(board));
		
		
		return "getBoardList";
	}
	
	@GetMapping("/getBoard")
	public String getBoard(Board board, Model model) {
	
		// 검색결과를 모델에 저장한다.
		model.addAttribute("board", boardService.getBoard(board));
		return "getBoard";
	}
	
	
	@GetMapping("/insertBoard")
	public String insertBoardView() {
		return "insertBoard";
	}
	
	@PostMapping("/insertBoard")
	public String insertBoard(Board board) {
		boardService.insertBoard(board);
		//화면으로 가는걸 요청하는 것이 아닌 getBoardList 함수를 요청해야함
		// 뷰 이름 앞에 foward:을 붙이면 ViewResolver를 무시한다.
		return "forward:getBoardList";
	}
	
	@PostMapping("/updateBoard")
	public String updateBoard(Board board) {
		boardService.updateBoard(board);
		//화면으로 가는걸 요청하는 것이 아닌 getBoardList 함수를 요청해야함
		// 뷰 이름 앞에 foward:을 붙이면 ViewResolver를 무시한다.
		return "forward:getBoardList";
	}
	
	@GetMapping("/deleteBoard")
	public String deleteBoard(Board board) {
		boardService.deleteBoard(board);
		//화면으로 가는걸 요청하는 것이 아닌 getBoardList 함수를 요청해야함
		// 뷰 이름 앞에 foward:을 붙이면 ViewResolver를 무시한다.
		return "forward:getBoardList";
	}
		
}
