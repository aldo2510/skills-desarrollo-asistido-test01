# Step 5 — Prepara el Pull Request

## Teoría
Un PR debe permitir que otra persona entienda qué cambió, por qué cambió y cómo verificarlo.

## 1. Prompt exacto
~~~text
Revisa git diff y el requerimiento original.

Genera una descripción de Pull Request en español con:
1. objetivo;
2. cambios;
3. pruebas;
4. riesgos;
5. cómo validar;
6. rollback.

No modifiques archivos.
~~~

## 2. Crea docs/pr-description.md
~~~markdown
# Pull Request

## Objetivo
Agregar priority a las tareas sin romper la API existente.

## Cambios
- Se incorporó priority al modelo de tarea.
- Se incorporó priority al modelo de creación.
- Se actualizaron los endpoints necesarios.
- Se agregaron pruebas.
- Se documentó una corrección de generación de ID.

## Pruebas
~~~bash
pytest -q
~~~

## Riesgos
- Clientes antiguos que no envíen priority.
- Cambios de contrato que deben verificarse antes del despliegue.

## Validación
Revisar git diff y ejecutar toda la suite.

## Rollback
Revertir el commit del cambio y ejecutar pytest.
~~~

## 3. Crea una rama
~~~bash
git checkout -b feat/task-priority
git status
~~~

Si tus cambios ya están en main, crea la rama antes de continuar y asegúrate de que el PR se origine desde esa rama.

## 4. Commit y push
~~~bash
git add .
git commit -m "feat: task priority and validation"
git push -u origin feat/task-priority
~~~

## 5. Abre el Pull Request
Crea un PR hacia main usando docs/pr-description.md como descripción.

No hagas merge.

## 6. Verificación
~~~bash
test -f docs/pr-description.md
test -f docs/debugging-notes.md
test -f tests/test_empty_tasks.py
pytest -q
~~~

**Tiempo sugerido: 8–10 min.**