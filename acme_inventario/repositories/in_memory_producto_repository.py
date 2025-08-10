from __future__ import annotations
from typing import Dict, List, Optional
from ..interfaces.repository import Repository
from ..models.producto import Producto

class InMemoryProductoRepository(Repository[Producto]):
    def __init__(self) -> None:
        self._data: Dict[str, Producto] = {}

    def save(self, entity: Producto) -> Producto:
        self._data[entity.id] = entity
        return entity

    def find_by_id(self, id: str) -> Optional[Producto]:
        return self._data.get(id)

    def find_all(self) -> List[Producto]:
        return list(self._data.values())

    # extra util
    def find_by_codigo(self, codigo: str) -> Optional[Producto]:
        for p in self._data.values():
            if p.codigo == codigo:
                return p
        return None
