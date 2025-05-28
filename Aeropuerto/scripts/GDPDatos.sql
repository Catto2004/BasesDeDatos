-- ========== DATOS MAESTROS ==========
-- Insertar departamentos (con manejo de conflicto por clave primaria)
INSERT INTO departamento (id_departamento, nombre, descripcion)
VALUES
(1, 'Seguridad', 'Encargado de la seguridad aeroportuaria'),
(2, 'Mantenimiento', 'Supervisa el mantenimiento de equipos e infraestructura'),
(3, 'Administración', 'Gestión administrativa y de personal')
ON CONFLICT (id_departamento) DO NOTHING;

-- Insertar roles
INSERT INTO rol (id_rol, nombre_rol, categoria)
VALUES
(1, 'Agente de seguridad', 'Operativo'),
(2, 'Tecnico de mantenimiento', 'Tecnico'),
(3, 'Administracion de turno', 'Administrativo')
ON CONFLICT (id_rol) DO NOTHING;

-- Insertar empleados
INSERT INTO empleado (id_empleado, nombres, apellidos, documento, correo, telefono)
VALUES
(1, 'Juan', 'Perez', '10012345', 'empleado1@gestion.com', '3123456'),
(2, 'Ana', 'Gomez', '10023456', 'empleado2@gestion.com', '3234567'),
(3, 'Luis', 'Martínez', '10034567', 'empleado3@gestion.com', '3456789')
ON CONFLICT (id_empleado) DO NOTHING;

-- Insertar turnos
INSERT INTO turno (id_turno, hora_inicio, hora_fin, jornada)
VALUES
(1, '06:00', '14:00', 'Diurna'),
(2, '14:00', '22:00', 'Nocturna'),
(3, '22:00', '06:00', 'Madrugada')
ON CONFLICT (id_turno) DO NOTHING;

-- Insertar estados
INSERT INTO estado (id_estado, "Descripcion")
VALUES 
(1, 'Asignado'),
(2, 'Modificado'),
(3, 'Cancelado')
ON CONFLICT (id_estado) DO NOTHING;

-- Insertar niveles de acceso
INSERT INTO nivel_acceso (id_nivel_acceso, descripcion)
VALUES
(1, 'alto'),
(2, 'medio'),
(3, 'bajo')
ON CONFLICT (id_nivel_acceso) DO NOTHING;

-- Insertar zonas
INSERT INTO zona (id_zona, nombre, nivel_acceso)
VALUES
(1, 'Pista', 1),
(2, 'Torre de Control', 1),
(3, 'Oficinas', 2)
ON CONFLICT (id_zona) DO NOTHING;

-- Insertar accesos
INSERT INTO acceso (id_acceso, id_zona)
VALUES  
(1, 1),
(2, 2),
(3, 3)
ON CONFLICT (id_acceso) DO NOTHING;

-- Insertar tarjetas de acceso
INSERT INTO tarjeta_acceso (id_tarjeta, serial, fecha_expedicion, vencimiento, id_empleado, nivel_acceso)
VALUES
(1, 'ABC123', '2025-01-01', '2026-01-01', 1, 1)
ON CONFLICT (id_tarjeta) DO NOTHING;

-- Insertar estados de validación
INSERT INTO estado_validacion (id_estado_validacion, descripcion)
VALUES 
(1, 'aprobado'),
(2, 'negado')
ON CONFLICT (id_estado_validacion) DO NOTHING;

-- ========== DATOS RELACIONADOS ==========
-- Insertar asignación de turnos
INSERT INTO asignacion_turno (id_asignacion, id_empleado, id_turno, observaciones, fecha, estado)
VALUES
(11, 1, 1, 'NN', '2025-05-30', 1),
(22, 2, 2, 'NN', '2025-05-31', 1),
(33, 3, 3, 'NN', '2025-06-01', 1)
ON CONFLICT (id_asignacion) DO NOTHING;

-- Insertar coberturas
INSERT INTO cobertura (id_cobertura, fecha, id_rol, cantidad_turnos, cantidad_empleados_por_turno)
VALUES
(1, '2025-05-25', 1, 2, 2),
(2, '2025-05-25', 2, 1, 1),
(3, '2025-05-26', 3, 1, 1)
ON CONFLICT (id_cobertura) DO NOTHING;

-- Insertar validaciones
INSERT INTO validacion (id_validacion, id_tarjeta, fecha, id_acceso, nivel_requerido, estado_validacion)
VALUES
(1, 1, '2025-05-25', 1, 1, 1),
(2, 1, '2025-05-25', 2, 2, 1)
ON CONFLICT (id_validacion) DO NOTHING;

-- Insertar capacitaciones
INSERT INTO capacitacion (id_capacitacion, nombre, descripcion, duracion)
VALUES
(1, 'Curso de Seguridad', 'Capacitación en protocolos de seguridad', 4),
(2, 'Mantenimiento Equipos', 'Revisión y mantenimiento de sistemas', 6),
(3, 'Gestión de Recursos', 'Administración eficiente del personal', 3)
ON CONFLICT (id_capacitacion) DO NOTHING;

-- Insertar capacitación asignada a empleados
INSERT INTO empleado_capacitacion (id_empleado, id_capacitacion, fecha_inicio, fecha_fin, vencimiento)
VALUES
(1, 1, '2025-01-01', '2025-01-05', '2026-01-01'),
(2, 2, '2025-01-10', '2025-01-14', '2026-01-10'),
(3, 3, '2025-02-01', '2025-02-04', '2026-02-01');

-- Insertar asistencia
INSERT INTO asistencia (id_asistencia, id_empleado, id_tarjeta, hora_inicio, hora_fin)
VALUES
(1, 1, 1, '06:00', '14:00')
ON CONFLICT (id_asistencia) DO NOTHING;

-- Insertar evaluaciones de rendimiento
INSERT INTO rendimiento (id_evaluacion, id_empleado, puntualidad, eficiencia, manejo_situaciones)
VALUES
(1, 1, 9, 8, 9)
ON CONFLICT (id_evaluacion) DO NOTHING;

-- Insertar tipos de licencia
INSERT INTO licencia (id_licencia, tipo)
VALUES
(1, 'Vacaciones'),
(2, 'Permiso Médico'),
(3, 'Permiso Personal')
ON CONFLICT (id_licencia) DO NOTHING;

-- Insertar solicitudes de licencia
INSERT INTO solicitud_licencia (id_solicitud, id_empleado, id_licencia, fecha_inicio, fecha_fin, estado, motivo, fecha_solicitud, aprobado_por)
VALUES 
(1, 1, 1, '2025-06-01', '2025-06-15', 'Aprobado',  'Vacaciones anuales',    '2025-05-20', 'Jefe de RRHH'),
(2, 2, 2, '2025-06-05', '2025-06-10', 'Aprobado',  'Reposo por enfermedad', '2025-05-21', 'Jefe de RRHH'),
(3, 3, 3, '2025-06-20', '2025-06-22', 'Pendiente', 'Asunto familiar', 	   '2025-05-22', 'Jefe de RRHH')
ON CONFLICT (id_solicitud) DO NOTHING;

-- Insertar comunicaciones internas
INSERT INTO comunicacion_interna (id_comunicacion, fecha, asunto, contenido, remitente, destinatario_empleado, destinatario_departamento, tipo_destinatario)
VALUES
(1, '2025-05-25', 'Cambio de Turno', 'El turno de noche ha sido modificado.', 1, 1, NULL, 'empleado'),
(2, '2025-05-25', 'Recordatorio de capacitación', 'Asistir al curso de seguridad esta semana.', 2, 2, NULL, 'empleado'),
(3, '2025-05-25', 'Emergencia en pista', 'Evacuar inmediatamente.', 3, NULL, 1, 'departamento')
ON CONFLICT (id_comunicacion) DO NOTHING;

-- Insertar historial de los empleados
INSERT INTO historial_empleado (id_historial, id_empleado, id_rol, id_departamento, fecha_inicio, fecha_fin)
VALUES (1, 1, 1, 1, '2024-01-01', NULL),  -- este empleado tiene un rol activo
	   (2, 2, 2, 2, '2024-02-01', NULL),
	   (3, 3, 3, 3, '2024-03-15', NULL);