CREATE TABLE category_entity (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE tag_entity (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE user_entity (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    phone VARCHAR(255),
    user_status INT
);

CREATE TABLE pet_entity (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    category_id BIGINT,
    status VARCHAR(255),
    FOREIGN KEY (category_id) REFERENCES category_entity(id)
);

CREATE TABLE pet_tags (
    pet_id BIGINT,
    tag_id BIGINT,
    FOREIGN KEY (pet_id) REFERENCES pet_entity(id),
    FOREIGN KEY (tag_id) REFERENCES tag_entity(id)
);

CREATE TABLE order_entity (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    pet_id BIGINT,
    quantity INT,
    ship_date TIMESTAMP,
    status VARCHAR(255),
    complete BOOLEAN,
    FOREIGN KEY (pet_id) REFERENCES pet_entity(id)
);