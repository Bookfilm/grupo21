-- insertar datos en la tabla
Insert  into Rol (rol)
values('administracion');

-- leer dato
select * from rol;

-- actualizar
update rol
set Rol = 'admin'
where ID_rol = 1;

-- eliminar
delete from rol 
where ID_rol = 2;
