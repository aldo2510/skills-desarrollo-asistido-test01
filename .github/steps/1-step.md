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

### 3. Copia y pega este prompt en Copilot Chat

```text
Analiza este proyecto FastAPI como un ingeniero senior. No modifiques ningún archivo.

Explícame:
1. La arquitectura y responsabilidad de cada archivo.
2. Los endpoints existentes, método HTTP, entrada y respuesta.
3. Los modelos Task y TaskCreate y sus campos.
4. Cómo se almacena actualmente la información.
5. Cómo se ejecutan las pruebas.
6. El flujo completo de POST /tasks.
7. El flujo completo de PATCH /tasks/{task_id}.
8. Al menos 2 riesgos o decisiones técnicas que debería conocer antes de modificar el proyecto.

Termina con una sección llamada "Lo que Copilot dijo vs. lo que debo verificar" con al menos 3 verificaciones concretas.
No escribas código ni hagas cambios.
```

### 4. Crea el documento

Crea `docs/project-analysis.md`.

**Copia y pega esta estructura y complétala usando la respuesta de Copilot y verificando los datos en el código:**

```markdown
# Project Analysis

## 1. Arquitectura
| Archivo | Responsabilidad |
|---|---|
| app/main.py | ... |
| tests/test_api.py | ... |
| requirements.txt | ... |

## 2. Endpoints
| Método | Endpoint | Entrada | Respuesta |
|---|---|---|---|
| GET | /health | ... | ... |
| GET | /tasks | ... | ... |
| POST | /tasks | ... | ... |
| PATCH | /tasks/{task_id} | ... | ... |

## 3. Modelos
### Task
- ...

### TaskCreate
- ...

## 4. Persistencia actual
...

## 5. Ejecución de pruebas
```bash
pytest -q
```
Resultado:
...

## 6. Riesgos o decisiones técnicas
1. ...
2. ...

## 7. Lo que Copilot dijo vs. lo que verifiqué
| Afirmación de Copilot | Cómo la verifiqué | Resultado |
|---|---|---|
| ... | ... | ... |
| ... | ... | ... |
| ... | ... | ... |

## 8. Información de Copilot verificada manualmente
- ...
- ...

## 9. Pregunta técnica abierta
- ...
```

### 5. Verificación final

Ejecuta:

```bash
test -f docs/project-analysis.md
pytest -q
```

Haz commit y push.

**Tiempo: 15-17 min.**
