# Laboratorios para estudiantes

Cada laboratorio incluye objetivo, escenario, requisitos, pasos, resultado esperado, validación, reflexión y reto.

## 1. Crear una branch
Objetivo: practicar branches. Escenario: preparar mejora de docs. Requisitos: repo clonado. Pasos: `git switch -c docs/readme-note`. Resultado: branch creada. Validación: `git branch --show-current`. Reflexión: ¿por qué no trabajar directo en main? Reto: publica la branch.

## 2. Corregir un error
Objetivo: corregir búsqueda. Pasos: crear Issue, modificar prueba, corregir servicio. Resultado: test pasa. Validación: `pytest tests/test_customers.py`.

## 3. Crear un Issue
Objetivo: describir trabajo. Pasos: usar template, labels, milestone y criterios. Resultado: Issue listo. Reto: vincularlo a Project.

## 4. Abrir un pull request
Objetivo: practicar PR. Pasos: push branch, abrir PR, completar template. Validación: checks aparecen.

## 5. Revisar un pull request
Objetivo: hacer code review. Pasos: leer diff, comentar línea, solicitar cambios o aprobar. Reflexión: diferencia entre comentario y review.

## 6. Resolver un conflicto
Objetivo: resolver conflicto controlado en `docs/roadmap.md`. Pasos: crear dos branches, editar misma línea, merge, resolver marcadores. Validación: pruebas en verde.

## 7. Ejecutar GitHub Actions
Objetivo: interpretar CI. Pasos: abrir Actions, revisar job, provocar fallo controlado y corregir. Reto: leer summary.

## 8. Usar GitHub Copilot
Objetivo: usar Ask, Edit y Agent. Pasos: pedir explicación, generar prueba y refactor. Validación: revisar cambios antes de aceptar.

## 9. Crear un Project
Objetivo: organizar trabajo. Pasos: estados Backlog, Ready, In Progress, In Review, Done; campos Priority, Size, Iteration, Area, Target release. Resultado: board con Issues.

## 10. Crear una release
Objetivo: versionado. Pasos: tag `v1.0.0`, notas, release y artefacto. Reflexión: tag vs release.

## 11. Identificar seguridad
Objetivo: reconocer riesgos. Pasos: revisar `SECURITY.md`, Dependabot y CodeQL. Validación: explicar secreto vs dependencia vulnerable.

## 12. Mejorar Markdown
Objetivo: documentar mejor. Pasos: agregar tabla o diagrama Mermaid. Validación: preview Markdown. Reto: prompt bilingüe con Copilot.
