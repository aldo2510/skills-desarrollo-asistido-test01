## Step 5: Depura un fallo real

### Teoría
Debugging asistido por IA debe seguir evidencia: síntoma → reproducción → causa raíz → corrección → regresión.

### Copia y pega
```text
Analiza create_task en app/main.py.
No corrijas todavía.
Explica qué ocurre si tasks está vacía y genera una prueba de regresión en tests/test_empty_tasks.py.
```

Después:

```text
Implementa tests/test_empty_tasks.py para reproducir el fallo.
No corrijas la implementación todavía.
Ejecuta esa prueba y muestra el fallo.
```

Después:

```text
Analiza el fallo.
No modifiques código.
Explica síntoma, causa raíz, dos alternativas y evidencia.
```

Finalmente:

```text
Corrige únicamente el bug identificado.
Ejecuta primero la regresión y luego pytest -q.
Muestra el diff.
```

### Documenta
Crea `docs/debugging-notes.md`:

```markdown
# Debugging Notes
## Síntoma
...
## Reproducción
...
## Causa raíz
...
## Hipótesis descartadas
...
## Alternativas
...
## Corrección
...
## Evidencia
...
```

Haz commit y push.

**Tiempo: 12-15 min.**