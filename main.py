from acme_inventario.repositories.in_memory_categoria_repository import InMemoryCategoriaRepository
from acme_inventario.repositories.in_memory_producto_repository import InMemoryProductoRepository
from acme_inventario.services.impl.email_notifier import EmailNotifier
from acme_inventario.services.impl.producto_validator import ProductoValidator
from acme_inventario.services.stock_service import StockService
from acme_inventario.services.reporte_service import ReporteService

def run_demo() -> None:
    categoria_repo = InMemoryCategoriaRepository()
    
    producto_repo = InMemoryProductoRepository()
    notifier = EmailNotifier()
    validator = ProductoValidator()

    stock = StockService(producto_repo, categoria_repo, notifier, validator, umbral_bajo=3)
    reportes = ReporteService(producto_repo, categoria_repo)

    # Crear datos
    cat_herr = stock.crear_categoria("Herramientas")
    cat_pint = stock.crear_categoria("Pinturas")

    martillo = stock.crear_producto("H-001", "Martillo de acero", cat_herr, stock=5, precio=45.0)
    brocha = stock.crear_producto("P-010", "Brocha 2 pulgadas", cat_pint, stock=10, precio=12.5)

    # Operaciones
    stock.vender(martillo, 2)   # queda 3 -> alerta si <= umbral
    stock.vender(martillo, 1)   # queda 2 -> alerta
    stock.reponer(martillo, 10) # queda 12

    print("--- Catálogo ---")
    print(reportes.catalogo())
    print("--- Valorización ---")
    print(f"Q {reportes.valorizacion_inventario():.2f}")

if __name__ == "__main__":
    run_demo()
