-- Creación de los usuarios para la aplicación en python:
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE "departamento" (
  "id_departamento" int PRIMARY KEY,
  "nombre" varchar,
  "descripcion" text
);

CREATE TABLE "rol" (
  "id_rol" int PRIMARY KEY,
  "nombre_rol" varchar,
  "categoria" varchar
);

CREATE TABLE "empleado" (
  "id_empleado" int PRIMARY KEY,
  "nombres" varchar,
  "apellidos" varchar,
  "documento" varchar,
  "correo" varchar,
  "telefono" varchar
);

CREATE TABLE "historial_empleado" (
  "id_historial" int PRIMARY KEY,
  "id_empleado" int,
  "id_rol" int,
  "id_departamento" int,
  "fecha_inicio" date,
  "fecha_fin" date
);

CREATE TABLE "turno" (
  "id_turno" int PRIMARY KEY,
  -- "fecha" date, se elimina por normalizacion
  "hora_inicio" time,
  "hora_fin" time,
  "jornada" varchar
);


CREATE TABLE "asignacion_turno" (
  "id_asignacion" int PRIMARY KEY,
  "id_empleado" int,
  "id_turno" int,
  "observaciones" text,
  "estado" int, -- se agrega FK de la tabla nueva creada llamada estado 
  -- fecha añadida ya que se elimino en turno 
  "fecha" date
);


create table "estado" (
"id_estado" int primary key,
"Descripcion" varchar);

CREATE TABLE "cobertura" (
  "id_cobertura" int PRIMARY KEY,
  "fecha" date, -- que cantidad de usuarios necesitan ese dia
  "id_rol" int,
  "cantidad_turnos" int,
  -- "duracion_turno" int, se elimina debido a que el turno por defecto es de 8 horas
  "cantidad_empleados_por_turno" int
);

CREATE TABLE "zona" (
  "id_zona" int PRIMARY KEY,
  "nombre" varchar,
  "nivel_acceso" int
);

create table "nivel_acceso" (
"id_nivel_acceso" int primary key,
"descripcion" varchar)

CREATE TABLE "acceso" (
  "id_acceso" int PRIMARY KEY,
  "id_zona" int
);

CREATE TABLE "tarjeta_acceso" (
  "id_tarjeta" int PRIMARY KEY,
  "serial" varchar,
  "nivel_acceso" int,
  "fecha_expedicion" date,
  "vencimiento" date,
  "id_empleado" int UNIQUE
);


CREATE TABLE "validacion" (
  "id_validacion" int PRIMARY KEY,
  "id_tarjeta" int,
  "nivel_requerido" int,
  "fecha" date,
  "estado_validacion" int,
  "id_acceso" int
);

create table "estado_validacion"(
"id_estado_validacion" int primary key,
"descripcion" varchar
);

alter table "validacion" add foreign key ("estado_validacion") references "estado_validacion" ("id_estado_validacion");

alter table "validacion" add foreign key ("nivel_requerido") references "nivel_acceso" ("id_nivel_acceso");

CREATE TABLE "capacitacion" (
  "id_capacitacion" int PRIMARY KEY,
  "nombre" varchar,
  "descripcion" text,
  "duracion" int
);

CREATE TABLE "empleado_capacitacion" (
  "id_empleado" int,
  "id_capacitacion" int,
  "fecha_inicio" date,
  "fecha_fin" date,
  "vencimiento" date
);

CREATE TABLE "asistencia" (
  "id_asistencia" int PRIMARY KEY,
  "id_empleado" int,
  "id_tarjeta" int,
  "hora_inicio" time,
  "hora_fin" time
);

CREATE TABLE "incidencia" (
  "id_incidencia" int PRIMARY KEY,
  "id_empleado" int,
  "fecha_incidencia" date,
  "tipo" varchar,
  "descripcion" text
);

CREATE TABLE "rendimiento" (
  "id_evaluacion" int PRIMARY KEY,
  "id_empleado" int,
  "puntualidad" int,
  "eficiencia" int,
  "manejo_situaciones" int
);

CREATE TABLE "licencia" (
  "id_licencia" int PRIMARY KEY,
  "tipo" varchar
);

CREATE TABLE "solicitud_licencia" (
  "id_solicitud" int PRIMARY KEY,
  "id_empleado" int,
  "id_licencia" int,
  "fecha_inicio" date,
  "fecha_fin" date,
  "estado" varchar,
  "motivo" text,
  "fecha_solicitud" date,
  "aprobado_por" varchar
);

CREATE TABLE "comunicacion_interna" (
  "id_comunicacion" int PRIMARY KEY,
  "fecha" date,
  "asunto" varchar,
  "contenido" text,
  "remitente" int,
  "destinatario_empleado" int,
  "destinatario_departamento" int,
  "tipo_destinatario" varchar
);


alter table "tarjeta_acceso" add foreign key ("nivel_acceso") references "nivel_acceso" ("id_nivel_acceso");

alter table "zona" add foreign key ("nivel_acceso") references "nivel_acceso" ("id_nivel_acceso");

ALTER TABLE "historial_empleado" ADD FOREIGN KEY ("id_empleado") REFERENCES "empleado" ("id_empleado");

alter table "asignacion_turno"  add foreign key ("estado") references "estado" ("id_estado"); -- creacion de llave foranera en la tabla asignacion turno

ALTER TABLE "historial_empleado" ADD FOREIGN KEY ("id_rol") REFERENCES "rol" ("id_rol");

ALTER TABLE "historial_empleado" ADD FOREIGN KEY ("id_departamento") REFERENCES "departamento" ("id_departamento");

ALTER TABLE "asignacion_turno" ADD FOREIGN KEY ("id_empleado") REFERENCES "empleado" ("id_empleado");

ALTER TABLE "asignacion_turno" ADD FOREIGN KEY ("id_turno") REFERENCES "turno" ("id_turno");

ALTER TABLE "cobertura" ADD FOREIGN KEY ("id_rol") REFERENCES "rol" ("id_rol");

ALTER TABLE "acceso" ADD FOREIGN KEY ("id_zona") REFERENCES "zona" ("id_zona");

ALTER TABLE "tarjeta_acceso" ADD FOREIGN KEY ("id_empleado") REFERENCES "empleado" ("id_empleado");

ALTER TABLE "validacion" ADD FOREIGN KEY ("id_tarjeta") REFERENCES "tarjeta_acceso" ("id_tarjeta");

ALTER TABLE "validacion" ADD FOREIGN KEY ("id_acceso") REFERENCES "acceso" ("id_acceso");

ALTER TABLE "empleado_capacitacion" ADD FOREIGN KEY ("id_empleado") REFERENCES "empleado" ("id_empleado");

ALTER TABLE "empleado_capacitacion" ADD FOREIGN KEY ("id_capacitacion") REFERENCES "capacitacion" ("id_capacitacion");

ALTER TABLE "asistencia" ADD FOREIGN KEY ("id_empleado") REFERENCES "empleado" ("id_empleado");

ALTER TABLE "asistencia" ADD FOREIGN KEY ("id_tarjeta") REFERENCES "tarjeta_acceso" ("id_tarjeta");

ALTER TABLE "incidencia" ADD FOREIGN KEY ("id_empleado") REFERENCES "empleado" ("id_empleado");

ALTER TABLE "rendimiento" ADD FOREIGN KEY ("id_empleado") REFERENCES "empleado" ("id_empleado");

ALTER TABLE "solicitud_licencia" ADD FOREIGN KEY ("id_empleado") REFERENCES "empleado" ("id_empleado");

ALTER TABLE "solicitud_licencia" ADD FOREIGN KEY ("id_licencia") REFERENCES "licencia" ("id_licencia");

ALTER TABLE "comunicacion_interna" ADD FOREIGN KEY ("remitente") REFERENCES "empleado" ("id_empleado");

ALTER TABLE "comunicacion_interna" ADD FOREIGN KEY ("destinatario_empleado") REFERENCES "empleado" ("id_empleado");

ALTER TABLE "comunicacion_interna" ADD FOREIGN KEY ("destinatario_departamento") REFERENCES "departamento" ("id_departamento");

alter table "tarjeta_acceso" add foreign key ("nivel_acceso") references "nivel_acceso" ("id_nivel_acceso");