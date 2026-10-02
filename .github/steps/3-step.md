# Step 3 — Implementa, compara y decide

## Teoría
El objetivo no es aceptar código generado. El ciclo es:

~~~text
Plan → IA implementa → diff → pruebas → comparación → decisión humana → evidencia
~~~

## 1. Prompt exacto para Copilot Agent
~~~text
Implementa el requerimiento descrito en docs/implementation-plan.md.

Agrega priority a Task y TaskCreate.
Solo permite low, medium y high.
Haz priority obligatoria al crear.
POST /tasks debe conservarla.
GET /tasks debe devolverla.
Las tareas iniciales deben tener un valor válido.
Agrega pruebas para valores válidos, valor inválido, ausencia del campo y persistencia en POST.
Mantén las funcionalidades existentes.

Antes de modificar archivos revisa app/main.py, tests/test_api.py y docs/implementation-plan.md.
Después ejecuta pytest -q y muestra los archivos modificados.
No agregues dependencias nuevas.
~~~

Después ejecuta:
~~~bash
git diff
pytest -q
~~~

## 2. Crea tests/test_priority.py
~~~python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_priority_is_returned_by_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert all(task["priority"] in {"low", "medium", "high"} for task in response.json())

def test_create_task_with_priority():
    response = client.post("/tasks", json={"title": "Priority test", "priority": "high"})
    assert response.status_code == 201
    assert response.json()["priority"] == "high"

def test_create_task_rejects_invalid_priority():
    response = client.post("/tasks", json={"title": "Invalid", "priority": "urgent"})
    assert response.status_code == 422

def test_create_task_requires_priority():
    response = client.post("/tasks", json={"title": "Missing priority"})
    assert response.status_code == 422
~~~

## 3. Crea docs/test-strategy.md
~~~markdown
# Test Strategy

## Objetivo
Comprobar que priority forma parte del contrato de la API sin romper funcionalidades existentes.

## Casos
| Caso | Resultado esperado |
|---|---|
| low | 201 |
| medium | 201 |
| high | 201 |
| urgent | 422 |
| priority ausente | 422 |
| GET /tasks | Cada tarea tiene priority |
| Tests existentes | Todos pasan |

## Ejecución
~~~bash
pytest -q
~~~

## Criterio de salida
No continuar mientras exista una prueba fallida.
~~~

## 4. Crea docs/implementation-review.md
~~~markdown
# Implementation Review

## Implementación
La solución implementa priority en los modelos y conserva el dato en los endpoints.

## Alternativa
La alternativa considerada es validar manualmente dentro de POST /tasks.

## Comparación
| Criterio | Modelo | Endpoint |
|---|---|---|
| Claridad | Contrato centralizado | Regla dentro de endpoint |
| Mantenibilidad | Menor duplicación | Mayor riesgo de duplicación |
| Validación | Automática por modelo | Manual |
| Extensibilidad | Más fácil reutilizar | Más acoplamiento |

## Decisión humana
Se mantiene la validación en el modelo porque la regla pertenece al contrato de entrada.

## Evidencia
Se revisó el diff y se ejecutó pytest -q.
~~~

## 5. Revisión con Copilot
~~~text
Revisa la implementación de priority, tests/test_priority.py y docs/implementation-review.md.

No modifiques archivos.

Comprueba que:
1. los requisitos estén cubiertos;
2. las pruebas correspondan al comportamiento real;
3. no haya cambios fuera de alcance;
4. la decisión técnica esté respaldada por evidencia.

Devuelve hallazgos y verificaciones faltantes. No escribas código.
~~~

## 6. Validación
~~~bash
test -f docs/implementation-review.md
test -f docs/test-strategy.md
test -f tests/test_priority.py
pytest -q
~~~

## 7. Commit
~~~bash
git add app tests docs
git commit -m "feat: add task priority"
git push
~~~
**Tiempo sugerido: 18–22 min.**