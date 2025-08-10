from __future__ import annotations
from dataclasses import dataclass
from .base import BaseEntity

@dataclass
class Categoria(BaseEntity):
    nombre: str = ""

    def __str__(self) -> str:
        return self.nombre
