package com.chiptopher.scalio.user;

import org.junit.Test;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

import static org.assertj.core.api.Assertions.assertThat;

public class UserTest {

    @Test
    public void setPasswordEncryptsPassword() {
        BCryptPasswordEncoder bCryptPasswordEncoder = new BCryptPasswordEncoder();
        User user = new User()
                .setbCryptPasswordEncoder(bCryptPasswordEncoder)
                .setPassword("password");
        assertThat(bCryptPasswordEncoder.matches("password", user.getPassword())).isTrue();
    }

}