package com.security.security.controller;

import com.security.security.model.WeeklySchedule;
import com.security.security.service.WeeklyScheduleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/api")
public class WeeklyController {


    @Autowired
    private WeeklyScheduleService weeklyScheduleService;


    @PostMapping("/addSchedule")
    public WeeklySchedule addWeeklySchedule(@RequestBody  WeeklySchedule weeklySchedule){

        return weeklyScheduleService.addWeeklySchedule(weeklySchedule);
    }
//
//    @GetMapping("/user")
//    public  void getScheduleByLoggedUser(){
//
//        weeklyScheduleService.getScheduleByLoggedUser();
//    }


}
