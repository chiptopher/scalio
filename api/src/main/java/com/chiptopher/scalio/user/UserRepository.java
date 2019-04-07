package com.chiptopher.scalio.user;

import org.springframework.data.jpa.repository.JpaRepository;

interface UserRepository extends JpaRepository<User, Long> {

    User findUserByUsername(String username);
}
