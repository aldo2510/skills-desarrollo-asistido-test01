# Step 4 — Diseña una estrategia de pruebas y depura con evidencia

## Teoría
Una prueba demuestra comportamiento. Una depuración demuestra causa. No aceptes una explicación de IA sin reproducir el problema.

## 1. Prompt para diseñar pruebas
~~~text
Revisa la implementación actual de priority.

No modifiques archivos.

Identifica qué comportamientos deben probarse y qué casos límite podrían fallar.
Relaciona cada caso con un endpoint y un resultado HTTP esperado.
No escribas código.
~~~

## 2. Crea docs/test-strategy.md
~~~markdown
# Test Strategy

## Objetivo
Validar el contrato de priority y preservar el comportamiento existente.

## Matriz
| Caso | Entrada | Esperado |
|---|---|---|
| low | priority=low | 201 |
| medium | priority=medium | 201 |
| high | priority=high | 201 |
| inválida | priority=urgent | 422 |
| ausente | sin priority | 422 |
| listado | GET /tasks | priority presente |
| regresión | suite existente | todo pasa |

## Evidencia
Comando:
~~~bash
pytest -q
~~~

La salida real de pytest debe revisarse antes de continuar.
~~~

## 3. Depura el caso de lista vacía
Primero reproduce la situación:

~~~text
Si el código actual usa max(task.id for task in tasks), una lista vacía puede producir ValueError.
~~~

Pide a Copilot:

~~~text
Analiza app/main.py.

No modifiques archivos todavía.

Determina si la generación del ID funciona cuando tasks está vacía.
Explica si existe una excepción posible, cómo reproducirla y cuál es la causa exacta.
No escribas código.
~~~

## 4. Crea la prueba
Crea tests/test_empty_tasks.py con una prueba que documente el comportamiento esperado de generación de ID cuando no hay tareas. Usa el mismo patrón de TestClient y modifica temporalmente el estado de forma segura.

## 5. Corrige con Copilot
~~~text
Ahora implementa la corrección mínima para que crear una tarea funcione cuando tasks está vacía.

No cambies otros comportamientos.
Agrega o ajusta la prueba que reproduce el problema.
Ejecuta pytest -q.
Explica la causa y la corrección.
~~~

## 6. Crea docs/debugging-notes.md
~~~markdown
# Debugging Notes

## Problema
Generación de ID cuando no existen tareas.

## Síntoma
La operación puede fallar si se calcula el máximo de una colección vacía.

## Causa
La expresión utilizada no contempla correctamente el caso sin elementos.

## Reproducción
La prueba tests/test_empty_tasks.py reproduce el escenario.

## Corrección
Se aplicó el cambio mínimo necesario y se verificó con pytest.

## Evidencia
~~~bash
pytest -q
~~~
~~~

## 7. Verificación
~~~bash
test -f docs/debugging-notes.md
test -f tests/test_empty_tasks.py
grep -Eiq 'causa|reprodu' docs/debugging-notes.md
pytest -q
~~~

## 8. Commit
~~~bash
git add app tests docs
git commit -m "test: cover empty task collection"
git push
~~~
**Tiempo sugerido: 12–15 min.**