package com.security.security.repository;

import com.security.security.model.Recipe;
import com.security.security.model.Substitute;
import jakarta.persistence.Id;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface SubstituteRepository extends JpaRepository<Substitute, Integer> {


    Substitute getSubstitueByIngredient(String ingredient);
}
