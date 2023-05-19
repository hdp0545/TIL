package com.rubypaper.persistence;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

@Repository
public class BoardDAO {
	
	// SQL 명령어들
	private static final String BOARD_GET = "select * from board where seq = ?";
	private static final String BOARD_LIST = "select * from board order by seq desc";
	
	@Autowired
	private JdbcTemplate spring;
	
	
	public BoardDAO() {
		System.out.println("===> BoardDAO 생성");
	}
	
	public Map<String, Object> getBoard(int seq) {
		Object[] params = {seq};
		return spring.queryForMap(BOARD_GET, params);
	}
	
	public List<Map<String, Object>> getBoardList() {
		return spring.queryForList(BOARD_LIST);
	}
	
	
}
