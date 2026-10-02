# Step 7 — Documenta decisiones técnicas

## Teoría
Una decisión técnica debe conservar contexto: problema, alternativas, decisión y consecuencias.

## 1. Prompt
~~~text
Analiza los cambios realizados en este ejercicio.

No modifiques archivos.

Identifica las decisiones técnicas más importantes relacionadas con:
- modelado de priority;
- validación;
- pruebas;
- generación de ID;
- compatibilidad.

Para cada una explica alternativas, beneficios, riesgos y consecuencia.
~~~

## 2. Crea docs/technical-decisions.md
~~~markdown
# Technical Decisions

## Decisión 1 — Validación de priority
**Decisión:** Validar priority en el modelo de entrada.

**Motivo:** La regla forma parte del contrato de la API.

**Alternativa:** Validación manual dentro del endpoint.

**Consecuencia:** La validación queda centralizada.

## Decisión 2 — Cobertura de pruebas
**Decisión:** Cubrir valores válidos, inválidos, ausencia del campo y regresiones.

**Motivo:** El nuevo campo cambia el contrato.

## Decisión 3 — Generación de ID
**Decisión:** Manejar explícitamente el caso de colección vacía.

**Motivo:** Evitar una excepción cuando no existen tareas.

## Evidencia
~~~bash
git diff
pytest -q
~~~
~~~

## 3. Revisión con Copilot
~~~text
Revisa docs/technical-decisions.md contra el código actual.

No modifiques archivos.

Indica cualquier decisión que no tenga evidencia suficiente o que describa un comportamiento inexistente.
~~~

## 4. Validación y commit
~~~bash
test -f docs/technical-decisions.md
pytest -q
git add docs/technical-decisions.md
git commit -m "docs: record technical decisions"
git push
~~~
**Tiempo sugerido: 8–10 min.**