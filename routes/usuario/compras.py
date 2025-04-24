from flask import redirect, render_template, session, url_for
from datetime import datetime, timedelta
from backend.Modelos import Pedido, ProductoColor

def compras():
    user_id = session.get("user")
    if not user_id:
        return redirect(url_for("login"))

    pedidos = Pedido.query.filter_by(id_usuario=user_id).all()

    for pedido in pedidos:
        fecha_pedido = pedido.fecha
        pedido.fecha_entrega_min = fecha_pedido + timedelta(days=3)
        pedido.fecha_entrega_max = fecha_pedido + timedelta(days=5)
        pedido.dias_restantes = (pedido.fecha_entrega_max - datetime.now().date()).days

        for pedido_producto in pedido.pedido_productos:
            producto_variante = pedido_producto.producto_variante
            color_imagen = ProductoColor.query.filter_by(id_producto=producto_variante.producto.id_producto, color_id=producto_variante.color.id_color).first()
            pedido_producto.color_imagen = color_imagen

    return render_template('user/usuario_configuracion/compras.html', pedidos=pedidos)
