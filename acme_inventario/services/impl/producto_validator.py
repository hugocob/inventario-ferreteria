from __future__ import annotations
from ...interfaces.validator import Validator
from ...models.producto import Producto

class ProductoValidator(Validator[Producto]):
    def validate(self, obj: Producto) -> None:
        if not obj.codigo.strip():
            raise ValueError("Código requerido")
        if not obj.nombre.strip():
            raise ValueError("Nombre requerido")
        if obj.precio < 0:
            raise ValueError("Precio no puede ser negativo")
        if obj.stock < 0:
            raise ValueError("Stock no puede ser negativo")
