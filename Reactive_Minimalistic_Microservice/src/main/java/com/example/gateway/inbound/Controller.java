package com.example.gateway.inbound;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Mono;

@RestController
@RequestMapping("/minimalistic")
public class Controller {


    @Autowired
    public Controller() {    }

    @GetMapping
    public Mono<String> get() {
        // Simulate an asynchronous operation with delay
        return Mono.delay(java.time.Duration.ofSeconds(4))
                .map(delay -> "Reactive - Minimalistic");
    }
}
