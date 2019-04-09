package com.chiptopher.scalio.web.user;

import com.chiptopher.scalio.user.User;
import com.chiptopher.scalio.user.UserMap;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.xml.ws.Response;

@RestController
@RequestMapping(value = "/api/user")
public class UserController {

    private final UserMap userMap;

    public UserController(UserMap userMap) {
        this.userMap = userMap;
    }

    @PostMapping(value = "/register")
    public ResponseEntity register(@RequestBody UserRequest userRequest) {
        User user = this.userMap.registerUser(userRequest.getUsername(), userRequest.getPassword());
        HttpHeaders headers = new HttpHeaders();
        headers.add("Authorization", "Bearer " + user.generateToken());
        return new ResponseEntity(headers, HttpStatus.CREATED);
    }
}
