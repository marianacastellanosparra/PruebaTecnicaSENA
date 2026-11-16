# Pruebas del backend

Este directorio contiene las pruebas automatizadas de ORION Maintenance Lite.

La organización prevista es:

- `unit/`: pruebas unitarias de esquemas, validaciones y servicios.
- `integration/`: pruebas de integración con PostgreSQL.

Las pruebas se incorporarán durante las fases de desarrollo e integración.

Las pruebas de integración que validen restricciones y bloqueos propios de PostgreSQL deberán ejecutarse contra una base de datos de pruebas aislada, nunca contra la base de datos productiva.