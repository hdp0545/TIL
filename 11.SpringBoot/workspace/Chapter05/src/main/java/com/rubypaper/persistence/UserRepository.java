package com.rubypaper.persistence;

import org.springframework.data.jpa.repository.JpaRepository;

import com.rubypaper.domain.User;

public interface UserRepository extends JpaRepository<User, String>  {

}
