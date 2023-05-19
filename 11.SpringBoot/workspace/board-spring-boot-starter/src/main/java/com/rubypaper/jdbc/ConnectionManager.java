package com.rubypaper.jdbc;

import lombok.Data;

@Data
public class ConnectionManager {
	
	private String driverClass;
	private String url;
	private String username;
	private String password;
	
	public ConnectionManager() {
		System.out.println("====> ConnectionManager 생성");
	}
}
