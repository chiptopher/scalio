package com.chiptopher.scalio.user;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class UserConfiguration {

    private final UserRepository userRepository;

    public UserConfiguration(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Bean
    public UserMap getUserMap() {
        return new ScalioUserMap(userRepository);
    }
}
