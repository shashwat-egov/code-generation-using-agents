package com.example.model;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "category_entity")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Category {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
}