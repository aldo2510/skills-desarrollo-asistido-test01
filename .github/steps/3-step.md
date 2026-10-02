## Step 3: Implementa, compara y decide

### Teoría: la IA propone, pero la decisión técnica sigue siendo humana

En desarrollo asistido por IA no basta con generar código. El flujo correcto es:

~~~
Plan → Implementación con IA → Diff → Pruebas → Comparación → Decisión humana → Evidencia
~~~

En este Step vas a implementar el requerimiento de priority, comparar la solución utilizada con una alternativa y dejar documentada la decisión.

La regla del ejercicio es:

> **Copilot puede implementar y recomendar, pero tú debes revisar el diff, ejecutar las pruebas y decidir qué solución aceptar.**

---

## 1. Implementa el requerimiento con Copilot Agent

Abre Copilot Chat en modo **Agent**.

Copia y pega exactamente este prompt:

~~~
Implementa el requerimiento descrito en docs/implementation-plan.md.

Objetivo:
Agregar el campo priority a las tareas.

Requisitos obligatorios:
- Task debe tener un campo priority.
- priority solo puede aceptar low, medium o high.
- TaskCreate debe recibir priority.
- priority debe ser obligatoria al crear una tarea.
- POST /tasks debe guardar la priority recibida.
- GET /tasks debe devolver priority.
- Las tareas iniciales deben tener una priority válida.
- Agrega las pruebas necesarias para cubrir el nuevo comportamiento.
- Mantén funcionando las funcionalidades existentes.

Antes de modificar archivos:
1. inspecciona app/main.py;
2. inspecciona tests/test_api.py;
3. revisa docs/implementation-plan.md;
4. identifica exactamente qué archivos necesitan cambios.

No modifiques funcionalidades que estén fuera del requerimiento.

Después de implementar:
1. ejecuta pytest -q;
2. revisa el resultado de las pruebas;
3. muestra los archivos modificados;
4. explica brevemente qué cambió en cada archivo;
5. identifica cualquier decisión técnica que hayas tomado.

No agregues dependencias nuevas salvo que sean estrictamente necesarias.
~~~

Cuando termine Copilot:

~~~bash
git diff
pytest -q
~~~

**No aceptes automáticamente todos los cambios.** Revisa primero el diff.

---

## 2. Verifica la implementación

Comprueba que:

- [ ] Task contiene priority.
- [ ] TaskCreate contiene priority.
- [ ] solo se aceptan low, medium y high.
- [ ] priority es obligatoria al crear.
- [ ] POST /tasks conserva la prioridad.
- [ ] GET /tasks devuelve la prioridad.
- [ ] las tareas iniciales tienen una prioridad válida.
- [ ] las pruebas existentes continúan funcionando.
- [ ] existen pruebas para el nuevo comportamiento.

Ejecuta:

~~~bash
pytest -q
~~~

El resultado debe terminar correctamente.

---

## 3. Pide a Copilot una alternativa

Ahora utiliza Copilot para analizar si existe otra forma razonable de implementar la misma regla.

Copia y pega:

~~~
Analiza la implementación actual de priority en este proyecto.

No modifiques ningún archivo y no escribas código.

Propón una alternativa técnicamente válida para modelar y validar priority.

Compara la implementación actual y la alternativa considerando:

1. claridad;
2. mantenibilidad;
3. validación;
4. extensibilidad;
5. compatibilidad;
6. complejidad;
7. riesgo de errores.

Indica:
- qué solución está actualmente implementada;
- qué solución alternativa propones;
- qué ventajas tiene cada una;
- qué desventajas tiene cada una;
- qué aspectos deberían verificarse antes de cambiar de solución.

Termina con:
- una recomendación técnica;
- dos aspectos que el desarrollador debe verificar manualmente.

No modifiques ningún archivo.
~~~

---

## 4. Crea el documento de revisión

Crea:

docs/implementation-review.md

**Copia y pega esta plantilla completa:**

~~~markdown
# Implementation Review

## 1. Objetivo

Comparar la implementación actual de priority con una alternativa técnicamente válida y registrar la decisión humana.

El requerimiento es:

- priority debe aceptar low, medium o high;
- priority es obligatoria al crear;
- GET /tasks debe devolver priority;
- las pruebas deben cubrir el nuevo comportamiento;
- no se deben modificar funcionalidades fuera del alcance.

## 2. Opción implementada

La implementación actual utiliza validación en el modelo de entrada mediante Pydantic.

Características verificadas:

- Task contiene priority.
- TaskCreate contiene priority.
- priority es obligatoria.
- Los valores permitidos son low, medium y high.
- POST /tasks conserva la prioridad.
- GET /tasks devuelve la prioridad.
- Existen pruebas para el nuevo comportamiento.

## 3. Alternativa considerada

Una alternativa sería realizar la validación manualmente dentro del endpoint POST /tasks.

### Ventajas de la alternativa

- La regla de validación queda visible directamente en el endpoint.
- Puede resultar sencilla en una aplicación pequeña.

### Desventajas de la alternativa

- La validación queda acoplada a la lógica del endpoint.
- Puede duplicarse si otros endpoints necesitan la misma regla.
- Existe mayor riesgo de olvidar aplicar la misma validación en otro punto.

## 4. Comparación

| Criterio | Implementación actual | Alternativa |
|---|---|---|
| Claridad | La regla pertenece al contrato del modelo | La regla queda dentro del endpoint |
| Mantenibilidad | La validación está centralizada | Puede quedar distribuida |
| Validación | FastAPI/Pydantic valida la entrada | El endpoint debe validar manualmente |
| Extensibilidad | Es sencillo ampliar el modelo | Puede requerir más lógica en endpoints |
| Compatibilidad | Debe verificarse el contrato de entrada | Debe verificarse el comportamiento HTTP |
| Complejidad | Menor duplicación | Mayor acoplamiento al endpoint |
| Riesgo | Riesgo principal: modificar el modelo incorrectamente | Riesgo de duplicar u olvidar validaciones |

## 5. Revisión de Copilot

Prompt utilizado:

Analiza la implementación actual de priority y compárala con una alternativa.

### Recomendaciones de Copilot

Registrar aquí las recomendaciones concretas entregadas por Copilot.

### Lo que verifiqué directamente

- Revisé app/main.py.
- Revisé tests/test_api.py.
- Revisé el diff.
- Ejecuté pytest -q.

## 6. Decisión humana

### Opción seleccionada

Mantener la implementación actual basada en validación del modelo.

### Motivo

La regla de valores permitidos forma parte del contrato de entrada de la API y mantenerla en el modelo permite centralizar la validación.

### Recomendación de Copilot que acepté

Mantener la validación asociada al modelo porque reduce duplicación y mantiene el contrato cerca de los datos de entrada.

### Recomendación de Copilot que modifiqué o rechacé

No se aceptó ninguna recomendación que implicara cambios fuera del alcance del requerimiento.

Si Copilot propuso otra recomendación, registrarla aquí y explicar por qué fue modificada o rechazada.

## 7. Evidencia

Comandos ejecutados:

~~~bash
git diff
pytest -q
~~~

Resultado:

- El diff fue revisado manualmente.
- Las pruebas fueron ejecutadas.
- Los cambios fueron contrastados con el requerimiento original.

## 8. Conclusión

La implementación fue revisada con asistencia de IA, pero la decisión final se tomó después de revisar el código, comparar alternativas y ejecutar las pruebas.

La IA fue utilizada como apoyo para analizar y contrastar la solución, no como autoridad final.
~~~

---

## 5. Revisión adicional con Copilot

Después de crear el documento, copia y pega:

~~~
Revisa la implementación actual de priority y docs/implementation-review.md.

No modifiques ningún archivo.

Comprueba:

1. que la implementación cumple el requerimiento original;
2. que la comparación entre las dos alternativas es técnicamente coherente;
3. que no se atribuyan al código comportamientos que realmente no existen;
4. que las pruebas mencionadas correspondan a pruebas realmente ejecutadas;
5. que la decisión humana esté respaldada por evidencia.

Devuelve:

## Hallazgos
Lista los problemas encontrados.

## Evidencia faltante
Lista cualquier afirmación que todavía deba verificarse.

## Riesgos
Lista cualquier riesgo técnico importante que no esté documentado.

No escribas código.
~~~

Revisa la respuesta de Copilot y corrige el documento **solo si verificaste que la observación corresponde al código real**.

---

## 6. Ejecuta la validación final

Ejecuta:

~~~bash
test -f docs/implementation-review.md
grep -q "Decisión humana" docs/implementation-review.md
grep -q "Revisión de Copilot" docs/implementation-review.md
pytest -q
~~~

Los cuatro comandos deben terminar correctamente.

---

## 7. Revisa el diff final

Ejecuta:

~~~bash
git diff --stat
git diff
~~~

Comprueba que los cambios están relacionados con:

- priority;
- sus pruebas;
- documentación del ejercicio.

Si encuentras cambios no relacionados, elimínalos antes del commit.

---

## 8. Commit y push

Cuando hayas terminado:

~~~bash
git add app tests docs/implementation-review.md
git commit -m "feat: add task priority"
git push
~~~

---

## 9. Evidencia que debes conservar

Al finalizar este Step debes tener:

- implementación funcional de priority;
- pruebas automatizadas;
- docs/implementation-review.md;
- evidencia de pytest -q;
- comparación entre alternativas;
- decisión humana documentada.

---

## 10. Qué aprendiste

En este Step practicaste el ciclo:

~~~
IA genera → humano revisa → pruebas verifican → IA compara → humano decide
~~~

La capacidad importante no es aceptar código generado por IA rápidamente, sino **saber evaluar si la solución propuesta realmente cumple el requerimiento**.

**Tiempo sugerido: 18-22 min.**
