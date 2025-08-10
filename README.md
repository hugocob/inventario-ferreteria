# Prototipo: Inventario de Ferretería (Python)

Cumple con el enunciado:
- **Clase base/abstracta**: `BaseEntity`
- **≥2 interfaces**: `Repository`, `Notifier` (y `Validator`)
- **2 repositorios**: `InMemoryProductoRepository`, `InMemoryCategoriaRepository`
- **2 servicios**: `StockService` (negocio) y `ReporteService` (consultas)
- Buenas prácticas: capas, validación, notificaciones, tipado

## Requisitos
Python 3.10+ y (opcional) entorno virtual

## Ejecutar
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
python main.py
```

## Funciones clave
- Crear categorías y productos
- Validación de datos de producto
- Vender y reponer stock con alerta de **stock bajo**
- Reporte de catálogo y valorización del inventario
