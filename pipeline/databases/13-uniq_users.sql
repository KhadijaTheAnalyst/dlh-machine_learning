-- This SQL script creates a table named 'users' to store unique user information.
-- The table includes an auto-incrementing 'id' as the primary key, a unique

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    PRIMARY KEY (id),
    UNIQUE (email)
);