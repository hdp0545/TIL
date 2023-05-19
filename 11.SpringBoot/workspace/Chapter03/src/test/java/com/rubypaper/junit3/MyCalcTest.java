package com.rubypaper.junit3;

import com.rubypaper.Junit.MyCalc;

import junit.framework.TestCase;

public class MyCalcTest extends TestCase {
	
	private MyCalc calc;

	protected void setUp() throws Exception {
		System.out.println("---> setup()");
		calc = new MyCalc(10, 3);
	}

	protected void tearDown() throws Exception {
		System.out.println("---> tearDown()");
		calc = null;
	}

	public void testPlus() {
		System.out.println("---> testplus()");
		assertEquals(13, calc.plus());
	}

	public void testMinus() {
		System.out.println("---> testMinus()");
		assertEquals(7, calc.minus());
	}
}
