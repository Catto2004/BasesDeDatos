-- Consultas: Proyecto Aeropuerto

-- Consulta 1:
-- Empleados y su rol actual.
SELECT 
    e.id_empleado, 
    e.nombres, 
    e.apellidos, 
    r.nombre_rol, 
    d.nombre AS departamento
FROM empleado e
JOIN historial_empleado h ON e.id_empleado = h.id_empleado
JOIN rol r ON h.id_rol = r.id_rol
JOIN departamento d ON h.id_departamento = d.id_departamento

-- Consulta 2:
-- Turnos asignados con nombres de empleados y estado.
SELECT 
    a.fecha, 
    t.jornada, 
    t.hora_inicio, 
    t.hora_fin,
    e.nombres || ' ' || e.apellidos AS empleado,
    es."Descripcion" AS estado
FROM asignacion_turno a
JOIN turno t ON a.id_turno = t.id_turno
JOIN empleado e ON a.id_empleado = e.id_empleado
JOIN estado es ON a.estado = es.id_estado;

-- Consulta 3:
-- Validaciones de acceso con resultado.
SELECT e.nombres || ' ' || e.apellidos AS empleado,
       z.nombre AS zona, v.fecha, ev.descripcion AS estado_validacion
FROM validacion v
JOIN tarjeta_acceso t ON v.id_tarjeta = t.id_tarjeta
JOIN empleado e ON t.id_empleado = e.id_empleado
JOIN acceso a ON v.id_acceso = a.id_acceso
JOIN zona z ON a.id_zona = z.id_zona
JOIN estado_validacion ev ON v.estado_validacion = ev.id_estado_validacion;

-- Consulta 4:
-- Capacitaciones por empleado.
SELECT e.nombres || ' ' || e.apellidos AS empleado, c.nombre AS curso,
       ec.fecha_inicio, ec.fecha_fin, ec.vencimiento
FROM empleado_capacitacion ec
JOIN empleado e ON ec.id_empleado = e.id_empleado
JOIN capacitacion c ON ec.id_capacitacion = c.id_capacitacion;

-- Consulta 5:
-- Solicitudes de licencia con tipo y estado.
SELECT e.nombres || ' ' || e.apellidos AS empleado,
       l.tipo AS tipo_licencia,
       s.fecha_inicio, s.fecha_fin, s.estado, s.aprobado_por
FROM solicitud_licencia s
JOIN empleado e ON s.id_empleado = e.id_empleado
JOIN licencia l ON s.id_licencia = l.id_licencia;



