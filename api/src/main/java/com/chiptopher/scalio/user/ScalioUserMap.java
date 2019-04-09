package com.chiptopher.scalio.user;

import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

class ScalioUserMap implements UserMap {

    private final UserRepository userRepository;
    private final BCryptPasswordEncoder bCryptPasswordEncoder;
    private final String jwtSecret;

    ScalioUserMap(UserRepository userRepository, BCryptPasswordEncoder bCryptPasswordEncoder, String jwtSecret) {
        this.userRepository = userRepository;
        this.bCryptPasswordEncoder = bCryptPasswordEncoder;
        this.jwtSecret = jwtSecret;
    }

    @Override
    public User registerUser(String username, String password) {
        User user = new User()
                .setbCryptPasswordEncoder(this.bCryptPasswordEncoder)
                .setJwtSecret(jwtSecret)
                .setUsername(username)
                .setPassword(password);
        this.userRepository.save(user);
        return user;
    }

    @Override
    public User getUserByUsername(String username) {
        return this.userRepository.findUserByUsername(username).setbCryptPasswordEncoder(this.bCryptPasswordEncoder).setJwtSecret(jwtSecret);
    }
}
