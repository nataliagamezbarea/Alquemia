from flask import render_template, request
from sqlalchemy import func
from backend.Modelos import Producto, ProductoVariante
from backend.Modelos.database import db
from math import ceil

def catalogo():
    pagina_actual = request.args.get('pagina', 1, type=int)
    productos_por_pagina = 42

    productos_paginados = db.session.query(Producto).join(Producto.variantes).join(ProductoVariante.color).order_by(func.random()).paginate(page=pagina_actual, per_page=productos_por_pagina)

    for producto in productos_paginados.items:
        producto.color_urls = list({
            variante.color.img_color
            for variante in producto.variantes
            if variante.color and variante.color.img_color
        })

    total_paginas = ceil(Producto.query.count() / productos_por_pagina)

    return render_template(
        'user/catalogo.html',
        productos=productos_paginados.items,
        pagina_actual=pagina_actual,
        total_paginas=total_paginas,
    )
