# Biblioteca de prompts Copilot

Cada prompt incluye contexto, objetivo, restricciones, criterios y formato.

## Español

### Explicar arquitectura
Contexto: Este repositorio es una app Flask GH-900. Objetivo: explica la arquitectura para audiencia no técnica. Restricciones: no inventes servicios externos. Criterios: menciona rutas, servicios, modelos y datos. Formato: resumen y diagrama Mermaid.

### Endpoint por industria
Contexto: `app/routes.py` y `app/services.py`. Objetivo: crea un endpoint para buscar clientes por industria. Restricciones: Python 3.12, SQLAlchemy, datos ficticios, validar entrada. Criterios: tests Pytest pasan. Formato: diff y explicación.

### Pruebas unitarias
Contexto: endpoint nuevo. Objetivo: genera pruebas unitarias. Restricciones: usar fixtures existentes. Criterios: cubre éxito y validación. Formato: código Pytest.

### Revisión de seguridad
Contexto: cambio actual. Objetivo: revisa seguridad, confiabilidad y mantenibilidad. Restricciones: no estilos triviales. Criterios: hallazgos accionables. Formato: severidad, archivo, recomendación.

### Refactor
Contexto: función ineficiente de búsqueda. Objetivo: refactorizar sin cambiar comportamiento. Restricciones: mantener tests. Criterios: API compatible. Formato: pasos y diff.

### PR y commits
Contexto: cambios staged. Objetivo: generar descripción de PR y mensaje Conventional Commits. Restricciones: conciso. Criterios: vincular Issue si existe. Formato: título, resumen, checklist.

### Mermaid y deuda técnica
Contexto: flujo de órdenes. Objetivo: crear diagrama Mermaid e identificar deuda técnica. Restricciones: educativo. Criterios: acciones incrementales. Formato: diagrama y backlog.

## English

### Explain repository
Context: This is a GH-900 Flask training repository. Goal: explain components and relationships. Constraints: do not assume cloud services. Acceptance: include routes, services, database and tests. Format: bullets plus Mermaid.

### Generate endpoint
Context: Customer API. Goal: add industry search endpoint. Constraints: validate input, Python 3.12, SQLAlchemy. Acceptance: unit tests pass. Format: patch and explanation.

### Review code
Context: Current branch diff. Goal: find security, reliability and maintainability issues. Constraints: ignore trivial style. Acceptance: high-confidence findings only. Format: severity, evidence, fix.

### Explain error
Context: Failing test output. Goal: explain the error and suggest a fix. Constraints: preserve existing behavior. Acceptance: root cause and minimal patch. Format: diagnosis and commands.

### Acceptance criteria
Context: Issue description. Goal: generate acceptance criteria. Constraints: testable and clear. Acceptance: Given/When/Then style. Format: checklist.
