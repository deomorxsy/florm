DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS admins;

--- create user table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR (120) UNIQUE NOT NULL
);

--- create admins table
CREATE TABLE admins (
    admin_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    privilege_level INT NOT NULL CHECK(privilege_level >= 1)
);

CREATE TABLE post (
    id SERIAL PRIMARY KEY,
    author_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES users (user_id)
);
