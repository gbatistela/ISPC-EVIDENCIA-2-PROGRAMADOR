-- Ver todos los dispositivos ordenados ascendentemente con el nombre del usuario propietario

*/
Esta consulta permite ver qué dispositivos tiene cada usuario dentro del sistema Smart Home. 
Es clave para el administrador, ya que le da una visión general de la cantidad de equipos conectados por persona.
Con esta información se pueden detectar usuarios que tienen muchos dispositivos (y quizás necesiten soporte especial), 
o identificar dispositivos no asignados correctamente (por ejemplo, si están sin usuario).
También sirve para realizar un seguimiento técnico o mantenimiento preventivo de forma más organizada.
/*

SELECT d.nombre AS dispositivo, d.tipo_dispositivo, u.nombre AS propietario, u.email
FROM dispositivos d
JOIN usuarios u ON d.id_usuario = u.id_usuario
ORDER BY propietario ASC;

-- Mostrar las automatizaciones y los dispositivos que controlan

SELECT a.nombre AS automatizacion, d.nombre AS dispositivo, d.tipo_dispositivo
FROM automatizaciones a
JOIN automatizacion_dispositivos ad ON a.id_automatizacion = ad.id_automatizacion
JOIN dispositivos d ON ad.id_dispositivo = d.id_dispositivo;

-- Consultar los 5 primeros eventos recientes junto con los usuarios que los generaron
SELECT e.tipo_evento, e.descripcion, e.fecha_evento, u.nombre AS usuario
FROM eventos_dispositivos e
JOIN usuarios u ON e.id_usuario = u.id_usuario
ORDER BY e.fecha_evento DESC
LIMIT 5;

-- Consultar los movimientos detectado

SELECT s.id_dispositivo, s.estado_activo, e.tipo_evento, e.descripcion
FROM sensor_movimiento s
JOIN eventos_dispositivos e ON s.id_dispositivo = e.id_dispositivo
WHERE e.tipo_evento = 'deteccion_movimiento';


-- SUBCONSULTAS
-- Mostrar la cantidad de dispositivos de los usuarios que poseen más de un dispositivo
SELECT nombre, apellido,
       (SELECT COUNT(*) 
        FROM dispositivos d 
        WHERE d.id_usuario = u.id_usuario) AS cantidad_dispositivos
FROM usuarios u
WHERE id_usuario IN (
    SELECT id_usuario 
    FROM dispositivos
    GROUP BY id_usuario
    HAVING COUNT(*) > 1
);


-- Mostrar dispositivo que pertenecen al rol de administrador
SELECT 
    nombre AS dispositivo,
    tipo_dispositivo,
    (SELECT u.nombre FROM usuarios u WHERE u.id_usuario = d.id_usuario) AS nombre_admin,
    (SELECT u.rol FROM usuarios u WHERE u.id_usuario = d.id_usuario) AS rol_admin
FROM dispositivos d
WHERE id_usuario IN (
    SELECT id_usuario 
    FROM usuarios 
    WHERE rol = 'administrador'
);
