CREATE DATABASE IF NOT EXISTS nork;
USE nork;

CREATE TABLE IF NOT EXISTS moradores (
  id INT(11) AUTO_INCREMENT,
  name VARCHAR(255),
  PRIMARY KEY (id)
);

INSERT INTO moradores VALUE(0, 'Renan');
INSERT INTO moradores VALUE(0, 'Ana');
INSERT INTO moradores VALUE(0, 'Luana');
INSERT INTO moradores VALUE(0, 'Silvana');
INSERT INTO moradores VALUE(0, 'Reinaldo');

CREATE TABLE IF NOT EXISTS cars (
  id INT(11) AUTO_INCREMENT,
  morador_idmoradores int,
  modelo VARCHAR(20),
  cor VARCHAR(20),
  PRIMARY KEY (id)
);

ALTER TABLE cars ADD CONSTRAINT FOREIGN KEY (morador_idmoradores) REFERENCES moradores(id);

INSERT INTO cars VALUE(0, 1, 'convertible', 'blue');
INSERT INTO cars VALUE(0, 2, 'hatch', 'gray');
INSERT INTO cars VALUE(0, 2, 'sedan', 'yellow');
INSERT INTO cars VALUE(0, 2, 'convertible', 'gray');
INSERT INTO cars VALUE(0, 3, 'sedan', 'blue');
INSERT INTO cars VALUE(0, 3, 'hatch', 'gray');
