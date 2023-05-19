package com.rubypaper.config;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.condition.ConditionalOnMissingBean;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.rubypaper.jdbc.ConnectionManager;

@Configuration
@EnableConfigurationProperties(ConnectionManagerProperties.class) // 밑의 ConnectionManagerProperties를 참조하기 위해
public class BoardAutoConfiguration {
	
	@Autowired
	private ConnectionManagerProperties properties;
	
	public BoardAutoConfiguration() {
		System.out.println("===> BoardAutoConfiguration 생성");
	}
	
	// ConnectionManager 객체를 생성하는 설정
	@Bean
	@ConditionalOnMissingBean // ConnectionManager 타입의 객체가 메모리에 없으면 이를 실행하라
	ConnectionManager connectionManager() {
		ConnectionManager manager = new ConnectionManager();
		manager.setDriverClass(properties.getDriverClass());
		manager.setUrl(properties.getUrl());
		manager.setUsername(properties.getUsername());
		manager.setPassword(properties.getPassword());
		return manager;
	}
}


