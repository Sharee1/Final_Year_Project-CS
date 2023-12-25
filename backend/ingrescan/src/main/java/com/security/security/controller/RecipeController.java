package com.security.security.controller;
import com.security.security.model.Recipe;
import com.security.security.service.RecipeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@RestController
@RequestMapping("/api")
public class RecipeController {



    @Autowired
    private RecipeService recipeService;


    //http://localhost:8080/api/recipe/{name}
    @GetMapping("/recipe/{name}")
    public Recipe getRecipeByName(@PathVariable("name") String recipeName) {
        if (recipeName != null) {
            Recipe recipe = recipeService.getRecipeByName(recipeName);

            if (recipe != null) {
                // Recipe found, return it
                return recipe;
            } else {
                // Recipe not found, throw RuntimeException
                throw new RuntimeException("Recipe not found");
            }
        } else {
            // recipeName is null, throw RuntimeException
            throw new RuntimeException("Recipe name is null");
        }
    }



    @PostMapping("/addRecipe")
    public Recipe addRecipe(@RequestBody Recipe recipe){

        return recipeService.addRecipe(recipe);

    }


    @PostMapping("/addRecipes")
    public List<Recipe> addAllRecipes(@RequestBody List<Recipe> recipes) {
        return recipeService.addAllRecipes(recipes);
    }
}
