package com.rubypaper.config;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity
public class SecrurityConfiguration {
	
	@Autowired
	private UserDetailsService userDetailsService;
	
	@Bean
	SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
		//CSRF 토큰 비활성화
		http.csrf().disable();
		
		// 인증/인가 설정
		http.authorizeHttpRequests()
		.requestMatchers("/member/**").authenticated()
		.requestMatchers("/manager/**").hasRole("MANAGER")
		.requestMatchers("/admin/**").hasRole("ADMIN")
		.anyRequest().permitAll();
		
		// 로그인 화면 설정
		http.formLogin();
		
		//사욪아 정의 USerDetailsService 적용하기
		http.userDetailsService(userDetailsService);
		
		return http.build();
	}
}
