package com.chiptopher.scalio.web.security;

import com.auth0.jwt.JWT;

import java.util.Date;

import static com.auth0.jwt.algorithms.Algorithm.HMAC512;
import static com.chiptopher.scalio.web.security.JwtConstants.EXPIRATION_TIME;
import static com.chiptopher.scalio.web.security.JwtConstants.SECRET;

public class JwtManager {

    public String encodeJwt(String username) {
        return JWT.create()
                .withSubject(username)
                .withExpiresAt(new Date(System.currentTimeMillis() + EXPIRATION_TIME))
                .sign(HMAC512(SECRET.getBytes()));
    }
}
