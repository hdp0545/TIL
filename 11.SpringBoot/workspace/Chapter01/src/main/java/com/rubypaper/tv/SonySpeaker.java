package com.rubypaper.tv;

import org.springframework.stereotype.Service;

//@Service("sony")
public class SonySpeaker implements Speaker {
	public SonySpeaker() {
		System.out.println("====> SonySpeaker 생성");
		
	}
	
	@Override
	public void volumeUp() {
		// TODO Auto-generated method stub
		System.out.println("====> SonySpeaker 소리 올림");
	}

	@Override
	public void volumeDown() {
		// TODO Auto-generated method stub
		System.out.println("====> SonySpeaker 소리 내림");
	}

}
