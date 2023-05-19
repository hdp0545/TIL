package com.rubypaper.domain;

import java.util.Date;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.SequenceGenerator;
import lombok.Data;
import lombok.ToString;

@Data
@SequenceGenerator(name="BOARD_SEQ_GENERATOR", sequenceName="BOARD_SEQUENCE", initialValue=1, allocationSize=1)
@Entity
@ToString(exclude = "user")
public class Board {
	@Id // 필수 (식별자 변수를 매핑한다. PK와 매핑되는 변수)
	@GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "BOARD_SEQ_GENERATOR")
	private int seq;
	private String title;
	
//	@Column(updatable = false)
//	private String writer;
	private String content;
	
	@Column(updatable = false)
	private Date regDate = new Date();
	private int cnt = 0;
	
	@ManyToOne(fetch = FetchType.EAGER) // User테이블을 가져오는 시점(EAGER = 즉시, LAZY = 필요할 때만)
	@JoinColumn(name = "USER_ID", nullable = false) // BOARD 테이블에 USER_ID라는 FK 컬럼 추가
	private User user;
}
