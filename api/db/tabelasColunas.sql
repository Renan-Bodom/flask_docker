CREATE DATABASE IF NOT EXISTS nork;
USE nork;

CREATE TABLE IF NOT EXISTS moradores (
  id INT(11) AUTO_INCREMENT,
  name VARCHAR(255),
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS cars (
  id INT(11) AUTO_INCREMENT,
  morador_idmoradores int,
  modelo VARCHAR(20),
  cor VARCHAR(20),
  PRIMARY KEY (id)
);

ALTER TABLE cars ADD CONSTRAINT FOREIGN KEY (morador_idmoradores) REFERENCES moradores(id);
