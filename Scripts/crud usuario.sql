-- Crear Usuario 
use grupo22;
insert into usuario(Nombre, Apellido, Email, Contraseña)
values ('Ana', 'Medrano', 'analujan761@gmail.com', 'contra123');

-- Leer usuario
Select nombre from usuario

-- Actualizar Usuario
UPDATE usuario
set nombre='Anabella', Apellido='Medranoo'
where ID_usuario = 1;

-- eliminar usuario 
delete from usuario
where ID_usuario = 1;