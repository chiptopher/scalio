package com.chiptopher.scalio.user;

public interface UserMap {
    User registerUser(String username, String password);
    User getUserByUsername(String username);
}
