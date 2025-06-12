-- crear rol
use grupo22;
insert into Rol(rol)
values ("Administración");

-- leer rol
select * from rol

-- Actualizar rol
UPDATE rol
SET Rol = "usuario"
WHERE ID_rol = 1

-- Eliminar rol
DELETE FROM rol
WHERE ID_rol = 1;