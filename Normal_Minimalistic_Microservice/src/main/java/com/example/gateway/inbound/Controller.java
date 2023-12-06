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
            Thread.sleep(4000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return "Normal - Minimalistic";
    }
}
