package com.rubypaper;

import java.util.Optional;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import com.rubypaper.domain.Board;
import com.rubypaper.persistence.BoardRepository;

@SpringBootTest
class BoardRepositoryTest {
	
	@Autowired
	private BoardRepository boardRepository;
	
	
	@Test
	void testDeleteBoard() {
		boardRepository.deleteById(1);
	}
	
//	@Test
	void testUpdateBoard() {
		Board board = new Board();
		board.setSeq(1);
		board.setTitle("---수정제목");
		board.setContent("내용수정");
		boardRepository.save(board);
	}
	
	
	
//	@Test
	void testGetBoard() {
		
		Optional<Board> findBoard = boardRepository.findById(1);
		if(findBoard.isPresent()) {
			Board board = findBoard.get();
		System.out.println(board.toString());
		}
	}
	
	
//	@Test
	void testInsertBoard() {
		Board board = new Board();
		board.setTitle("JPA Test");
//		board.setWriter("테스터");
		board.setContent("JPA 등록테스트");
		boardRepository.save(board);
	}
	
	

}
