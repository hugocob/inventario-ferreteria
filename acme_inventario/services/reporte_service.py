from __future__ import annotations
from ..interfaces.repository import Repository
from ..models.producto import Producto
from ..models.categoria import Categoria

class ReporteService:
    def __init__(self,
                 producto_repo: Repository[Producto],
                 categoria_repo: Repository[Categoria]) -> None:
        self.producto_repo = producto_repo
        self.categoria_repo = categoria_repo

    def catalogo(self) -> str:
        lineas = [str(p) for p in self.producto_repo.find_all()]
        return "\n".join(lineas) if lineas else "Sin productos"

    def valorizacion_inventario(self) -> float:
        return sum(p.precio * p.stock for p in self.producto_repo.find_all())
