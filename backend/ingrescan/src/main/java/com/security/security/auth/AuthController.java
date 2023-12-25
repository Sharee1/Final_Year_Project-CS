package com.security.security.auth;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;




@RestController
@RequestMapping("/api/auth")
@RequiredArgsConstructor
public class AuthController {

    private final  AuthenicationService authenicationService;


    //http://localhost:8080/api/auth/register
    @PostMapping("/register")
    public ResponseEntity<AuthenicationResponse> Register(@RequestBody @Valid RegisterRequest request){
        return ResponseEntity.ok(authenicationService.register(request));
    }


    //http://localhost:8080/api/auth/authenticate
    @PostMapping("/authenticate")
    public ResponseEntity<AuthenicationResponse> Register( @RequestBody AuthenticationRequest request){
        return ResponseEntity.ok(authenicationService.authenticate(request));
    }
}
