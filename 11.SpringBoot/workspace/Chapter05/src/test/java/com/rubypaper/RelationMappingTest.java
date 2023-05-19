package com.rubypaper;

import java.util.List;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import com.rubypaper.domain.Board;
import com.rubypaper.domain.User;
import com.rubypaper.persistence.BoardRepository;
import com.rubypaper.persistence.UserRepository;

@SpringBootTest
class RelationMappingTest {

	@Autowired
	private BoardRepository boardRepository;
	
	@Autowired
	private UserRepository userRepository;
	
	@Test
	void testCascade() {
		// user1 회원 삭제
		userRepository.deleteById("user01");
		
	}
	
	
//	@Test
	void testOneToMany() {
		//5번게시글을 검색한다.
		User user = userRepository.findById("user01").get();
		
		System.out.println(user.getId() + "유저");
		System.out.println("이름 : " + user.getName());
//		System.out.println("작성자 : " + board.getUser().getName());
//		System.out.println("작성자 : " + board.getUser().getId());
		List<Board> boardList = user.getBoardList();
		for (Board board : boardList) {
			System.out.println("--->" + board.toString());
		}
	}
	
//	@Test
	void testManyToOne() {
		//5번게시글을 검색한다.
		Board board = boardRepository.findById(5).get();
		
		System.out.println(board.getSeq() + "번 게시글 상세 정보");
		System.out.println("제목 : " + board.getTitle());
//		System.out.println("작성자 : " + board.getUser().getName());
//		System.out.println("작성자 : " + board.getUser().getId());
	}

//	@BeforeEach
	public void dataSetting() {
		User user1 = new User();
		user1.setId("user01");
		user1.setName("둘리");
		userRepository.save(user1);
		
		User user2 = new User();
		user2.setId("user02");
		user2.setName("도우너");
		userRepository.save(user2);
		
		for (int i=1; i<=3;i++) {
			Board board = new Board();
			board.setTitle("둘리가 등록한 게시글 " + i);
			board.setUser(user1);
			boardRepository.save(board);
		}
		
		for (int i=1; i<=3;i++) {
			Board board = new Board();
			board.setTitle("도우너가 등록한 게시글 " + i);
			board.setUser(user2);
			boardRepository.save(board);
		}
	}
}
