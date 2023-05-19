package com.rubypaper.Junit;

public class MyCalc {
	private int x;
	private int y;
	
	public MyCalc(int x, int y) {
		// TODO Auto-generated constructor stub
		super();
		this.x = x;
		this.y = y;
	}
	
	public int plus() {
		return x+y;
	}
	
	public int minus() {
		return x-y;
	}
}
