-- crear sesion
use grupo22;
INSERT INTO  Sesion (Usuario, fecha_inicio, fecha_fin)
VALUES ('1', '2025-06-07 15:39:55, 2025-06-07 17:32:06');

-- leer tabla sesion
SELECT * FROM Sesion;

-- Actualizar tabla sesion
UPDATE Sesion  
SET fecha_sesion = '2025-06-07 15:45:09',  '2025-06-07 17:46:09'
WHERE ID_sesion = 1;

-- Eliminar de le tabla de sesion
DELETE FROM Sesion
WHERE ID_sesion = 1; 
