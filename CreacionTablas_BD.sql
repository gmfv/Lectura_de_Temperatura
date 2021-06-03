CREATE DATABASE if not exists sensortemperatura1;
use sensortemperatura1;

drop table if exists funcionario;
CREATE TABLE funcionario(
cedula int,
nombre varchar(50),
primary key (cedula)
);

drop table if exists medicion;
CREATE TABLE medicion(
id INT auto_increment,
cedula_f int,
fecha VARCHAR(15),
hora VARCHAR(20),
temperatura FLOAT,
FOREIGN KEY (cedula_f) REFERENCES funcionario(cedula),
primary key (id)
);


insert into funcionario(cedula, nombre)
values
(1, "Juan Huerta"),
(2, "Maria Margarinhos"),
(3, "Benito Duarte"),
(4, "Maria Morales"),
(5, "Ramiro Hidalgo"),
(6, "Jose Escurra");