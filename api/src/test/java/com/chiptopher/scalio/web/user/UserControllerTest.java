package com.chiptopher.scalio.web.user;

import com.auth0.jwt.JWT;
import com.auth0.jwt.interfaces.DecodedJWT;
import com.chiptopher.scalio.user.UserMap;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.annotation.DirtiesContext;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.MvcResult;

import java.io.UnsupportedEncodingException;
import java.sql.Date;
import java.time.Instant;

import static org.assertj.core.api.Assertions.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
@RunWith(SpringRunner.class)
@AutoConfigureMockMvc
@DirtiesContext(classMode = DirtiesContext.ClassMode.BEFORE_EACH_TEST_METHOD)
public class UserControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private UserMap userMap;

    @Test
    public void registeringAUserCreatesThem() throws Exception {
        String body = "{\"username\":\"email@localhost\",\"password\":\"password\"}";
        MvcResult response = this.mockMvc.perform(post("/api/user/register")
                .contentType(MediaType.APPLICATION_JSON)
                .content(body))
                .andExpect(status().isCreated())
                .andReturn();

        assertThat(userMap.getUserByUsername("email@localhost")).isNotNull();
    }

    @Test
    public void registerAddsTheTokenWhenCreatingAUser() throws Exception {
        String body = "{\"username\":\"email@localhost\",\"password\":\"password\"}";
        MvcResult response = this.mockMvc.perform(post("/api/user/register")
                .contentType(MediaType.APPLICATION_JSON)
                .content(body))
                .andReturn();

        assertResponseReturnsValidToken(response);
    }

    @Test
    public void loginGetsAppropriateJwtForUser() throws Exception {
        String body = "{\"username\":\"email@localhost\",\"password\":\"password\"}";
        mockMvc.perform(post("/api/user/register")
                .contentType(MediaType.APPLICATION_JSON)
                .content(body));
        MvcResult result = mockMvc.perform(post("/api/user/login")
                .contentType(MediaType.APPLICATION_JSON)
                .content(body)).andReturn();
        assertResponseReturnsValidToken(result);
    }

    private void assertResponseReturnsValidToken(MvcResult response) {
        String token = getTokenFromResponse(response);
        assertThat(JWT.decode(token).getSubject()).isEqualTo("email@localhost");
        assertThat(JWT.decode(token).getExpiresAt()).isBetween(Date.from(Instant.now().minusSeconds(2).plusMillis(864_000_000)), Date.from(Instant.now().plusMillis(864_000_000)));
    }

    private String getTokenFromResponse(MvcResult response) {
        return response.getResponse().getHeader("Authorization").replace("Bearer ", "");

    }
}