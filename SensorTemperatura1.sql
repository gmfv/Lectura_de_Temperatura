-- CREATE DATABASE sensortemperatura1;
-- medicionmedicion
USE sensortemperatura1;
-- 
DROP TABLE if EXISTS funcionario;
CREATE TABLE funcionario(
cedula VARCHAR(10),
nombre VARCHAR(50),
telefono VARCHAR(20),
mail VARCHAR(20),
PRIMARY KEY (cedula)
);

DROP TABLE if EXISTS medicion;
CREATE TABLE medicion(
id_medicion VARCHAR(10),
temperatura FLOAT,
cedulafuncionario VARCHAR(10),
fecha VARCHAR(10),
hora VARCHAR(10), 
lugar_marcacion VARCHAR(50),
FOREIGN KEY (cedulafuncionario) REFERENCES funcionario (cedula),
PRIMARY KEY (id_medicion)
);