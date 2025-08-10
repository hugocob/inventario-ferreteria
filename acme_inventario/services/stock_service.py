from __future__ import annotations
from ..interfaces.repository import Repository
from ..interfaces.notifier import Notifier
from ..interfaces.validator import Validator
from ..models.producto import Producto
from ..models.categoria import Categoria

class StockService:
    def __init__(self,
                 producto_repo: Repository[Producto],
                 categoria_repo: Repository[Categoria],
                 notifier: Notifier,
                 producto_validator: Validator[Producto],
                 umbral_bajo: int = 5) -> None:
        self.producto_repo = producto_repo
        self.categoria_repo = categoria_repo
        self.notifier = notifier
        self.producto_validator = producto_validator
        self.umbral_bajo = umbral_bajo

    def crear_categoria(self, nombre: str) -> Categoria:
        return self.categoria_repo.save(Categoria(nombre=nombre))

    def crear_producto(self, codigo: str, nombre: str, categoria: Categoria, stock: int, precio: float) -> Producto:
        p = Producto(codigo=codigo, nombre=nombre, categoria=categoria, stock=stock, precio=precio)
        self.producto_validator.validate(p)
        return self.producto_repo.save(p)

    def reponer(self, producto: Producto, cantidad: int) -> Producto:
        if cantidad <= 0:
            raise ValueError("Cantidad debe ser positiva")
        producto.stock += cantidad
        return self.producto_repo.save(producto)

    def vender(self, producto: Producto, cantidad: int) -> Producto:
        if cantidad <= 0:
            raise ValueError("Cantidad debe ser positiva")
        if producto.stock < cantidad:
            raise ValueError("Stock insuficiente")
        producto.stock -= cantidad
        actualizado = self.producto_repo.save(producto)
        if actualizado.stock <= self.umbral_bajo:
            self.notifier.notify("compras@ferreteria.com",
                                 "Alerta de stock bajo",
                                 f"Producto {actualizado.nombre} ({actualizado.codigo}) en {actualizado.stock} unidades.")
        return actualizado
