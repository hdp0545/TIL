package com.rubypaper.junit4;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import com.rubypaper.Junit.MyCalc;

public class MyCalcTest {
	
	private MyCalc calc;

	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
	}

	@AfterClass
	public static void tearDownAfterClass() throws Exception {
	}

	@Before
	public void setUp() throws Exception {
		System.out.println("---> setup()");
		calc = new MyCalc(10, 3);
	}

	@After
	public void tearDown() throws Exception {
		System.out.println("---> tearDown()");
		calc = null;
	}

	@Test
	public void testPlus() {
		System.out.println("---> testplus()");
		assertEquals(13, calc.plus());
	}

	@Test
	public void testMinus() {
		System.out.println("---> testMinus()");
		assertEquals(7, calc.minus());
	}

}
