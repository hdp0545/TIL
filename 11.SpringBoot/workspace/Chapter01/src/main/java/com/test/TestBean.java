package com.test;

import org.springframework.stereotype.Service;

@Service("bean")
public class TestBean {
	private TestBean() {
		// TODO Auto-generated method stub
		System.out.println("===> TestBean 생성");

	}
}
