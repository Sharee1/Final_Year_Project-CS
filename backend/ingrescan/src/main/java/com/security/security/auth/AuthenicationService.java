package com.security.security.auth;
import com.security.security.config.JwtService;
import com.security.security.entity.Role;
import com.security.security.entity.User;
import com.security.security.repository.UserRepository;
import lombok.AllArgsConstructor;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;


@Service
@AllArgsConstructor
public class AuthenicationService {

    private final UserRepository userRepository;

    private final PasswordEncoder passwordEncoder;
    private final JwtService jwtService;
    private final AuthenticationManager authenticationManager;

    public AuthenicationResponse register(RegisterRequest request) {


        if (userRepository.existsByEmail(request.getEmail())) {

            throw new EmailAlreadyExistsException("Use Different Email Address");
        } else {
            var user = User.builder().firstName(request.getFirstName())
                    .lastName(request.getLastName()).
                    email(request.getEmail()).
                    password(passwordEncoder.encode(request.getPassword()))
                    .role(Role.USER).
                    build();

            User savedUser = userRepository.save(user);


            var jwtToken = jwtService.generateToken(savedUser);
            return AuthenicationResponse.builder().token(jwtToken).build();
        }

    }


    public AuthenicationResponse authenticate(RegisterRequest request) {


        return null;
    }


    public AuthenicationResponse authenticate(AuthenticationRequest request) {
        if (userRepository.existsByEmail(request.getEmail())) {

            authenticationManager.authenticate(
                    new UsernamePasswordAuthenticationToken(
                            request.getEmail(),
                            request.getPassword()
                    )
            );
            var user = userRepository.findByEmail(request.getEmail()).orElseThrow();


            var jwtToken = jwtService.generateToken(user);
            return AuthenicationResponse.builder().token(jwtToken).build();
        } else {

            throw new EmailAlreadyExistsException("Enter Correct Correct Email and Password");
        }

    }


    public class EmailAlreadyExistsException extends RuntimeException {
        public EmailAlreadyExistsException(String message) {
            super(message);
        }

    }
}