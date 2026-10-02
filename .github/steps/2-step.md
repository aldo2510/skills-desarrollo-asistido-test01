## Step 2: Convierte el requerimiento en un plan

### Teoría: de requerimiento a diseño técnico

Un requerimiento funcional describe **qué necesita el usuario**; un plan técnico explica **qué partes del sistema deben cambiar para cumplirlo**.

Una buena planificación asistida por IA conecta:

```
Requerimiento → impacto → alternativas → criterios de aceptación → pruebas → implementación
```

La ventaja de hacer esto antes de programar es reducir cambios innecesarios y detectar incompatibilidades temprano.

En este laboratorio no necesitas inventar el análisis: usarás prompts preparados y después verificarás el resultado.

### Requerimiento

Agregar prioridad a las tareas.

Reglas:
- valores permitidos: `low`, `medium`, `high`;
- la prioridad es obligatoria al crear una tarea;
- `GET /tasks` debe devolverla;
- las pruebas deben cubrir los nuevos escenarios;
- no cambiar funcionalidades que no estén relacionadas.

### 1. Copia y pega este prompt en Copilot

```text
Analiza el requerimiento de agregar priority a Task.

Requerimiento:
- priority debe aceptar únicamente low, medium o high;
- priority es obligatoria al crear una tarea;
- GET /tasks debe devolver priority;
- debemos agregar pruebas;
- no debemos cambiar funcionalidades no relacionadas.

Inspecciona el repositorio y genera un plan de implementación.
No modifiques archivos.

Incluye:
1. archivos que habría que modificar;
2. archivos que habría que crear;
3. cambios en modelos;
4. cambios en endpoints;
5. estrategia de validación;
6. pruebas necesarias;
7. riesgos;
8. criterios de aceptación;
9. una alternativa de implementación y sus ventajas y riesgos;
10. decisiones que requieren revisión humana.
```

### 2. Pide una revisión del plan

```text
Revisa el plan anterior como arquitecto de software.

No modifiques archivos.

Busca:
- supuestos ocultos;
- cambios innecesarios;
- riesgos de compatibilidad;
- validaciones faltantes;
- pruebas faltantes.

Devuelve una lista concreta de ajustes.
```

### 3. Crea el documento

Crea `docs/implementation-plan.md`.

**Copia esta plantilla:**

```markdown
# Implementation Plan

## 1. Requerimiento
...

## 2. Estado actual
- Task:
- TaskCreate:
- POST /tasks:
- GET /tasks:
- Validaciones:
- Pruebas:

## 3. Impacto técnico
| Componente | Cambio | Motivo |
|---|---|---|
| Task | ... | ... |
| TaskCreate | ... | ... |
| POST /tasks | ... | ... |
| GET /tasks | ... | ... |
| Tests | ... | ... |

## 4. Archivos a modificar
- ...

## 5. Archivos a crear
- ...

## 6. Alternativas
### Alternativa A
- Descripción:
- Ventajas:
- Riesgos:

### Alternativa B
- Descripción:
- Ventajas:
- Riesgos:

## 7. Decisión
- Opción elegida:
- Motivo:
- Qué recomendó Copilot:
- Qué decidí yo:

## 8. Criterios de aceptación
- [ ] low funciona.
- [ ] medium funciona.
- [ ] high funciona.
- [ ] valor inválido es rechazado.
- [ ] priority ausente es rechazada.
- [ ] GET /tasks devuelve priority.

## 9. Estrategia de pruebas
| Escenario | Tipo | Resultado esperado |
|---|---|---|
| low | ... | ... |
| medium | ... | ... |
| high | ... | ... |
| inválida | ... | ... |
| ausente | ... | ... |
| GET /tasks | ... | ... |

## 10. Compatibilidad
...

## 11. Riesgos y mitigaciones
...

## 12. Rollback
...

## 13. Orden de implementación
1. ...
2. ...
3. ...
4. ...

## 14. Decisiones humanas
- ...

## 15. Pregunta de revisión
...
```

### 4. Verifica el plan

Copia y pega:

```text
Revisa docs/implementation-plan.md contra el requerimiento original.

No modifiques archivos.

Devuelve una tabla:
- requisito;
- dónde está cubierto;
- evidencia;
- qué falta.

Después indica si existe algún cambio innecesario.
```

Aplica las correcciones.

Haz commit y push.

**Tiempo: 15-17 min.**
