package com.security.security.service;

import com.security.security.entity.User;
import com.security.security.model.WeeklySchedule;
import com.security.security.repository.UserRepository;
import com.security.security.repository.WeeklyRepository;
import org.apache.naming.factory.SendMailFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Service;

@Service
public class WeeklyScheduleService {

    @Autowired
    private WeeklyRepository weeklyRepository;

    @Autowired
    private UserRepository userRepository;

    public WeeklySchedule addWeeklySchedule(WeeklySchedule weeklySchedule) {


        return weeklyRepository.save(weeklySchedule);
    }

}