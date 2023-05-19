package com.rubypaper.domain;

import java.util.Date;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Data
@Entity
public class Board {
	@Id
	@GeneratedValue
	private int seq;
	private String title;
	@Column(updatable = false)
	private String writer;
	private String content;
	@Column(updatable = false)
	private Date regDate = new Date();
	private int cnt = 0;
}
