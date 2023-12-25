package com.security.security.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor

public class Substitute {



    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private int id;

    @Column(name="ingredient_table")
    private String ingredient;
    @Column(name="substitute_table")
    private String substitute;


}
