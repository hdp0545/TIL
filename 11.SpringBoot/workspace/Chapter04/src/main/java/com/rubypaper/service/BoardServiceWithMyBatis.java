package com.rubypaper.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Service;

import com.rubypaper.domain.Board;
import com.rubypaper.persistence.BoardDAO;

//@Service
public class BoardServiceWithMyBatis implements ApplicationRunner {

	@Autowired
	private BoardDAO boardDAO;
	
	@Override
	public void run(ApplicationArguments args) throws Exception {
		// TODO Auto-generated method stub
		Board board = new Board();
		board.setTitle("MyBatis 등록 테스트");
		board.setWriter("테스터");
		board.setContent("Mybatis 등록 기능 테스트 중입니다.");
		boardDAO.insertBoard(board);
		
		List<Board> boardList = boardDAO.getBoardList();
		for (Board row : boardList) {
			System.out.println("---> " + row.toString());
		}
	}

}
