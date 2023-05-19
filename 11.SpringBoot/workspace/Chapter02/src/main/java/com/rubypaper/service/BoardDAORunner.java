package com.rubypaper.service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Service;

import com.rubypaper.persistence.BoardDAO;

@Service
public class BoardDAORunner implements ApplicationRunner {
	
	@Autowired
	private BoardDAO boardDAO;
	
	@Override
	public void run(ApplicationArguments args) throws Exception {
		Map<String, Object> board = new HashMap<String, Object>();
		board.put("SEQ", 2);
		board.put("TITLE", "두 번째 글");
		board.put("WRITER", "채규태");
		board.put("CONTENT", "두 번째 글입니다.");
		//boardDAO.insertBoard(board);
		
		List<Map<String, Object>> boardList = boardDAO.getBoardList();
		for (Map<String, Object> row : boardList) {
			System.out.println("--->" + row.toString());
		}

	}

}
