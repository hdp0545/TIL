package com.rubypaper.persistence;

import java.util.List;

import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import com.rubypaper.domain.Board;

@Repository
public class BoardDAO {
	
	// SqlSessionTemplate 타입의 객체는 mybatis  컨테이너 객체이며, 자동설정으로 메모리에 올라간다.
	@Autowired
	private SqlSessionTemplate mybatis;
	
	public void insertBoard(Board board) {
		mybatis.insert("insertBoard", board);
	}
	
	public List<Board> getBoardList() {
		return mybatis.selectList("getBoardList");
	}
	
}
