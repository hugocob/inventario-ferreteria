from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")

class Repository(ABC, Generic[T]):
    @abstractmethod
    def save(self, entity: T) -> T: ...

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[T]: ...

    @abstractmethod
    def find_all(self) -> List[T]: ...
