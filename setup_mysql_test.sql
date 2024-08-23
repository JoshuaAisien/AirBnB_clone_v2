-- create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant privileges on database hbnb_test_db
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* to 'hbnb_test'@'localhost';

-- grant SELECT privilege on database performance_schema
GRANT SELECT ON `performance_schema`.* to 'hbnb_test'@'localhost';

-- apply privileges
FLUSH PRIVILEGES;