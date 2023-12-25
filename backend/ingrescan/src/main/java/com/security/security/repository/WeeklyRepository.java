package com.security.security.repository;

import com.security.security.model.WeeklySchedule;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface WeeklyRepository extends JpaRepository<WeeklySchedule,Integer> {


}
