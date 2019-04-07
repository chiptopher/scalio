package com.chiptopher.scalio.web.user;

public class UserRequest {
    private String username;
    private String password;

    public String getUsername() {
        return username;
    }

    public UserRequest setUsername(String username) {
        this.username = username;
        return this;
    }

    public String getPassword() {
        return password;
    }

    public UserRequest setPassword(String password) {
        this.password = password;
        return this;
    }
}
