## Step 2: Convierte el requerimiento en un plan

### Teoría: de requerimiento a diseño técnico

Un requerimiento funcional describe **qué necesita el usuario**; un plan técnico explica **qué partes del sistema deben cambiar para cumplirlo**.

Una buena planificación conecta:

```
Requerimiento → impacto → alternativas → criterios de aceptación → pruebas → implementación
```

La planificación es importante porque permite detectar cambios innecesarios, riesgos y pruebas faltantes **antes de modificar el código**.

En este laboratorio no necesitas inventar el plan desde cero. El documento que crearás ya contiene una propuesta base. Tu trabajo consiste en:

1. entender por qué se propone cada cambio;
2. contrastarlo con el código real;
3. utilizar Copilot para revisar la propuesta;
4. registrar cualquier diferencia que encuentres;
5. decidir qué información debe quedar bajo control humano.

### Requerimiento

Agregar prioridad a las tareas.

Reglas:

- valores permitidos: `low`, `medium`, `high`;
- la prioridad es obligatoria al crear una tarea;
- `GET /tasks` debe devolver la prioridad;
- las pruebas deben cubrir los nuevos escenarios;
- no cambiar funcionalidades que no estén relacionadas.

---

## 1. Revisa el requerimiento

Antes de usar Copilot, lee el requerimiento y comprueba que entiendes estas condiciones:

| Requisito | Qué significa |
|---|---|
| `low`, `medium`, `high` | No se deben aceptar otros valores |
| Obligatoria al crear | `POST /tasks` debe rechazar una solicitud sin prioridad |
| Visible en `GET /tasks` | Las tareas devueltas deben incluir `priority` |
| Nuevas pruebas | Deben existir pruebas para valores válidos e inválidos |
| Sin cambios no relacionados | No modificar endpoints o comportamientos que no formen parte del requisito |

---

## 2. Compara el requerimiento con el código actual

Revisa directamente:

- `app/main.py`
- `tests/test_api.py`
- `requirements.txt`

Identifica qué partes del código están relacionadas con:

- `Task`;
- `TaskCreate`;
- `POST /tasks`;
- `GET /tasks`;
- pruebas existentes.

No modifiques código en este paso.

---

## 3. Compara el análisis con Copilot

Ahora utiliza Copilot para comprobar si tu comprensión coincide con la interpretación de la IA.

Copia y pega este prompt:

```text
Analiza este proyecto FastAPI y el requerimiento descrito a continuación.

Requerimiento:
- agregar un campo priority a las tareas;
- priority solo puede ser low, medium o high;
- priority es obligatoria al crear una tarea;
- GET /tasks debe devolver priority;
- debemos agregar pruebas para los nuevos escenarios;
- no debemos cambiar funcionalidades no relacionadas.

No modifiques ningún archivo.

Explica:
1. qué archivos actuales están involucrados;
2. qué componentes deberían cambiar;
3. qué pruebas nuevas serían necesarias;
4. qué riesgos o problemas de compatibilidad existen;
5. qué alternativa de implementación propondrías.

Termina con:
- 3 afirmaciones que yo debería verificar directamente en el repositorio;
- 1 posible interpretación incorrecta que podría cometer un desarrollador.

No escribas código.
```

Lee la respuesta de Copilot y compárala con el código real.

---

## 4. Crea el documento

Crea:

`docs/implementation-plan.md`

**No necesitas inventar el contenido. Copia y pega exactamente esta plantilla completa:**

```markdown
# Implementation Plan

## 1. Requerimiento

Agregar un campo `priority` a las tareas.

Reglas funcionales:

- `priority` debe aceptar únicamente `low`, `medium` o `high`.
- `priority` es obligatoria al crear una tarea.
- `GET /tasks` debe devolver `priority`.
- Las pruebas deben cubrir los nuevos escenarios.
- No se deben modificar funcionalidades que no estén relacionadas con este requerimiento.

## 2. Estado actual

### Task

Actualmente representa una tarea con:

- `id`: identificador numérico.
- `title`: título de la tarea.
- `completed`: indica si la tarea está completada.

### TaskCreate

Actualmente recibe:

- `title`: título de la nueva tarea.

### POST /tasks

Crea una nueva tarea a partir de `TaskCreate`.

Actualmente genera el ID y agrega la tarea a la lista en memoria.

### GET /tasks

Devuelve la lista actual de tareas.

### Validaciones actuales

FastAPI y Pydantic realizan la validación de los modelos definidos en `app/main.py`.

El código actual no tiene una validación específica para un campo `priority`, porque todavía no existe.

### Pruebas actuales

Las pruebas utilizan `pytest` y `FastAPI TestClient`.

Las pruebas existentes cubren:

- `GET /health`;
- `GET /tasks`;
- `POST /tasks`;
- `PATCH /tasks/{task_id}`.

## 3. Impacto técnico

| Componente | Cambio | Motivo |
|---|---|---|
| `Task` | Agregar `priority` | Las tareas deben exponer su prioridad |
| `TaskCreate` | Agregar `priority` obligatoria | El cliente debe proporcionar prioridad al crear |
| `POST /tasks` | Recibir y conservar `priority` | La prioridad debe almacenarse en la tarea |
| `GET /tasks` | Devolver `priority` | El consumidor debe poder consultar la prioridad |
| Pruebas | Agregar escenarios de prioridad | Verificar valores válidos, inválidos y ausentes |

## 4. Archivos a modificar

- `app/main.py`
- `tests/test_api.py`

## 5. Archivos a crear

No es obligatorio crear archivos adicionales para implementar el requerimiento.

Las nuevas pruebas pueden incorporarse al archivo existente:

`tests/test_api.py`

## 6. Alternativas

### Alternativa A — Validación mediante Pydantic

Descripción:

Definir `priority` en el modelo y restringir sus valores permitidos mediante las capacidades de validación del modelo.

Ventajas:

- la validación queda cerca del modelo;
- FastAPI puede devolver automáticamente errores de validación;
- evita duplicar validaciones en cada endpoint.

Riesgos:

- una modificación incorrecta del modelo puede afectar las solicitudes existentes;
- hay que verificar el comportamiento de las respuestas de validación.

### Alternativa B — Validación manual en el endpoint

Descripción:

Recibir el valor y comprobar manualmente que pertenece al conjunto permitido dentro del endpoint.

Ventajas:

- la regla es explícita en el flujo del endpoint;
- puede resultar sencilla para una implementación pequeña.

Riesgos:

- puede duplicarse la lógica;
- otros endpoints podrían olvidar aplicar la misma regla;
- la validación queda más acoplada a la implementación del endpoint.

## 7. Decisión

### Opción propuesta

Utilizar validación en el modelo de entrada mediante Pydantic.

### Motivo

La regla de valores permitidos pertenece al contrato de entrada de la API. Mantenerla en el modelo permite que FastAPI valide automáticamente las solicitudes antes de ejecutar la lógica del endpoint.

### Qué recomendó Copilot

Registrar aquí la recomendación concreta obtenida de Copilot después de comparar su respuesta con este plan.

Ejemplo:

> Copilot recomendó validar `priority` en el modelo porque forma parte del contrato de entrada.

### Qué decidí yo

Escribir aquí la decisión final después de revisar la recomendación de Copilot y contrastarla con el código real.

## 8. Criterios de aceptación

- [ ] `low` funciona.
- [ ] `medium` funciona.
- [ ] `high` funciona.
- [ ] Un valor diferente de `low`, `medium` o `high` es rechazado.
- [ ] Una solicitud sin `priority` es rechazada.
- [ ] Una tarea creada conserva su `priority`.
- [ ] `GET /tasks` devuelve `priority`.
- [ ] Las funcionalidades existentes continúan funcionando.
- [ ] Las pruebas existentes continúan pasando.
- [ ] Existen pruebas para los nuevos escenarios.

## 9. Estrategia de pruebas

| Escenario | Tipo | Resultado esperado |
|---|---|---|
| Crear con `low` | Prueba de API | HTTP 201 y `priority=low` |
| Crear con `medium` | Prueba de API | HTTP 201 y `priority=medium` |
| Crear con `high` | Prueba de API | HTTP 201 y `priority=high` |
| Crear con valor inválido | Prueba de validación | Solicitud rechazada |
| Crear sin `priority` | Prueba de validación | Solicitud rechazada |
| Consultar `GET /tasks` | Prueba de API | Cada tarea devuelve `priority` |
| Pruebas existentes | Regresión | Continúan pasando |

## 10. Compatibilidad

El cambio modifica el contrato de creación de tareas porque `priority` será obligatoria.

Por esta razón, las solicitudes existentes a `POST /tasks` que no envíen `priority` deberán considerarse incompatibles con el nuevo contrato.

Los endpoints que no están relacionados con la creación o consulta de tareas deben mantener su comportamiento actual.

## 11. Riesgos y mitigaciones

### Riesgo 1 — Romper las pruebas existentes

Mitigación:

Actualizar las solicitudes de prueba de creación para proporcionar una prioridad válida y ejecutar toda la suite después del cambio.

### Riesgo 2 — Aceptar valores de prioridad no permitidos

Mitigación:

Validar explícitamente los valores permitidos y agregar pruebas para valores inválidos.

### Riesgo 3 — Olvidar devolver priority

Mitigación:

Agregar una prueba específica para `GET /tasks`.

### Riesgo 4 — Introducir cambios fuera del alcance

Mitigación:

Revisar el diff antes del commit y comprobar que únicamente se modificaron archivos relacionados con el requerimiento.

## 12. Rollback

Si la implementación provoca regresiones, revertir el commit que introduce el cambio de prioridad.

Antes de hacer rollback se debe identificar qué pruebas o funcionalidades fueron afectadas.

## 13. Orden de implementación

1. Modificar el modelo `Task`.
2. Modificar el modelo `TaskCreate`.
3. Ajustar `POST /tasks`.
4. Ajustar los datos iniciales para incluir prioridad.
5. Actualizar las pruebas existentes.
6. Agregar pruebas para valores válidos.
7. Agregar pruebas para valores inválidos y ausencia de prioridad.
8. Ejecutar toda la suite de pruebas.
9. Revisar el diff.
10. Documentar la decisión técnica.

## 14. Decisiones humanas

La IA puede proponer una implementación, pero la decisión final debe ser revisada por la persona que mantiene el proyecto.

Registrar aquí:

- qué propuesta de Copilot fue aceptada;
- qué propuesta fue descartada;
- por qué;
- qué supuestos fueron verificados manualmente.

## 15. Evidencia de revisión

Registrar aquí:

- archivos revisados;
- comandos ejecutados;
- resultado de las pruebas;
- diferencias encontradas entre el análisis humano y Copilot;
- cambios aprobados.

## 16. Pregunta de revisión

Antes de implementar, responder:

**¿La solución propuesta modifica únicamente lo necesario para agregar `priority` sin cambiar el comportamiento de las funcionalidades que están fuera del alcance?**

Respuesta:

> Escribir aquí la respuesta después de revisar el plan y el código.

```

---

## 5. Verificación con Copilot

Después de crear el archivo, puedes utilizar este prompt para contrastar el plan:

```text
Revisa docs/implementation-plan.md contra el requerimiento original.

No modifiques archivos.

Devuelve una tabla con:
- requisito;
- dónde está cubierto en el plan;
- evidencia en el código;
- qué falta.

Después indica:
1. si existe algún cambio innecesario;
2. si falta alguna prueba;
3. si existe algún riesgo importante que no esté documentado.

No escribas código.
```

Si Copilot encuentra una diferencia, **no aceptes automáticamente su propuesta**. Comprueba primero el código y decide si realmente corresponde.

## 6. Verificación final

Ejecuta:

```bash
test -f docs/implementation-plan.md
grep -q "priority" docs/implementation-plan.md
grep -q "Criterios de aceptación" docs/implementation-plan.md
```

Si los tres comandos terminan correctamente, el documento está creado y contiene los elementos mínimos del plan.

Finalmente ejecuta:

```bash
pytest -q
```

En este paso todavía no deberías haber implementado `priority`, por lo que las pruebas existentes deben continuar pasando.

## 7. Commit y push

Cuando hayas terminado:

```bash
git add docs/implementation-plan.md
git commit -m "docs: create implementation plan"
git push
```

El objetivo de este Step es que exista un **plan técnico verificable antes de comenzar la implementación**.

**Tiempo: 15-17 min.**
