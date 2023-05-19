package com.rubypaper.config;

import org.springframework.boot.context.properties.ConfigurationProperties;

import lombok.Data;

@Data
@ConfigurationProperties(prefix = "board.jdbc")
public class ConnectionManagerProperties {
	
	private String driverClass;
	private String url;
	private String username;
	private String password;
}
