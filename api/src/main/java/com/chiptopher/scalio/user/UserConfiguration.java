package com.chiptopher.scalio.user;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

import static com.chiptopher.scalio.web.security.JwtConstants.SECRET;

@Configuration
public class UserConfiguration {

    private final UserRepository userRepository;

    public UserConfiguration(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Bean
    public UserMap getUserMap() {
        return new ScalioUserMap(userRepository, new BCryptPasswordEncoder(), SECRET);
    }
}
