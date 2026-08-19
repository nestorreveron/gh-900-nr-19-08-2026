# Roadmap y backlog

Versiones ficticias: v0.1.0 Initial prototype, v0.5.0 Training preview, v1.0.0 Course release, v1.1.0 Search improvements, v2.0.0 Analytics expansion.

| Tipo | Elemento | Prioridad | Tamaño | Área | Versión | Criterios de aceptación |
| --- | --- | --- | --- | --- | --- | --- |
| Bug | Customer search is case-sensitive | Alta | S | API | v1.1.0 | Buscar `contoso` y `CONTOSO` devuelve resultados equivalentes |
| Feature | Add filtering by industry | Media | M | API | v1.1.0 | Endpoint documentado y probado |
| Docs | Add API examples | Alta | S | Docs | v1.0.0 | README incluye curl para endpoints clave |
| Security | Review input validation | Alta | M | API | v1.0.0 | Payloads inválidos devuelven 400 |
| Tech debt | Refactor customer service | Media | M | Backend | v1.1.0 | Servicio mantiene cobertura de pruebas |
| Accessibility | Improve navigation labels | Media | S | UI | v1.0.0 | Navegación usable con lector de pantalla |
| Performance | Add indexes for search | Baja | M | DB | v2.0.0 | Consultas explicadas y medidas |
| Automation | Add Pages preview | Baja | M | CI | v0.5.0 | Documentación publicada desde Actions |
| Tests | Add product detail tests | Media | S | Tests | v0.5.0 | Pruebas de 200 y 404 |
| Feature | Add order export | Baja | L | API | v2.0.0 | Export CSV ficticio |
| Bug | Prevent negative order quantity | Alta | S | API | v1.0.0 | Test para cantidad negativa |
| Docs | Instructor checklist | Media | S | Docs | v1.0.0 | Guía con tiempos y objetivos |
| Security | Document push protection | Media | S | Security | v1.0.0 | Advertencias claras sin secretos reales |
| Feature | Dashboard trend chart | Baja | L | UI | v2.0.0 | Gráfico con datos ficticios |
| Tests | Add support status validation | Media | S | Tests | v0.5.0 | Estado inválido devuelve 400 |

## Escenarios de Pull Request

| Branch | Archivos | Cambio esperado | Issue | Pruebas | Comentarios posibles | Resultado |
| --- | --- | --- | --- | --- | --- | --- |
| feature/customer-search | `app/services.py`, `tests/test_customers.py` | Búsqueda por texto | #1 | Pytest clientes | Validar longitud mínima | Endpoint funcional |
| feature/industry-filter | `app/routes.py`, README | Filtro por industria | #2 | Test API | Documentar parámetro | Filtro agregado |
| fix/case-insensitive-search | `app/services.py` | Normalizar búsqueda | #3 | Test mayúsculas | Usar lower en ambos lados | Bug corregido |
| docs/api-examples | README | Más ejemplos curl | #4 | Revisión visual | Evitar tokens | Docs mejoradas |
| test/order-validation | `tests/test_orders.py` | Casos inválidos | #5 | Pytest | Cubrir producto inexistente | Mayor cobertura |
| refactor/customer-service | `app/services.py` | Separar validación | #6 | Suite API | Mantener comportamiento | Código limpio |
| security/input-validation | `app/routes.py`, `app/services.py` | Validación robusta | #7 | Pytest | No revelar detalles internos | API segura |
