package com.rubypaper.domain;

import java.util.Date;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.SequenceGenerator;
import jakarta.persistence.Table;
import jakarta.persistence.TableGenerator;
import jakarta.persistence.Temporal;
import jakarta.persistence.TemporalType;
import jakarta.persistence.Transient;
import lombok.Data;

@Data
@Entity
//@TableGenerator(name="BOARD_SEQ_GENERATOR", table="SEQUENCE_TABLE", pkColumnName="BOARD_SEQ", initialValue=0, allocationSize=1)
//@SequenceGenerator(name="BOARD_SEQ_GENERATOR", sequenceName="BOARD_SEQUENCE", initialValue=1, allocationSize=1)
//@Table(name="MY_BOARD")
public class Board {
	@Id // 필수 (식별자 변수를 매핑한다. PK와 매핑되는 변수)
	@GeneratedValue//(strategy = GenerationType.SEQUENCE, generator = "BOARD_SEQ_GENERATOR")//(strategy = GenerationType.TABLE, generator = "BOARD_SEQ_GENERATOR") // (테이블 생성 어노테이션)
	private int seq;
	private String title;
	
//	@Column(updatable=false, unique = true,  nullable = false)
	private String writer;
	private String content;
	
	@Column(name = "REG_DATE")
	@Temporal(TemporalType.DATE)
	private Date regDate;
	
	@Column(insertable = false, columnDefinition = "NUMBER(5) DEFAULT 0")
	private int cnt;
	
	@Transient
	private String searchCondition;
}
