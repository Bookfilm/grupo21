-- creamos la base de datos (paso 1)
create database grupo22;

-- creamos la tabla usuario que contiene los datos personales del usuario(paso 2)
USE grupo22;
create table usuario(
ID_usuario int primary key auto_increment,
Nombre varchar(50),
Apellido varchar(50),
Email varchar(50) unique,
Contraseña varchar(50),
);

-- creamos la tabla rol que contiene el rol de los distintos tipos de usuarios (paso 3)
USE grupo22;
create table Rol(
ID_rol int primary key auto_increment,
Rol varchar(50)
);

-- Agregamos la columna rol a la tabla usuario (paso 4)
ALTER TABLE usuario
ADD COLUMN rol INT;

-- Agregamos la clave foránea
ALTER TABLE usuario
ADD CONSTRAINT fk_ID_rol
FOREIGN KEY (rol) REFERENCES rol(ID_rol);

-- creamos la tabla sesion que contiene el horario de inicio y de cierre de sesion del usuario(paso 5)
USE grupo22;
Create table Sesion(
ID_sesion int primary key auto_increment,
FOREIGN KEY (ID_usuario) REFERENCES Usuario(id),
fecha_inicio datetime,
fecha_fin datetime
);

-- Agregamos la columna Usuario a la tabla sesion (paso 6)
ALTER TABLE sesion
ADD COLUMN Usuario INT;

-- Agregamos la clave foránea
ALTER TABLE sesion
ADD CONSTRAINT fk_ID_Usuario
FOREIGN KEY (Usuario) REFERENCES usuario(ID_Usuario);