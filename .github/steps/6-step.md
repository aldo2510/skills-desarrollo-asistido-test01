## Step 6: Prepara el Pull Request

### Teoría
El Pull Request convierte un cambio local en una unidad revisable. La descripción debe permitir que otra persona entienda problema, solución, evidencia y riesgos sin reconstruir la historia.

### Copia y pega
```text
Genera una descripción de Pull Request usando únicamente evidencia del repositorio.
Incluye problema, solución, archivos modificados, pruebas, riesgos, rollback y decisiones humanas.
No inventes resultados.
```

Crea `docs/pr-description.md`:

```markdown
# Pull Request
## Problema
...
## Solución
...
## Archivos modificados
- ...
## Pruebas
- ...
## Riesgos
- ...
## Rollback
...
## Decisiones humanas
...
```

Crea una rama, haz commit y push y abre un PR contra `main`. **No hagas merge.**

**Tiempo: 8-10 min.**