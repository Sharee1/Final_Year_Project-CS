package com.security.security.model;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;


@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
@Entity
@Table(name="recipe_table")
public class Recipe {


@Id
@GeneratedValue(strategy = GenerationType.AUTO)
private int  recipeId;
private String recipeName;
private int totalIngredients;
@Column(name = "ingredients_required", length = 2048)
private String ingredientsRequired;
@Column(name = "description", length = 1024)
private String  description;

;


}



