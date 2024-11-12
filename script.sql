/*   THIS SCRIPT IS MEANT TO BE USED IN A PostgreSQL SHELL (PSQL)   */

-- Creation of the database
CREATE DATABASE tasks_manager;

-- Conection to the database
\c tasks_manager

-- Creation of the table "users"
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
);

-- Creation of the table "projects"
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    p_name VARCHAR(100) NOT NULL,
    p_description TEXT
);

-- Creation of the table "tasks"
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    t_description TEXT,
    project_id INTEGER REFERENCES projects(id) ON DELETE CASCADE,
    t_user_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
    due_date DATE
);

