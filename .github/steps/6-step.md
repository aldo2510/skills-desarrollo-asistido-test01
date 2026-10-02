# Step 6 — Revisa el cambio antes del merge

## Teoría
El review asistido por IA debe buscar defectos, no reemplazar el juicio del reviewer.

## 1. Prompt
~~~text
Actúa como reviewer senior del Pull Request actual.

Revisa el diff contra main.

No modifiques archivos.

Busca:
- errores funcionales;
- regresiones;
- validaciones incompletas;
- pruebas faltantes;
- cambios fuera de alcance;
- problemas de mantenibilidad;
- riesgos de compatibilidad.

Para cada hallazgo indica archivo, problema, evidencia y severidad.
Si no encuentras problemas, explica qué verificaste.
~~~

## 2. Crea docs/code-review.md
~~~markdown
# Code Review

## Alcance
Se revisó el diff del Pull Request contra main.

## Checklist
- [x] Requerimiento de priority revisado.
- [x] Validación de entrada revisada.
- [x] Endpoints revisados.
- [x] Pruebas revisadas.
- [x] Cambios fuera de alcance revisados.
- [x] Regresión de la suite revisada.

## Hallazgos
La respuesta de Copilot debe contrastarse con el código real antes de registrar un hallazgo como válido.

## Evidencia
~~~bash
git diff main...HEAD
pytest -q
~~~

## Decisión
Solo aceptar cambios después de revisar evidencia.
~~~

## 3. Verificación
~~~bash
test -f docs/code-review.md
test -f docs/pr-description.md
pytest -q
~~~

## 4. Commit
~~~bash
git add docs/code-review.md
git commit -m "docs: record ai code review"
git push
~~~
**Tiempo sugerido: 8–10 min.**