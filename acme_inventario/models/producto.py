from __future__ import annotations
from dataclasses import dataclass
from .base import BaseEntity
from .categoria import Categoria

@dataclass
class Producto(BaseEntity):
    codigo: str = ""
    nombre: str = ""
    categoria: Categoria | None = None
    stock: int = 0
    precio: float = 0.0

    def __str__(self) -> str:
        cat = self.categoria.nombre if self.categoria else "Sin categoría"
        return f"[{self.codigo}] {self.nombre} ({cat}) - stock={self.stock}, precio={self.precio:.2f}"
