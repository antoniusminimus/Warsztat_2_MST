CREATE TABLE Users(
id INT(11) AUTO_INCREMENT,
email VARCHAR(255) UNIQUE,
username VARCHAR(255),
hashed_password VARCHAR(60),
PRIMARY KEY(id)
);

ALTER TABLE Users
MODIFY COLUMN hashed_password VARCHAR(90);