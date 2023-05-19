package com.rubypaper.service;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.rubypaper.persistence.BoardDAO;

@Service
public class BoardServiceImpl implements BoardService {
	
	
	@Autowired
	private BoardDAO boardDAO;
	
	public BoardServiceImpl() {		
		System.out.println("===> BoardServiceImpl 생성");
	}
	
	public String hello(String name) {
		return "hello : " + name;
	}
	
	public Map<String, Object> getBoard(int seq) {
		return boardDAO.getBoard(seq);
	}
	
	public List<Map<String, Object>> getBoardList() {
		return boardDAO.getBoardList();
	}
}
