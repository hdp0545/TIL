package com.rubypaper.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class SecurityController {
	@GetMapping("/")
	public String index() {
		return "index";
	}
	
	@GetMapping("/login")
	public String login() {
		return "login";
	}
	
	@GetMapping("/success")
	public String success() {
		return "success";
	}
	
	@GetMapping("/member") 
	public String member(){
		return "member";
	}
	
	@GetMapping("/manager") 
	public String manager(){
		return "manager";
	}
	
	@GetMapping("/admin") 
	public String admin(){
		return "admin";
	}
}
