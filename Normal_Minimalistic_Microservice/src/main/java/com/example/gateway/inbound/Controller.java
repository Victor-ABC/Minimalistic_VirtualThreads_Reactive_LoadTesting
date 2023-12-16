package com.example.gateway.inbound;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/minimalistic")
public class Controller {


    @Autowired
    public Controller() {    }

    @GetMapping
    public String get() {
        // return all students
        try {
            Thread.sleep(500); //DB-Call
            highCPUTask(); //ca. 500ms
            Thread.sleep(500); //DB-Call
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return "Normal - Minimalistic";
    }
    public static void highCPUTask() {
        long startTime = System.currentTimeMillis();

        // Perform a high CPU-intensive task
        int result = 0;
        for (int i = 0; i < 100_000_000; i++) {
            result += i;
        }

        long endTime = System.currentTimeMillis();
        long executionTime = endTime - startTime;

        System.out.println("Execution Time: " + executionTime + " milliseconds");
    }
}
