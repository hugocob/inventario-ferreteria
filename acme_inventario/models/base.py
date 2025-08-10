from __future__ import annotations
from dataclasses import dataclass, field
import uuid

@dataclass
class BaseEntity:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
