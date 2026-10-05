# TraceIT - Corte I

TraceIT es una mesa de ayuda informática desarrollada para el Proyecto Cuatrimestral con IA. En el Corte I se implementa la base funcional del sistema mediante un CRUD completo de tickets conectado a SQLite.

## Autor

Johan Rosas

## Objetivo del Corte I

- Definir el problema y los requisitos del proyecto.
- Modelar los datos con al menos tres entidades.
- Diseñar las pantallas principales.
- Implementar un CRUD funcional de la entidad `Ticket`.
- Mantener una bitácora del uso responsable de Inteligencia Artificial.

## Tecnologías

- Python 3.12 o superior
- Flask 3.x
- Flask-SQLAlchemy 3.x
- SQLite
- HTML5 / CSS3
- Bootstrap 5 por CDN
- Git y GitHub

## Modelo de datos

Entidades principales:

- `User`: persona que reporta o administra solicitudes.
- `Category`: clasificación funcional del incidente.
- `Ticket`: solicitud de soporte. Contiene dos llaves foráneas: `user_id` y `category_id`.

Relaciones:

- Un usuario puede registrar muchos tickets (`User 1:N Ticket`).
- Una categoría puede agrupar muchos tickets (`Category 1:N Ticket`).

El diagrama está disponible en `docs/modelo_er.png`.

## Funcionalidades implementadas

- Listar tickets.
- Filtrar tickets por estado.
- Crear un ticket.
- Consultar el detalle de un ticket.
- Editar un ticket.
- Eliminar un ticket.
- Validar campos obligatorios y valores permitidos.
- Crear automáticamente usuarios y categorías de ejemplo la primera vez que se ejecuta el proyecto.

## Instalación en macOS

```bash
git clone https://github.com/johanr-lab/TraceIT-CorteI.git
cd TraceIT-CorteI
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 run.py
```

Abrir en el navegador:

```text
http://127.0.0.1:5000
```

La base de datos se crea automáticamente en `instance/traceit.db`.

## Pruebas

Con el entorno virtual activo:

```bash
pytest -q
```

Las pruebas cubren el acceso a la pantalla principal y el ciclo crear - editar - eliminar de un ticket.

## Estructura del proyecto

```text
TraceIT-CorteI/
├── run.py
├── requirements.txt
├── README.md
├── traceit/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── static/
│   │   └── css/styles.css
│   └── templates/
│       ├── base.html
│       └── tickets/
│           ├── list.html
│           ├── form.html
│           └── detail.html
├── tests/
│   └── test_app.py
└── docs/
    └── modelo_er.png
```

## Alcance posterior

En cortes posteriores se puede incorporar el componente de IA para apoyar tareas como clasificación automática, resumen de incidentes, recuperación de casos similares y sugerencias de diagnóstico. La IA no reemplaza la decisión del técnico.

## Uso de IA

El uso de IA durante el desarrollo se documenta en la bitácora del Corte I. Se registran los prompts, la respuesta recibida, la decisión tomada y al menos un caso donde una respuesta de la IA fue incompleta y debió corregirse.
