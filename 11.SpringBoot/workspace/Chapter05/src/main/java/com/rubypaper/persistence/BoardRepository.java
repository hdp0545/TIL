package com.rubypaper.persistence;

import java.util.List;

import org.apache.ibatis.annotations.Param;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import com.rubypaper.domain.Board;

@Repository
public interface BoardRepository extends JpaRepository<Board, Integer> {
	
	//쿼리 메소드 등록
	List<Board> findByTitle(String searchkeyword);
	
	List<Board> findByTitleContaining(String searchkeyword);
	
	List<Board> findByTitleContainingOrContentContaining(String searchKeyword, String content);
	
	List<Board> findByTitleContainingOrderBySeqDesc(String searchkeyword);
	
//	List<Board> findByTitleContaining(String searchkeyword, Pageable pageable);
	
	Page<Board> findByTitleContaining(String searchkeyword, Pageable pageable);
	
//	@Query(value="SELECT SEQ, TITLE, REG_DATE FROM BOARD WHERE TITLE LIKE '%'||:keyword||'%' ORDER BY SEQ DESC"
//			, nativeQuery = true)
//	List<Object[]> getBoardList(@Param("keyword") String keyword);
	
	@Query("From Board b")
	List<Board> getBoardList(Pageable pageable);
 }
