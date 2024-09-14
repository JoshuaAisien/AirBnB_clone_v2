-- create sql file non interactively -e
Create DATABASE IF NOT EXISTS hbnb_dev_db ;

-- create user if not exits
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant all privileges on data_base to database_user
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* to 'hbnb_dev'@'localhost';

-- grant SELECT privilege on performance_schema to database_user
GRANT SELECT ON `performance_schema`.* to 'hbnb_dev'@'localhost';

-- apply changes
FLUSH PRIVILEGES;