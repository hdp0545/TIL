package com.rubypaper.tv;

public class LGTV implements TV {
	private Speaker speaker;
	
	public LGTV() {
		System.out.println("====> LG TV 생성");
	}
	
	
	public void setSpeaker(Speaker speaker) {
		this.speaker = speaker;
	}
	

	public void powerOn() {
		System.out.println("====> LG TV 전원켜기");
	}
	
	public void powerOff() {
		System.out.println("====> LG TV 전원 끈다");
	}
	
	public void volumeUp() {
		speaker.volumeUp();
	}
	
	public void volumeDown() {
		speaker.volumeDown();
	}

}
