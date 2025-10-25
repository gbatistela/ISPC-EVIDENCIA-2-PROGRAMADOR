# Smart Home Database — Evidencia 6

## Descripción
Este proyecto contiene el script DML correspondiente al sistema de hogar inteligente **Smart Home**.  
Incluye inserciones de datos, consultas multitabla y subconsultas justificadas según las necesidades del negocio.

---

## Cómo ejecutar el script

1. Ingresar a [https://onecompiler.com/mysql](https://onecompiler.com/mysql)
2. Seleccionar el lenguaje **MySQL**.
3. Copiar y pegar el contenido del archivo `SmartHome_DML.sql` en el editor.
4. Ejecutar el código para visualizar los resultados de las consultas.

---

## Motor de base de datos utilizado
El script está desarrollado para funcionar en **MySQL** (versión 8 o superior).  
También puede ejecutarse en **MariaDB** o en otros motores compatibles configurando el entorno en modo MySQL.

---

## Contenido del script
El archivo `SmartHome_DML.sql` incluye:
- Inserciones (`INSERT`) para poblar las tablas de usuarios, dispositivos, automatizaciones y eventos.
- Consultas **multitabla con JOIN** para relacionar entidades (usuarios ↔ dispositivos, automatizaciones ↔ dispositivos).
- **Subconsultas** justificadas según el contexto del negocio.
- Comentarios descriptivos que explican el propósito de cada consulta.

---

## Ejemplo de justificación de negocio

```sql
-- Esta subconsulta muestra los usuarios que poseen más de un dispositivo.
-- Sirve para detectar usuarios con alta carga de equipos y ofrecer soporte prioritario.
SELECT nombre, apellido 
FROM usuarios
WHERE id_usuario IN (
    SELECT id_usuario FROM dispositivos GROUP BY id_usuario HAVING COUNT(*) > 1
);
