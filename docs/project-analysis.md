# Project Analysis

## 1. Arquitectura

| Archivo | Responsabilidad |
|---|---|
| app/main.py | Contiene la aplicación FastAPI, los modelos Task y TaskCreate, la lista en memoria y los endpoints de la API. |
| app/__init__.py | Identifica `app` como un paquete Python. |
| tests/test_api.py | Contiene las pruebas automatizadas de los endpoints principales. |
| requirements.txt | Define las dependencias Python necesarias para ejecutar la aplicación y sus pruebas. |
| pytest.ini | Configura pytest para incluir el directorio raíz del proyecto en el path de importación. |

## 2. Endpoints

| Método | Endpoint | Entrada | Respuesta |
|---|---|---|---|
| GET | /health | Sin parámetros | `{"status": "ok"}` |
| GET | /tasks | Sin parámetros | Lista de tareas |
| POST | /tasks | JSON con `title` | Nueva tarea con `id`, `title` y `completed` |
| PATCH | /tasks/{task_id} | ID de la tarea en la URL | Tarea actualizada con `completed=true` |

## 3. Modelos

### Task

Representa una tarea existente.

- `id`: identificador entero.
- `title`: título de la tarea.
- `completed`: indica si la tarea está completada. Por defecto es `false`.

### TaskCreate

Representa los datos necesarios para crear una tarea.

- `title`: título de la nueva tarea.

## 4. Persistencia actual

La aplicación utiliza una lista Python llamada `tasks` como almacenamiento en memoria.

No existe una base de datos.

Esto significa que los datos se pierden cuando se reinicia la aplicación.

## 5. Ejecución de pruebas

Comando utilizado:

```bash
pytest -q
```

Resultado esperado:

```text
4 passed
```

## 6. Riesgos o decisiones técnicas

1. La información se almacena únicamente en memoria, por lo que no existe persistencia entre reinicios.
2. La generación del ID depende de los IDs existentes en la lista de tareas.
3. Los cambios realizados directamente sobre la lista global afectan el estado compartido de la aplicación durante la ejecución.
4. Las pruebas utilizan FastAPI TestClient y no requieren levantar un servidor HTTP real.

## 7. Lo que Copilot dijo vs. lo que verifiqué

La respuesta de Copilot se utilizó como apoyo para comprender el proyecto y se contrastó con el código real del repositorio.

| Afirmación | Cómo la verifiqué | Resultado |
|---|---|---|
| La aplicación utiliza FastAPI | Revisé `app/main.py` | Confirmado |
| Las tareas se almacenan en memoria | Revisé la variable `tasks` | Confirmado |
| Existen cuatro endpoints principales | Revisé las funciones decoradas con `@app.get`, `@app.post` y `@app.patch` | Confirmado |

## 8. Información de Copilot verificada manualmente

- Copilot puede acelerar la lectura inicial del proyecto.
- La información generada por IA debe contrastarse con los archivos reales.
- La fuente definitiva para este ejercicio es el código del repositorio.

## 9. Pregunta técnica abierta

¿Qué cambios serían necesarios para agregar un nuevo campo `priority` a las tareas sin romper los endpoints ni las pruebas existentes?