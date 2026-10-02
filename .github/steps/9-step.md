# Step 9 — Ejecuta la validación final

## Teoría
Antes de cerrar el ejercicio necesitas evidencia reproducible.

## 1. Prompt
~~~text
Analiza el estado final del proyecto.

No modifiques archivos.

Dime qué comandos debo ejecutar para comprobar:
- instalación;
- pruebas;
- archivos obligatorios;
- consistencia del cambio;
- ausencia de cambios fuera de alcance.

No inventes resultados.
~~~

## 2. Ejecuta la validación
~~~bash
python -m pip install -r requirements.txt
pytest -q
git status --short
git diff --check
test -f docs/project-analysis.md
test -f docs/implementation-plan.md
test -f docs/implementation-review.md
test -f docs/test-strategy.md
test -f docs/debugging-notes.md
test -f docs/pr-description.md
test -f docs/code-review.md
test -f docs/technical-decisions.md
~~~

## 3. Crea docs/final-validation.md
~~~markdown
# Final Validation

## Comandos
~~~bash
python -m pip install -r requirements.txt
pytest -q
git status --short
git diff --check
~~~

## Evidencia esperada
- Dependencias instaladas.
- Suite de pruebas correcta.
- Sin errores de whitespace.
- Documentación obligatoria presente.

## Control humano
El resultado de cada comando debe revisarse directamente. No registrar como exitoso un comando que no fue ejecutado.

## Resultado
La solución está lista para revisión final cuando todas las validaciones anteriores terminan correctamente.
~~~

## 4. Commit
~~~bash
git add docs/final-validation.md
git commit -m "docs: record final validation"
git push
~~~
**Tiempo sugerido: 7–8 min.**