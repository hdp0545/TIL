package com.rubypaper;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;

import com.querydsl.core.BooleanBuilder;
import com.rubypaper.domain.Board;
import com.rubypaper.domain.QBoard;
import com.rubypaper.persistence.BoardRepository;
import com.rubypaper.persistence.BoardRepositoryQueryDSL;

@SpringBootTest
class QueryMethodTest {
	
	@Autowired
	private BoardRepository boardRepository;
	
	@Autowired
	private BoardRepositoryQueryDSL boardRepositoryQueryDSL;
	
	@Test
	public void testDynamicQuery() {
		BooleanBuilder builder = new BooleanBuilder();
		
		String condition = "CONTENT";
		String keyword = "10";
		QBoard qboard = QBoard.board;
		
		if("TITLE".equals(condition)) {
			builder.and(qboard.title.like("%"+keyword+"%"));
		} else if ("CONTENT".equals(condition)) {
			builder.and(qboard.content.like("%"+keyword+"%"));
		}
		
		Iterable<Board> boardList = boardRepositoryQueryDSL.findAll(builder);
		
		for (Board board : boardList) {
			System.out.println("---> "+ board.toString());
		}
		
		
		System.out.println("");
		
	}
	
//	@Test
	public void testQueryMethod() {
		// 페이징 처리를 위한 Pageable 객체 생성
		Pageable pageable = PageRequest.of(1, 5, Sort.Direction.DESC, "seq");
		
		Page<Board> pageInfo = boardRepository.findByTitleContaining("테스트",pageable);

		System.out.println("검색된 전체 데이터 수 : " + pageInfo.getTotalElements());
		System.out.println("전체 페이지 수 : " + pageInfo.getTotalPages());
		System.out.println("한 페이지에 출력할 데이터 수 : " + pageInfo.getSize());
		System.out.println("검색 결과");
		for (Board board : pageInfo.getContent()) {
			System.out.println("---> "+ board.toString());
		}
		
		if(pageInfo.hasPrevious()) {
			System.out.println("이전 페이지가 있나? : " + pageInfo.previousPageable());
		}
		
		System.out.println("현재 정보" + pageInfo.getPageable());
		
		if(pageInfo.hasNext()) {
			System.out.println("다음 페이지가 있나? : " + pageInfo.nextPageable());
		}
	
		// @Query 사용하기
		// nativeQuery
		List<Board> boardList = boardRepository.getBoardList(pageable);
		for (Board board : boardList) {
			System.out.println("---> "+ board.toString());
		}
	}
	
//	@BeforeEach
	void testInsert() {	
		for (int i=1; i <= 200; i++) {
			Board board = new Board();
			board.setTitle("테스트 제목 " + i);
//			board.setWriter("테스터 " + i);
			board.setContent("테스트 내용 " + i);
			boardRepository.save(board);
		}
	}
}





