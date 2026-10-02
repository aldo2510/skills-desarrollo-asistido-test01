## Step 1: Analiza el proyecto

### Teoría: por qué analizar antes de programar

Cuando trabajas con una base de código existente, el primer riesgo no es escribir código incorrecto: es **cambiar algo sin entender cómo funciona**.

Antes de pedirle a una IA que implemente una funcionalidad, conviene construir un modelo mental mínimo del sistema:

```
Código existente → comportamiento actual → puntos de cambio → riesgos
```

Copilot puede acelerar esta exploración, pero su explicación no reemplaza la lectura del código. En este laboratorio aprenderás una práctica importante de desarrollo asistido por IA:

> **Usar IA para acelerar la comprensión, pero verificar la información contra el repositorio.**

### Objetivo

Usar Copilot para entender la aplicación antes de modificarla.

### 1. Abre el GitHub Codespace

Usa el siguiente botón para abrir la página **Create Codespace** en una nueva pestaña. Utiliza la configuración predeterminada.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

Espera a que se abra Visual Studio Code en el navegador y a que termine de preparar el entorno.

El repositorio ya incluye un archivo `.devcontainer/devcontainer.json`, por lo que Codespaces instalará el entorno de Python y las extensiones necesarias para el laboratorio.

> **Nota:** el enlace utiliza `{{full_repo_name}}`, una variable que GitHub Skills reemplaza automáticamente por el repositorio del participante cuando se publica el contenido del Step.

### 2. Instala y ejecuta

Dentro del Codespace, abre una terminal y ejecuta:

```bash
pip install -r requirements.txt
pytest -q
```

Resultado esperado: las pruebas existentes pasan.

### 3. Compara tu análisis con Copilot

Ahora utiliza Copilot para contrastar tu comprensión del proyecto con la interpretación de la IA.

**No tienes que inventar ningún prompt.** Copia y pega exactamente el siguiente bloque en **Copilot Chat**:

```text
Analiza el proyecto FastAPI actual como un ingeniero senior.

IMPORTANTE:
- No modifiques ningún archivo.
- No escribas código.
- No propongas cambios.
- Basa tu análisis únicamente en los archivos que realmente existen en este repositorio.
- Si no puedes confirmar algo en el código, indícalo como "No confirmado".

Analiza únicamente estos puntos:

1. ¿Cuál es la responsabilidad de app/main.py?
2. ¿Qué endpoints existen? Indica método HTTP, ruta, entrada y respuesta.
3. ¿Qué representan los modelos Task y TaskCreate y qué campos tiene cada uno?
4. ¿Cómo se almacenan actualmente las tareas?
5. ¿Cómo se ejecutan las pruebas y qué herramienta utilizan?
6. ¿Qué ocurre paso a paso cuando se ejecuta POST /tasks?
7. ¿Qué ocurre paso a paso cuando se ejecuta PATCH /tasks/{task_id}?
8. Indica dos riesgos o decisiones técnicas que deberían conocerse antes de modificar el proyecto.

Al final incluye exactamente estas dos secciones:

## Verificaciones necesarias

Indica 3 afirmaciones de tu análisis que deberían verificarse directamente revisando los archivos del repositorio.

## Posible interpretación incorrecta

Indica 1 afirmación que podría ser incorrecta o que necesite confirmación adicional.

No generes archivos y no realices cambios en el repositorio.
```

Después de ejecutar el prompt:

1. Lee la respuesta de Copilot.
2. Compara sus afirmaciones con `app/main.py`, `tests/test_api.py` y `requirements.txt`.
3. No necesitas copiar la respuesta de Copilot al repositorio.
4. El objetivo es comprobar que puedes **usar la IA para acelerar el análisis sin aceptar automáticamente sus conclusiones**.

> **Importante:** Copilot participa en este Step como herramienta de análisis. Sin embargo, el resultado del laboratorio no depende de que Copilot produzca exactamente una respuesta determinada: la fuente definitiva sigue siendo el código del repositorio.

### 4. Crea el documento

Crea el archivo `docs/project-analysis.md`.

No necesitas inventar el contenido ni completar campos manualmente. **Copia y pega exactamente todo el bloque siguiente en el archivo**.

````markdown
# Project Analysis

## 1. Arquitectura

| Archivo | Responsabilidad |
|---|---|
| app/main.py | Contiene la aplicación FastAPI, los modelos Task y TaskCreate, la lista en memoria y los endpoints de la API. |
| app/__init__.py | Identifica `app` como un paquete Python. |
| tests/test_api.py | Contiene las pruebas automatizadas de los endpoints principales. |
| requirements.txt | Define las dependencias Python necesarias para ejecutar la aplicación y sus pruebas. |
| pytest.ini | Configura pytest para incluir el directorio raíz del proyecto en el path de importación. |

## 2. Endpoints

| Método | Endpoint | Entrada | Respuesta |
|---|---|---|---|
| GET | /health | Sin parámetros | `{"status": "ok"}` |
| GET | /tasks | Sin parámetros | Lista de tareas |
| POST | /tasks | JSON con `title` | Nueva tarea con `id`, `title` y `completed` |
| PATCH | /tasks/{task_id} | ID de la tarea en la URL | Tarea actualizada con `completed=true` |

## 3. Modelos

### Task

Representa una tarea existente.

- `id`: identificador entero.
- `title`: título de la tarea.
- `completed`: indica si la tarea está completada. Por defecto es `false`.

### TaskCreate

Representa los datos necesarios para crear una tarea.

- `title`: título de la nueva tarea.

## 4. Persistencia actual

La aplicación utiliza una lista Python llamada `tasks` como almacenamiento en memoria.

No existe una base de datos.

Esto significa que los datos se pierden cuando se reinicia la aplicación.

## 5. Ejecución de pruebas

Comando utilizado:

```bash
pytest -q
```

Resultado esperado:

```text
4 passed
```

## 6. Riesgos o decisiones técnicas

1. La información se almacena únicamente en memoria, por lo que no existe persistencia entre reinicios.
2. La generación del ID depende de los IDs existentes en la lista de tareas.
3. Los cambios realizados directamente sobre la lista global afectan el estado compartido de la aplicación durante la ejecución.
4. Las pruebas utilizan FastAPI TestClient y no requieren levantar un servidor HTTP real.

## 7. Lo que Copilot dijo vs. lo que verifiqué

La respuesta de Copilot se utilizó como apoyo para comprender el proyecto y se contrastó con el código real del repositorio.

| Afirmación | Cómo la verifiqué | Resultado |
|---|---|---|
| La aplicación utiliza FastAPI | Revisé `app/main.py` | Confirmado |
| Las tareas se almacenan en memoria | Revisé la variable `tasks` | Confirmado |
| Existen cuatro endpoints principales | Revisé las funciones decoradas con `@app.get`, `@app.post` y `@app.patch` | Confirmado |

## 8. Información de Copilot verificada manualmente

- Copilot puede acelerar la lectura inicial del proyecto.
- La información generada por IA debe contrastarse con los archivos reales.
- La fuente definitiva para este ejercicio es el código del repositorio.

## 9. Pregunta técnica abierta

¿Qué cambios serían necesarios para agregar un nuevo campo `priority` a las tareas sin romper los endpoints ni las pruebas existentes?
````

> **Importante:** el bloque anterior utiliza cuatro acentos graves (````) para delimitar el archivo completo porque dentro de `project-analysis.md` existen bloques Markdown de tres acentos graves. Debes copiar el contenido **desde `# Project Analysis` hasta la última línea de la pregunta**, sin copiar los cuatro acentos graves externos.

Después de pegarlo, guarda el archivo.

### 5. Verificación final

Ejecuta:

```bash
test -f docs/project-analysis.md
pytest -q
```

Si ambos comandos terminan correctamente, haz commit y push:

```bash
git add docs/project-analysis.md
git commit -m "docs: analyze project structure"
git push
```

**Resultado del Step:** tendrás un análisis documentado del proyecto y habrás comprobado que una explicación generada por IA debe contrastarse con el código fuente antes de aceptarla como válida.

> **Objetivo del Step:** aprender a verificar una explicación de IA contra el código real. El documento ya contiene una respuesta base para que puedas avanzar; puedes contrastarla con Copilot, pero no necesitas esperar a que Copilot genere el contenido.

**Tiempo: 15-17 min.**
