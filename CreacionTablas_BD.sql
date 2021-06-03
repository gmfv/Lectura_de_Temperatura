CREATE DATABASE if not exists sensortemperatura1;
use sensortemperatura1;

drop table if exists funcionario;
CREATE TABLE funcionario(
cedula int,
nombre varchar(50),
correo VARCHAR(30),
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


insert into funcionario(cedula, nombre, correo)
values
(1, "Juan Huerta", "correojuan"),
(2, "Maria Margarinhos", "correomariamar"),
(3, "Benito Duarte", "correobenito"),
(4, "Maria Morales", "correomariamo"),
(5, "Ramiro Hidalgo", "correoramiro"),
(6, "Jose Escurra", "correojose");