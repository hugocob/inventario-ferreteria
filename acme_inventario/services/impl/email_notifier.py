from __future__ import annotations
from ...interfaces.notifier import Notifier

class EmailNotifier(Notifier):
    def __init__(self, destinatario_alertas: str = "admin@ferreteria.com") -> None:
        self.destinatario_alertas = destinatario_alertas

    def notify(self, to: str, subject: str, body: str) -> None:
        print(f"[EMAIL -> {to}] {subject}: {body}")
