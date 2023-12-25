package com.security.security.auth;


import jakarta.validation.constraints.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;


@Builder
@NoArgsConstructor
@AllArgsConstructor
@Data
public class RegisterRequest {


    @NotNull(message = "YOU MUST ENTER YOUR FIRST NAME ")
    private String firstName;
    @NotNull(message = "YOU MUST ENTER YOUR LAST NAME ")
    private String lastName;
    @Pattern(regexp = "^(?=.*[A-Z])(?=.*\\d)(?=.*[@#$%^&+=!]).*$", message = "Invalid password pattern")
    private String password;
    @Email(message = "Not a valid email")
    private String email;
}
