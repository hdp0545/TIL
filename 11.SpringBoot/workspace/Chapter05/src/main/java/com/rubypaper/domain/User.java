package com.rubypaper.domain;

import java.util.ArrayList;
import java.util.List;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;
import lombok.Data;
import lombok.ToString;

@Entity
@Data
@Table(name = "USERS")
@ToString(exclude = "boardList")
public class User {
	@Id
	private String id;
	private String password;
	private String name;
	private String role;
	
	@OneToMany(mappedBy = "user", fetch = FetchType.EAGER, cascade = CascadeType.ALL)// 연관관계의 주인이 아닌 엔티티에 mappedby 설정을 해준다.
	private List<Board> boardList = new ArrayList<Board>();
}
