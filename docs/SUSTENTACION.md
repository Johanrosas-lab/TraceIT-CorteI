# Guion de sustentación - TraceIT (10 minutos)

## 1. Problema y modelo de datos (aprox. 5 minutos)

**Inicio**
TraceIT nace de un problema frecuente en mesas de ayuda pequeñas: los incidentes de soporte pueden quedar dispersos y perder seguimiento. El primer objetivo es centralizar los casos en una aplicación web sencilla.

**Usuario objetivo**
Estudiantes, docentes y personal de TI que necesitan registrar y hacer seguimiento a solicitudes de soporte.

**Alcance del Corte I**
El Corte I implementa la base del sistema. Todavía no se automatizan diagnósticos con IA. La IA se usa como asistente de desarrollo y su uso queda documentado en la bitácora.

**Modelo de datos**
- `User 1:N Ticket`: un usuario puede tener varios tickets.
- `Category 1:N Ticket`: una categoría puede agrupar varios tickets.
- `Ticket` guarda `user_id` y `category_id` como llaves foráneas.

Explicar por qué no es una cadena Usuario → Ticket → Categoría, sino dos relaciones independientes hacia Ticket.

## 2. Demostración del CRUD

1. Abrir el listado de tickets.
2. Crear un ticket nuevo.
3. Mostrar el ticket creado.
4. Editarlo y cambiar su estado a `En proceso` o `Resuelto`.
5. Regresar al listado y comprobar el cambio.
6. Eliminar un ticket de prueba.

## 3. Preguntas individuales sobre el código

Archivos que debes saber explicar:

- `traceit/models.py`: entidades y relaciones.
- `traceit/routes.py`: rutas del CRUD, validación y operaciones con la base de datos.
- `traceit/templates/`: interfaz HTML.
- `traceit/__init__.py`: configuración y creación de la base SQLite.

## Cambio pequeño recomendado para practicar

Agregar un nuevo estado llamado `En espera`:

1. Abrir `traceit/routes.py`.
2. Cambiar:

```python
STATUSES = ("Abierto", "En proceso", "Resuelto")
```

por:

```python
STATUSES = ("Abierto", "En proceso", "En espera", "Resuelto")
```

3. Guardar y reiniciar Flask.
4. Verificar que el nuevo estado aparezca en el formulario y en el filtro.

Este cambio permite demostrar que entiendes cómo una constante del backend alimenta la interfaz.
