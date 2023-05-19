package com.rubypaper.common;

import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice
public class BoardExeptionHandler {
	
	@ExceptionHandler(ArithmeticException.class)
	public String handleCustomException(ArithmeticException exception, Model model) {
		model.addAttribute("exception", exception);
		return "/errors/arithmetic";
	}
	
	@ExceptionHandler(Exception.class)
	public String handleException(Exception exception, Model model) {
		model.addAttribute("exception", exception);
		return "/errors/default";
	}
}
