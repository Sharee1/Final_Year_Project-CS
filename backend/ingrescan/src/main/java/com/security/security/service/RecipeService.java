package com.security.security.service;


import com.security.security.model.Recipe;
import com.security.security.repository.RecipeRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class RecipeService {

    @Autowired
    private RecipeRepository recipeRepository;


    public Recipe addRecipe(Recipe recipe) {


        return recipeRepository.save(recipe);

    }

    public List<Recipe> addAllRecipes(List<Recipe> recipes) {

        return recipeRepository.saveAll(recipes);

    }

    public Recipe getRecipeByName(String recipeName) {

            return recipeRepository.findByRecipeNameContainingIgnoreCase(recipeName);

        }
    }