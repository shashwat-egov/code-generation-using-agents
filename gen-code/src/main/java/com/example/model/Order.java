package com.example.model;

import jakarta.persistence.*;
import lombok.*;
import java.util.Date;

@Entity
@Table(name = "order_entity")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Order {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Long petId;

    private int quantity;

    @Temporal(TemporalType.TIMESTAMP)
    private Date shipDate;

    private String status;

    private boolean complete;
}