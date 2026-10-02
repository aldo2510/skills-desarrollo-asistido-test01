## Step 4: Diseña la estrategia de pruebas

### Teoría
Una funcionalidad no está terminada cuando "funciona una vez". Las pruebas convierten el requerimiento en comportamiento verificable. Una buena suite debe cubrir tanto casos válidos como inválidos.

### Copia y pega
```text
Diseña e implementa tests/test_priority.py para el requerimiento de priority.
Cubre low, medium, high, prioridad inválida, prioridad ausente y priority visible en GET /tasks.
Ejecuta pytest -q.
Después revisa las assertions buscando falsos positivos.
```

### Documenta
Crea `docs/test-strategy.md`:

```markdown
# Test Strategy
## Escenarios
| Escenario | Qué valida | Resultado |
|---|---|---|
| low | ... | ... |
| medium | ... | ... |
| high | ... | ... |
| inválida | ... | ... |
| ausente | ... | ... |
| GET /tasks | ... | ... |

## Revisión QA
- Hallazgo:
- Corrección:

## Evidencia
- Comando:
- Resultado:
```

Ejecuta `pytest -q`, haz commit y push.

**Tiempo: 10-12 min.**