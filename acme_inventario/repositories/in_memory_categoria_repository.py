from __future__ import annotations
from typing import Dict, List, Optional
from ..interfaces.repository import Repository
from ..models.categoria import Categoria

class InMemoryCategoriaRepository(Repository[Categoria]):
    def __init__(self) -> None:
        self._data: Dict[str, Categoria] = {}

    def save(self, entity: Categoria) -> Categoria:
        self._data[entity.id] = entity
        return entity

    def find_by_id(self, id: str) -> Optional[Categoria]:
        return self._data.get(id)

    def find_all(self) -> List[Categoria]:
        return list(self._data.values())
