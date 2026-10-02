# Step 1 — Analiza el proyecto

## Objetivo
Antes de modificar un sistema con IA, establece una línea base. En este Step solo observarás, preguntarás a Copilot y verificarás. No modifiques código.

## 1. Revisa el proyecto
~~~bash
find . -maxdepth 3 -type f | sort
sed -n '1,240p' app/main.py
sed -n '1,240p' tests/test_api.py
cat requirements.txt
~~~

## 2. Prompt exacto para Copilot
~~~text
Analiza este proyecto FastAPI como un ingeniero senior.

No modifiques ningún archivo y no escribas código.

Explícame:
1. La responsabilidad de cada archivo relevante.
2. Los endpoints disponibles, método HTTP, entrada y respuesta.
3. Los modelos Task y TaskCreate y sus campos.
4. Cómo se almacenan actualmente las tareas.
5. Cómo funcionan las pruebas.
6. El flujo completo de POST /tasks.
7. El flujo completo de PATCH /tasks/{task_id}.
8. Al menos 2 riesgos o decisiones técnicas que debo conocer antes de modificar el proyecto.

Termina con una sección llamada "Lo que Copilot dijo vs. lo que debo verificar" con al menos 3 verificaciones concretas.

No escribas código.
No hagas cambios.
~~~

## 3. Crea docs/project-analysis.md
~~~markdown
# Project Analysis

## 1. Arquitectura
| Archivo | Responsabilidad |
|---|---|
| app/main.py | Aplicación FastAPI, modelos, estado y endpoints |
| tests/test_api.py | Pruebas de la API |
| requirements.txt | Dependencias Python |

## 2. Endpoints
| Método | Endpoint | Entrada | Respuesta |
|---|---|---|---|
| GET | /health | Ninguna | Estado |
| GET | /tasks | Ninguna | Lista de tareas |
| POST | /tasks | TaskCreate | Nueva tarea |
| PATCH | /tasks/{task_id} | ID | Tarea actualizada |

## 3. Modelos
### Task
- id
- title
- completed

### TaskCreate
- title

## 4. Persistencia actual
Las tareas se almacenan en memoria mediante la lista global tasks. No existe una base de datos y los datos se pierden al reiniciar el proceso.

## 5. Pruebas
El proyecto utiliza pytest y FastAPI TestClient.

## 6. Flujo de POST /tasks
1. Recibe TaskCreate.
2. Valida la entrada.
3. Calcula el nuevo ID.
4. Crea Task.
5. Agrega la tarea a la lista.
6. Devuelve la tarea.

## 7. Flujo de PATCH /tasks/{task_id}
1. Recibe el ID.
2. Busca la tarea.
3. Marca completed como true.
4. Devuelve la tarea.
5. Si no existe, devuelve 404.

## 8. Riesgos
1. La información se pierde al reiniciar.
2. El ID depende del estado actual de la lista.
3. La lista global representa estado compartido durante la ejecución.
4. Las pruebas dependen del estado inicial del módulo.

## 9. Lo que Copilot dijo vs. lo que verifiqué
| Afirmación | Verificación | Resultado |
|---|---|---|
| La aplicación utiliza FastAPI | Revisé app/main.py | Confirmado |
| Las tareas están en memoria | Revisé la variable tasks | Confirmado |
| Existen cuatro endpoints | Revisé las rutas | Confirmado |

## 10. Conclusión
La aplicación es una API FastAPI pequeña con almacenamiento en memoria y pruebas automatizadas. La IA se utilizó como apoyo y el código real del repositorio fue la fuente de verificación.
~~~

## 4. Verificación
~~~bash
test -f docs/project-analysis.md
pytest -q
~~~

## 5. Commit
~~~bash
git add docs/project-analysis.md
git commit -m "docs: analyze project"
git push
~~~
**Tiempo sugerido: 10–12 min.**