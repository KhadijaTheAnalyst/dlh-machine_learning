-- This SQL script creates a table named 'users' to store user information with a country attribute.
-- The table includes an auto-incrementing 'id' as the primary key, a unique 'email', and a 'country' field.

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY (id),
    UNIQUE (email)
);