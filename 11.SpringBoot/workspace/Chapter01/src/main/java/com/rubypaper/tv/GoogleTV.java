package com.rubypaper.tv;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service("tv")
public class GoogleTV implements TV {
	
	// Autowired 사용시 주의점
	// 1. 만드시 Speaker 타입의 객체가 존재해야한다.
	// 2. Speaker 타입의 객체는 유일해야 한다.
	@Autowired // Type Injection
	private Speaker speaker;
	
	public GoogleTV() {
		System.out.println("====> GoogleTV 생성");
	}
	

	public void powerOn() {
		System.out.println("====> GoogleTV 전원켜기");
	}
	
	public void powerOff() {
		System.out.println("====> GoogleTV 전원 끈다");
	}
	
	public void volumeUp() {
		speaker.volumeUp();
	}
	
	public void volumeDown() {
		speaker.volumeDown();
	}

}
