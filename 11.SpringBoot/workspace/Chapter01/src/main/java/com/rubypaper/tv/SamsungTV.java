package com.rubypaper.tv;

public class SamsungTV implements TV {
	private Speaker speaker;
	
	public SamsungTV() {
		System.out.println("====> Samsung TV(1) 생성");
	}
	
	public SamsungTV(Speaker speaker) {
		System.out.println("====> Samsung TV(2) 생성");
		this.speaker = speaker;
	}
	

	public void powerOn() {
		System.out.println("====> Samsung TV 전원켜기");
	}
	
	public void powerOff() {
		System.out.println("====> Samsung TV 전원 끈다");
	}
	
	public void volumeUp() {
		// System.out.println("====> Samsung TV 소리 올린다.");
		speaker.volumeUp();
	}
	
	public void volumeDown() {
		// System.out.println("====> Samsung TV 소리내린다");
		speaker.volumeDown();
	}

}
