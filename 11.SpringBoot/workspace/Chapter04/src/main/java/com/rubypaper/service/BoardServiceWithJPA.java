package com.rubypaper.service;

import java.util.Date;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Service;

import com.rubypaper.domain.Board;
import com.rubypaper.persistence.BoardDAO;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.EntityTransaction;
import jakarta.persistence.Persistence;

@Service
public class BoardServiceWithJPA implements ApplicationRunner {

//	@Override
//	public void run(ApplicationArguments args) throws Exception {
//		// EntityManagerFactory 생성
//		EntityManagerFactory emf = Persistence.createEntityManagerFactory("Chapter04");
//		// EntityManager 생성
//		EntityManager em = emf.createEntityManager();
//		
//		// 상세 조회
//		Board board1 = em.find(Board.class, 1);
//		System.out.println("검색된 게시글 : " + board1.toString());
//		
//		// 목록검색
//		String jpql = "select b from Board b order by b.seq desc";
//		List<Board> boardList= em.createQuery(jpql).getResultList();
//		for (Board board : boardList) {
//			System.out.println("---> " + board.toString());
//		}
//		
//		em.close();
//		emf.close();
//	}

	
	
//	@Autowired
//	private BoardDAO boardDAO;
	
	@Override
	public void run(ApplicationArguments args) throws Exception {
		// EntityManagerFactory 생성
		EntityManagerFactory emf = Persistence.createEntityManagerFactory("Chapter04");
		// EntityManager 생성
		EntityManager em = emf.createEntityManager();
		
		// Transaction 획득
		EntityTransaction tx = em.getTransaction();
		
		
				
		// 글 등록
//		for (int i=0; i<5; i++) {
//			Board board = new Board();
//			board.setTitle("JPA 등록 테스트");
//			board.setWriter("테스터");
//			board.setContent("JPA 등록 기능 테스트 중입니다." + i);
//			board.setRegDate(new Date());
//			board.setCnt(0);
//			
//			// 등록하기
//			em.persist(board);
//		}
		
		Board board = new Board();
		board.setSeq(1);
		board.setTitle("merge() 테스트");
		board.setWriter("머지");
		board.setContent("merge()테스트 중");
		board.setRegDate(new Date());
		board.setCnt(0);
		
		
		

		
		//트랜잭션 시작
		tx.begin();
		Board mergedBoard = em.merge(board);


		
		
	
//		// 1건의 글 등록
//		Board board = new Board();
//		board.setTitle("JPA 등록 테스트");
//		board.setWriter("테스터");
//		board.setContent("JPA 등록 기능 테스트 중입니다.");
//		board.setRegDate(new Date());
//		board.setCnt(0);
		
		// 등록하기
//		System.out.println("PERSIST 전 : 영속상태인가 ? ->" + em.contains(findBoard));
//		em.persist(findBoard);
//		System.out.println("PERSIST 후 : 영속상태인가 ? ->" + em.contains(findBoard));
		
		// 수정하기
//		Board findBoard = em.find(Board.class, 1);
//		findBoard.setTitle("--- 제목 수정");
//		findBoard.setContent("--- 내용 수정");
		
		
		// 삭제하기
//		Board findBoard = em.find(Board.class, 1);
//		em.remove(findBoard);
		
		
		tx.commit();
		
		em.close();
		emf.close();
	}

}
