package com.example.gateway.inbound;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Mono;
import reactor.core.scheduler.Schedulers;

@RestController
@RequestMapping("/minimalistic")
public class Controller {


    @Autowired
    public Controller() {    }

    @GetMapping
    public Mono<String> get() {
        // Introduce a 500 milliseconds delay
        Mono<String> delayBefore = Mono.delay(java.time.Duration.ofMillis(500))
                .map(delay -> "Delay before HighCPUTaskReactive");

        // High CPU-intensive task
        Mono<Integer> highCPUTask = highCPUTaskReactive();

        // Introduce another 500 milliseconds delay after the high CPU-intensive task
        Mono<String> delayAfter = Mono.delay(java.time.Duration.ofMillis(500))
                .map(delay -> "Delay after HighCPUTaskReactive");

        // Combine the delays and the high CPU-intensive task
        return delayBefore.then(highCPUTask).then(delayAfter)
                .map(result -> "Reactive - Minimalistic");
    }

    public static Mono<Integer> highCPUTaskReactive() {
        return Mono.fromCallable(() -> {
            long startTime = System.currentTimeMillis();

            // Perform a high CPU-intensive task
            int result = 0;
            for (int i = 0; i < 100_000_000; i++) {
                result += i;
            }

            long endTime = System.currentTimeMillis();
            long executionTime = endTime - startTime;

            System.out.println("Execution Time: " + executionTime + " milliseconds");

            return result;
        });
    }


}
