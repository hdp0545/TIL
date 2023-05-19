package com.rubypaper.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Service;


@Service
public class LoggingService implements ApplicationRunner {
	
	private Logger logger = LoggerFactory.getLogger(LoggingService.class);
	
	@Override
	public void run(ApplicationArguments args) throws Exception {
		// TODO Auto-generated method stub
		logger.trace("TRACE 레벨 로그");
		logger.debug("DEBUG 레벨 로그");
		logger.info("INFO 레벨 로그");
		logger.warn("WARN 레벨 로그");
		logger.error("ERROR 레벨 로그");
	}

}
