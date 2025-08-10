from __future__ import annotations
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def notify(self, to: str, subject: str, body: str) -> None: ...
