package com.example.controller;

import com.example.model.Pet;
import com.example.service.PetService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/pet")
public class PetController {

    private final PetService petService;

    public PetController(PetService petService) {
        this.petService = petService;
    }

    @PostMapping
    public ResponseEntity<Pet> addPet(@RequestBody Pet pet) {
        Pet createdPet = petService.addPet(pet);
        return ResponseEntity.ok(createdPet);
    }

    @PutMapping
    public ResponseEntity<Pet> updatePet(@RequestBody Pet pet) {
        Pet updatedPet = petService.updatePet(pet);
        return ResponseEntity.ok(updatedPet);
    }

    @GetMapping("/findByStatus")
    public ResponseEntity<List<Pet>> findPetsByStatus(@RequestParam String status) {
        List<Pet> pets = petService.findPetsByStatus(status);
        return ResponseEntity.ok(pets);
    }

    @GetMapping("/findByTags")
    public ResponseEntity<List<Pet>> findPetsByTags(@RequestParam List<String> tags) {
        List<Pet> pets = petService.findPetsByTags(tags);
        return ResponseEntity.ok(pets);
    }

    @GetMapping("/{petId}")
    public ResponseEntity<Pet> getPetById(@PathVariable Long petId) {
        Optional<Pet> pet = petService.getPetById(petId);
        return pet.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
    }

    @PostMapping("/{petId}")
    public ResponseEntity<Void> updatePetWithForm(@PathVariable Long petId, @RequestParam String name, @RequestParam String status) {
        petService.updatePetWithForm(petId, name, status);
        return ResponseEntity.ok().build();
    }

    @DeleteMapping("/{petId}")
    public ResponseEntity<Void> deletePet(@PathVariable Long petId) {
        petService.deletePet(petId);
        return ResponseEntity.ok().build();
    }

    @PostMapping("/{petId}/uploadImage")
    public ResponseEntity<Void> uploadFile(@PathVariable Long petId, @RequestParam String file) {
        petService.uploadFile(petId, file);
        return ResponseEntity.ok().build();
    }
}