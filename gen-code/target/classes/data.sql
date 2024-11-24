-- Insert sample data for Category
INSERT INTO category_entity (name) VALUES ('Dogs');
INSERT INTO category_entity (name) VALUES ('Cats');

-- Insert sample data for Tag
INSERT INTO tag_entity (name) VALUES ('Friendly');
INSERT INTO tag_entity (name) VALUES ('Aggressive');

-- Insert sample data for Pet
INSERT INTO pet_entity (name, category_id, status) VALUES ('Buddy', 1, 'available');
INSERT INTO pet_entity (name, category_id, status) VALUES ('Charlie', 2, 'sold');

-- Insert sample data for Pet Tags
INSERT INTO pet_tags (pet_id, tag_id) VALUES (1, 1);
INSERT INTO pet_tags (pet_id, tag_id) VALUES (2, 2);

-- Insert sample data for User
INSERT INTO user_entity (username, first_name, last_name, email, password, phone, user_status) VALUES ('johndoe', 'John', 'Doe', 'john@example.com', 'password', '1234567890', 1);

-- Insert sample data for Order
INSERT INTO order_entity (pet_id, quantity, ship_date, status, complete) VALUES (1, 2, CURRENT_TIMESTAMP, 'shipped', FALSE);