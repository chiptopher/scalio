package com.chiptopher.scalio.user;

class ScalioUserMap implements UserMap {

    private final UserRepository userRepository;

    ScalioUserMap(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public User registerUser(String username, String password) {
        User user = new User().setUsername(username).setPassword(password);
        this.userRepository.save(user);
        return user;
    }

    @Override
    public User getUserByUsername(String username) {
        return this.userRepository.findUserByUsername(username);
    }
}
