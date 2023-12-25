package com.security.security.service;

import com.security.security.model.Recipe;
import com.security.security.model.Substitute;
import com.security.security.repository.SubstituteRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class SubstituteService {


    @Autowired
    private SubstituteRepository substituteRepository;

    public Substitute addSubstitute(Substitute substitute){

        return  substituteRepository.save(substitute);
    }
    public List<Substitute> addAllSubstitute( List<Substitute> substitutes){
        return substituteRepository.saveAll(substitutes);
    }

    public Substitute getSubstituteByIngredient(String ingredient){

        return substituteRepository.getSubstitueByIngredient(ingredient);

    }



}
