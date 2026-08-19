# Guía de demostración GH-900 para instructor

## DEMO 1: Crear el repositorio

Crear repositorio público o privado, agregar descripción y topics, explicar README, `.gitignore`, licencia, clonar, mostrar `origin` y remotes.

## DEMO 2: Commits

Modificar README, ejecutar `git status`, `git diff`, agregar al staging, crear commit y publicar. Explicar working directory, staging area y repository.

## DEMO 3: Branches y GitHub Flow

Crear `feature/customer-search`, implementar búsqueda, hacer commits pequeños, publicar branch y comparar con `main`.

## DEMO 4: Issues

Ejemplos completos:

- Bug: Customer search is case-sensitive. Pasos: buscar `CONTOSO`; criterios: resultado equivalente; labels: bug; milestone: v1.1.0; relacionado con industry filter.
- Feature: Add filtering by customer industry. Criterios: endpoint probado; labels: enhancement; milestone: v1.1.0.
- Documentation: Add API examples to README. Criterios: curl para endpoints; labels: documentation; milestone: v1.0.0.
- Security: Review input validation. Criterios: payload inválido devuelve 400; labels: security; milestone: v1.0.0.
- Technical debt: Refactor customer service. Criterios: comportamiento sin cambios; labels: technical debt; milestone: v1.1.0.

## DEMO 5: Pull request

Abrir PR desde `feature/customer-search`, vincular Issue con `Closes #`, completar checklist, solicitar revisión, comentar, sugerir cambios, aprobar, mostrar checks, hacer merge y eliminar branch.

## DEMO 6: Conflicto de merge

Crear dos branches que cambien la misma sección de `docs/roadmap.md`, provocar conflicto, explicar marcadores, resolver, ejecutar pruebas y completar merge.

## DEMO 7: GitHub Copilot

Prompts: explicar repositorio, explicar archivo, generar función, crear endpoint, generar pruebas, corregir error, mejorar documentación, crear commit, crear PR, revisar código, identificar seguridad, refactorizar, crear Mermaid y generar datos ficticios.

## DEMO 8: GitHub Actions

Abrir `ci.yml`, explicar eventos/jobs/runners/steps, provocar prueba fallida controlada, mostrar check fallido, corregir, reejecutar y mostrar éxito.

## DEMO 9: GitHub Projects

Estados: Backlog, Ready, In Progress, In Review, Done. Campos: Priority, Size, Iteration, Area, Target release. Cargar los Issues de la DEMO 4 y mostrar vistas table, board y roadmap.

## DEMO 10: Releases y tags

Crear tag `v1.0.0`, explicar SemVer, preparar notas, crear release, adjuntar artefacto y comparar release contra commit simple.

## DEMO 11: Seguridad

Mostrar `SECURITY.md`, Dependabot, dependency graph, CodeQL, secret scanning, push protection y diferencias entre código vulnerable, dependencia vulnerable y secreto expuesto. No usar secretos reales ni vulnerabilidades explotables.

## DEMO 12: Comunidad

Mostrar `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SUPPORT.md`, forks, stars, watching, following, Discussions conceptualmente y participación responsable.
