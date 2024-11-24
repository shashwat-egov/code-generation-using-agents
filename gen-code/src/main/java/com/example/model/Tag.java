package com.example.model;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "tag_entity")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Tag {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
}