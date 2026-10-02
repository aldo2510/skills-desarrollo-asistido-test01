# Step 2 — Convierte el requerimiento en un plan

## Objetivo
Aprende a transformar una necesidad funcional en cambios concretos, criterios de aceptación, pruebas y riesgos.

## Requerimiento
Agregar priority a las tareas. Solo se permiten low, medium y high. El valor es obligatorio al crear una tarea y debe aparecer al consultar tareas.

## 1. Prompt exacto para Copilot
~~~text
Analiza el requerimiento de priority y el código actual.

No modifiques ningún archivo.

Crea un plan técnico que incluya:
1. requerimiento funcional;
2. estado actual;
3. archivos que deben modificarse;
4. archivos que deben crearse;
5. cambios en Task;
6. cambios en TaskCreate;
7. cambios en POST /tasks;
8. cambios en GET /tasks;
9. pruebas necesarias;
10. criterios de aceptación;
11. riesgos;
12. estrategia de rollback.

No escribas código.
~~~

## 2. Crea docs/implementation-plan.md
~~~markdown
# Implementation Plan

## 1. Requerimiento
Agregar priority a las tareas con valores permitidos low, medium y high. El campo es obligatorio al crear y debe devolverse en las respuestas.

## 2. Estado actual
La API tiene Task, TaskCreate, POST /tasks y GET /tasks. Las tareas se almacenan en memoria.

## 3. Impacto técnico
| Componente | Cambio | Motivo |
|---|---|---|
| Task | Agregar priority | Exponer prioridad |
| TaskCreate | Agregar priority obligatoria | Validar entrada |
| POST /tasks | Persistir priority | Conservar dato recibido |
| GET /tasks | Devolver priority | Exponer dato |
| Tareas iniciales | Asignar priority válida | Mantener contrato |
| Tests | Cubrir valores y obligatoriedad | Evitar regresiones |

## 4. Archivos a modificar
- app/main.py
- tests/test_api.py

## 5. Archivos a crear
- tests/test_priority.py
- docs/test-strategy.md
- docs/implementation-review.md

## 6. Alternativas
Alternativa A: validar priority en el modelo de entrada.
Alternativa B: validar manualmente dentro del endpoint.

## 7. Criterios de aceptación
- low, medium y high son válidos.
- Un valor fuera del conjunto es rechazado.
- Omitir priority al crear es rechazado.
- POST conserva priority.
- GET devuelve priority.
- Las pruebas existentes siguen pasando.

## 8. Riesgos
- Romper clientes que no envíen el nuevo campo.
- Introducir validación inconsistente.
- Modificar comportamiento existente fuera del alcance.

## 9. Rollback
Revertir el commit que introduce priority y ejecutar nuevamente pytest.

## 10. Evidencia
El plan debe contrastarse con app/main.py y tests/test_api.py antes de implementarlo.
~~~

## 3. Verificación
~~~bash
test -f docs/implementation-plan.md
grep -Eiq 'low|medium|high' docs/implementation-plan.md
grep -Eiq 'POST /tasks|GET /tasks|Task' docs/implementation-plan.md
grep -Eiq 'criterios|aceptaci' docs/implementation-plan.md
grep -Eiq 'riesgo|rollback' docs/implementation-plan.md
~~~

## 4. Commit
~~~bash
git add docs/implementation-plan.md
git commit -m "docs: create implementation plan"
git push
~~~
**Tiempo sugerido: 10–12 min.**