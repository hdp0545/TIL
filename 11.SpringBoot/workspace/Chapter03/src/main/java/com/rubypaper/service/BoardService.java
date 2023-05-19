package com.rubypaper.service;

import java.util.List;
import java.util.Map;

public interface BoardService {

	String hello(String name);

	Map<String, Object> getBoard(int seq);

	List<Map<String, Object>> getBoardList();

}