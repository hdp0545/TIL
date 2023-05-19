package com.rubypaper.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.SessionAttributes;
import org.springframework.web.bind.support.SessionStatus;

import com.rubypaper.domain.User;
import com.rubypaper.service.UserService;
import com.rubypaper.service.UserServiceImpl;

@Controller
// model 에 "user"라는 이름으로 검색결과가 등록되면 세션에도 동일한 이름으로 등록해라.
@SessionAttributes("user")
public class LoginController {
	
	@Autowired
	private UserService userService;
	
	@RequestMapping("/loginView")
	public String loginView() {
//		System.out.println(9/0);
		return "login";
	}
	
	@GetMapping("/logout")
	public String logout(SessionStatus session) {
		session.setComplete();//세션 강제종료
		return "redirect:/";
	}
	
	@PostMapping("/login")
	public String login(User user, Model model) {
		User findUser = userService.getUser(user);
		if (findUser != null && findUser.getPassword().equals(user.getPassword())) {
			model.addAttribute("user", findUser);
			return "forward:getBoardList";
		} else {
			return "forward:loginView";
		}
	}
}
