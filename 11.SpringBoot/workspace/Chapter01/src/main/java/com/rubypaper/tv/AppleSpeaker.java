package com.rubypaper.tv;

import org.springframework.stereotype.Service;

@Service("apple")
public class AppleSpeaker implements Speaker {
	public AppleSpeaker() {
		System.out.println("====> AppleSpeaker 생성");
		
	}
	
	@Override
	public void volumeUp() {
		// TODO Auto-generated method stub
		System.out.println("====> AppleSpeaker 소리 올림");
	}

	@Override
	public void volumeDown() {
		// TODO Auto-generated method stub
		System.out.println("====> AppleSpeaker 소리 내림");
	}

}
