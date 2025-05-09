from flask import redirect, render_template, session, url_for
from datetime import datetime, timedelta
from sqlalchemy.orm import joinedload
from backend.Modelos import Pedido, PedidoProducto, ProductoColor, ProductoVariante

def compras():
    user_id = session.get("user")
    if not user_id:
        return redirect(url_for("login"))

    pedidos = Pedido.query.options(joinedload(Pedido.pedido_productos).joinedload(PedidoProducto.producto_variante).joinedload(ProductoVariante.color)).filter_by(id_usuario=user_id).all()

    for pedido in pedidos:
        fecha_pedido = pedido.fecha
        pedido.fecha_entrega_min = fecha_pedido + timedelta(days=3)
        pedido.fecha_entrega_max = fecha_pedido + timedelta(days=5)
        pedido.dias_restantes = (pedido.fecha_entrega_max - datetime.now().date()).days

    return render_template('user/usuario_configuracion/compras.html', pedidos=pedidos)
