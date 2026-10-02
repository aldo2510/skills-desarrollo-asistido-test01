## Step 7: Haz code review asistido por IA

### Teoría
Una IA puede revisar un diff, pero el reviewer humano decide si una observación es válida. El objetivo es detectar cambios no relacionados, tests débiles y riesgos.

### Copia y pega
```text
Revisa el Pull Request actual como reviewer senior.
No modifiques archivos.
Busca cambios no relacionados, tests débiles, validaciones faltantes, comportamiento inesperado y documentación sin evidencia.
Devuelve los hallazgos y su evidencia.
```

Revisa cada hallazgo contra el diff. Corrige los problemas reales y vuelve a ejecutar `pytest -q`.

Crea `docs/code-review.md`:

```markdown
# Code Review
## Hallazgos de IA
- ...
## Hallazgos confirmados
- ...
## Hallazgos rechazados
- ...
## Correcciones realizadas
- ...
## Evidencia
...
```

Haz commit y push.

**Tiempo: 8-10 min.**