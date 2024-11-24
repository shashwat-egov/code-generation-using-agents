package com.example.service;

import com.example.model.User;
import com.example.repository.UserRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public User createUser(User user) {
        return userRepository.save(user);
    }

    public void createUsersWithListInput(List<User> users) {
        userRepository.saveAll(users);
    }

    public Optional<User> getUserByName(String username) {
        return userRepository.findAll().stream().filter(user -> user.getUsername().equals(username)).findFirst();
    }

    public void deleteUser(Long id) {
        userRepository.deleteById(id);
    }

    public User updateUser(User user) {
        return userRepository.save(user);
    }

    public String loginUser(String username, String password) {
        // Implement logic for user login
        return "Logged in";
    }

    public String logoutUser() {
        // Implement logic for user logout
        return "Logged out";
    }
}