CREATE DATABASE if not exists sensortemperatura;
use sensortemperatura;

drop table if exists funcionario;
CREATE TABLE funcionario(
cedula int,
nombre varchar(50),
correo VARCHAR(30),
telefono varchar(20),
primary key (cedula)
);

drop table if exists medicion;
CREATE TABLE medicion(
id INT auto_increment,
cedula_f int,
fecha VARCHAR(15),
hora VARCHAR(20),
lugar varchar(20),
temperatura FLOAT,
FOREIGN KEY (cedula_f) REFERENCES funcionario(cedula),
primary key (id)
);


insert into funcionario(cedula, nombre, correo, telefono)
values
(1, "Juan Huerta", "correojuan", "9813"),
(2, "Maria Margarinhos", "correomariamar", "7342"),
(3, "Benito Duarte", "correobenito", "7342"),
(4, "Maria Morales", "correomariamo", "7342"),
(5, "Ramiro Hidalgo", "correoramiro", "7342"),
(6, "Jose Escurra", "correojose", "7342");
