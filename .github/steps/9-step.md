## Step 9: Ejecuta la validación final

### Teoría
La validación final comprueba coherencia entre requerimiento, código, pruebas, documentación y PR.

### Copia y pega
```text
Revisa el ejercicio completo contra el requerimiento original.
No modifiques archivos.
Comprueba priority, pruebas, bug corregido, documentación y Pull Request.
Devuelve una checklist PASS/FAIL con evidencia. No inventes evidencia.
```

Ejecuta:

```bash
pytest -q
test -f docs/project-analysis.md
test -f docs/implementation-plan.md
test -f docs/implementation-review.md
test -f docs/test-strategy.md
test -f docs/debugging-notes.md
test -f docs/pr-description.md
test -f docs/code-review.md
test -f docs/technical-decisions.md
```

Crea `docs/final-validation.md` con:

```markdown
# Final Validation
| Requisito | PASS/FAIL | Evidencia |
|---|---|---|
| priority | ... | ... |
| pruebas | ... | ... |
| debugging | ... | ... |
| documentación | ... | ... |
| PR | ... | ... |

## Riesgos pendientes
...
```

Haz commit y push.

**Tiempo: 7-8 min.**