# Smart Home Database — Evidencia 6

## Descripción
Este proyecto forma parte de la evidencia número 6 y tiene como objetivo mostrar el script DML de la base de datos del sistema Smart Home, un hogar inteligente que gestiona usuarios, dispositivos conectados, automatizaciones y eventos.
En este script se incluyen inserciones de datos reales, consultas multitabla y subconsultas que reflejan situaciones que podrían pasar en un sistema real, como detectar qué usuarios tienen más dispositivos o qué automatizaciones están activas.

La idea es demostrar cómo se puede trabajar con una base de datos completa y ordenada, pensada para ser útil y práctica dentro del contexto del negocio.

---

## Cómo ejecutar el script

1. Ingresar a [https://onecompiler.com/mysql](https://onecompiler.com/mysql)
2. Seleccionar el lenguaje **MySQL**.
3. Copiar y pegar el contenido del archivo `SmartHome_DML.sql` en el editor.
4. Ejecutar el código para visualizar los resultados de las consultas.

Importante:
En OneCompiler no se puede crear una base de datos nueva, así que hay que eliminar o comentar las líneas CREATE DATABASE y USE antes de ejecutar el script.

---

## Motor de base de datos utilizado
El proyecto fue desarrollado usando MySQL 8 como motor principal.
También se puede ejecutar sin problemas en MariaDB o cualquier entorno compatible con MySQL.

El código respeta la sintaxis estándar de MySQL (por ejemplo: tipos de datos, claves foráneas y restricciones), por lo que no debería generar errores si se usa un entorno similar.

---

## Contenido del script
El archivo `SmartHome_DML.sql` incluye todo lo necesario para probar la base de datos:
- Inserciones (`INSERT`) para poblar las tablas con datos de ejemplo: usuarios, dispositivos, sensores, automatizaciones y eventos.
- Consultas multitabla (JOIN) que muestran relaciones reales entre los datos (por ejemplo, qué dispositivos tiene cada usuario o qué automatización controla qué aparato).
- **Subconsultas** que responden a preguntas más específicas del sistema, como cuántos dispositivos tiene cada usuario o qué dispositivos pertenecen al administrador.
- Comentarios descriptivos que explican el propósito de cada consulta.

---

## Ejemplo de justificación de negocio

A continuación se muestra un ejemplo con explicación incluida:

```sql
-- Esta subconsulta muestra los usuarios que poseen más de un dispositivo.
-- Sirve para detectar usuarios con alta carga de equipos y ofrecer soporte prioritario.
SELECT nombre, apellido 
FROM usuarios
WHERE id_usuario IN (
    SELECT id_usuario FROM dispositivos GROUP BY id_usuario HAVING COUNT(*) > 1
);

sql

## Otro ejemplo:

```sql
-- Esta consulta muestra los dispositivos que pertenecen al rol de administrador.
-- Permite identificar qué equipos están bajo control directo del administrador del sistema,
-- algo importante para temas de seguridad o mantenimiento remoto.
SELECT nombre AS dispositivo, tipo_dispositivo
FROM dispositivos
WHERE id_usuario IN (
    SELECT id_usuario FROM usuarios WHERE rol = 'administrador'
);


## Conclusion

Este trabajo busca mostrar un ejemplo completo de cómo estructurar y consultar una base de datos de un hogar inteligente.
Cada tabla y consulta fue pensada para reflejar necesidades reales del sistema, como:

- Monitorear qué usuarios tienen más dispositivos.

- Analizar los eventos registrados por cada equipo.

- Controlar automatizaciones activas.

- Obtener información rápida para soporte y gestión.

De esta forma, el proyecto no solo cumple con los requisitos técnicos de la consigna, sino que también representa un caso práctico y funcional de cómo se podría aplicar una base de datos relacional en un entorno real de Internet de las Cosas (IoT).
