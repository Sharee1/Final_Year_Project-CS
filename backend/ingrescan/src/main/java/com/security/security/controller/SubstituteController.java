package com.security.security.controller;

import com.security.security.model.Recipe;
import com.security.security.model.Substitute;
import com.security.security.service.SubstituteService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@RestController
@RequestMapping("/api")
public class SubstituteController {


    @Autowired
    private SubstituteService substituteService;

    //http://localhost:8080/api/add
    @PostMapping("/add")
    public Substitute addSubstitute(@RequestBody Substitute substitute) {
        return substituteService.addSubstitute(substitute);
    }

    //http://localhost:8080/api/adds
    @PostMapping("/adds")
    public List<Substitute> addSubstitute(@RequestBody List<Substitute> substitutes) {
        return substituteService.addAllSubstitute(substitutes);
    }

    //http://localhost:8080/api/{ingredient}
    @GetMapping("/{ingredient}")
    public Substitute getSubstituteByIngredient(@PathVariable("ingredient")   String ingredient) {
    return    substituteService.getSubstituteByIngredient(ingredient);



    }}