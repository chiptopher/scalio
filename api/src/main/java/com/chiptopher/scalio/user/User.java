package com.chiptopher.scalio.user;

import com.auth0.jwt.JWT;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

import javax.persistence.*;
import javax.validation.constraints.Email;
import java.util.Date;

import static com.auth0.jwt.algorithms.Algorithm.HMAC512;

@Entity
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    @Email
    private String username;
    private String password;

    @Transient
    private BCryptPasswordEncoder bCryptPasswordEncoder;
    @Transient
    private String jwtSecret;

    User() {

    }


    public Long getId() {
        return id;
    }

    public User setId(Long id) {
        this.id = id;
        return this;
    }

    public String getUsername() {
        return username;
    }

    public User setUsername(String username) {
        this.username = username;
        return this;
    }

    public String getPassword() {
        return password;
    }

    public User setPassword(String password) {
        this.password = this.bCryptPasswordEncoder.encode(password);
        return this;
    }

    public String generateToken() {
        return JWT.create()
                .withSubject(username)
                .withExpiresAt(new Date(System.currentTimeMillis() + 864_000_000))
                .sign(HMAC512(jwtSecret.getBytes()));
    }

    User setbCryptPasswordEncoder(BCryptPasswordEncoder bCryptPasswordEncoder) {
        this.bCryptPasswordEncoder = bCryptPasswordEncoder;
        return this;
    }

    User setJwtSecret(String jwtSecret) {
        this.jwtSecret = jwtSecret;
        return this;
    }
}
