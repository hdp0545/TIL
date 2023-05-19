package com.rubypaper.persistence;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

// controller 		: @Controller, @RestController
// Service 			: @Service
// DAO 				: @Repository
// Configuration	: @Configuration

@Repository
public class BoardDAO {
	private static final String BOARD_INSERT = "insert into board(seq, title, writer, content) values (?, ?, ?, ?)";
	private static final String BOARD_LIST = "select * from board order by seq desc";
	
	@Autowired
	private JdbcTemplate spring;
	
	public void insertBoard(Map<String, Object> board) {
		spring.update(BOARD_INSERT, board.get("SEQ"), board.get("TITLE"), board.get("WRITER"), board.get("CONTENT"));
	}
	
	public List<Map<String, Object>> getBoardList() {
		return spring.queryForList(BOARD_LIST);
	}
}
