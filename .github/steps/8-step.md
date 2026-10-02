# Step 8 — Revisa el PR como un equipo técnico

## Teoría
La revisión debe combinar requerimiento, código, pruebas y documentación.

## 1. Prompt
~~~text
Realiza una revisión integral del Pull Request actual.

No modifiques archivos.

Compara:
- requerimiento original;
- implementation-plan;
- código;
- tests;
- debugging-notes;
- code-review;
- technical-decisions.

Devuelve:
1. requisitos cubiertos;
2. requisitos parcialmente cubiertos;
3. riesgos;
4. pruebas faltantes;
5. cambios innecesarios;
6. decisión que debería tomar el reviewer humano.

No escribas código.
~~~

## 2. Completa docs/technical-decisions.md
Agrega al final:

~~~markdown
## Revisión integral

La solución debe considerarse aceptable únicamente después de comprobar el requerimiento, el diff, las pruebas y los riesgos.

### Control humano
- El código fue revisado.
- Las pruebas fueron ejecutadas.
- Las recomendaciones de IA fueron contrastadas.
- El reviewer humano conserva la decisión final.
~~~

## 3. Verificación
~~~bash
test -f docs/technical-decisions.md
test -f docs/code-review.md
pytest -q
~~~

## 4. Commit
~~~bash
git add docs/technical-decisions.md
git commit -m "docs: complete technical review"
git push
~~~
**Tiempo sugerido: 6–8 min.**