-- Tabla de usuarios
CREATE TABLE usuario (
    id_usuario     INT PRIMARY KEY AUTO_INCREMENT,
    nombre         VARCHAR(50) NOT NULL,
    apellido1      VARCHAR(50) NOT NULL,
    apellido2      VARCHAR(50),
    email          VARCHAR(100) NOT NULL UNIQUE,
    contrasena     VARCHAR(100) NOT NULL,
    is_admin       BOOLEAN NOT NULL DEFAULT FALSE
);

-- Tabla de colores
CREATE TABLE colores (
    id_color       INT PRIMARY KEY AUTO_INCREMENT,
    color          VARCHAR(50) NOT NULL UNIQUE,
    img_color      VARCHAR(255)
);

-- Tabla de tallas
CREATE TABLE tallas (
    id_talla       INT PRIMARY KEY AUTO_INCREMENT,
    talla          VARCHAR(10) NOT NULL UNIQUE
);

-- Tabla de secciones
CREATE TABLE secciones (
    id_seccion     INT PRIMARY KEY AUTO_INCREMENT,
    nombre         ENUM('hombre', 'mujer', 'niño', 'niña', 'unisex') NOT NULL
);

-- Tabla de productos
CREATE TABLE productos (
    id_producto    INT PRIMARY KEY AUTO_INCREMENT,
    nombre         VARCHAR(100) NOT NULL,
    id_seccion     INT NOT NULL,
    precio         DECIMAL(10,2) NOT NULL,
    descripcion    TEXT NOT NULL,
    FOREIGN KEY (id_seccion) REFERENCES secciones(id_seccion) ON DELETE CASCADE
);

-- Tabla de imágenes de productos con asociación directa a color
CREATE TABLE producto_imagenes (
    id_imagen      INT PRIMARY KEY AUTO_INCREMENT,
    id_producto    INT NOT NULL,
    id_color       INT NOT NULL,
    imagen_url     VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto) ON DELETE CASCADE,
    FOREIGN KEY (id_color) REFERENCES colores(id_color) ON DELETE CASCADE
);

-- Tabla de variantes de productos
CREATE TABLE producto_variantes (
    id_variantes   INT PRIMARY KEY AUTO_INCREMENT,
    id_producto    INT NOT NULL,
    id_color       INT NOT NULL,
    id_talla       INT NOT NULL,
    stock          INT NOT NULL DEFAULT 0,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto) ON DELETE CASCADE,
    FOREIGN KEY (id_color) REFERENCES colores(id_color) ON DELETE CASCADE,
    FOREIGN KEY (id_talla) REFERENCES tallas(id_talla) ON DELETE CASCADE
);

-- Tabla de cestas
CREATE TABLE cesta (
    id_cesta       INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario     INT NOT NULL UNIQUE,
    fecha_creacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE
);

-- Tabla de productos en la cesta
CREATE TABLE cesta_productos (
    id_cesta       INT NOT NULL,
    id_variantes   INT NOT NULL,
    cantidad       INT NOT NULL DEFAULT 1,
    PRIMARY KEY (id_cesta, id_variantes),
    FOREIGN KEY (id_cesta) REFERENCES cesta(id_cesta) ON DELETE CASCADE,
    FOREIGN KEY (id_variantes) REFERENCES producto_variantes(id_variantes) ON DELETE CASCADE
);

-- Tabla de métodos de pago
CREATE TABLE metodos_pago (
    id_metodo         INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario        INT NOT NULL,
    tipo              ENUM('tarjeta', 'paypal', 'otro') NOT NULL DEFAULT 'tarjeta',
    tarjeta           VARCHAR(20) NOT NULL,
    fecha_caducidad   DATE NOT NULL,
    csv               VARCHAR(4) NOT NULL,
    is_default        BOOLEAN NOT NULL DEFAULT FALSE,
    created_at        DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at        DATETIME NOT NULL ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE
);

-- Tabla de categorías
CREATE TABLE categorias (
    id_categoria   INT PRIMARY KEY AUTO_INCREMENT,
    nombre         VARCHAR(100) NOT NULL
);

-- Tabla de relación producto-categoría
CREATE TABLE producto_categoria (
    id_producto    INT NOT NULL,
    id_categoria   INT NOT NULL,
    PRIMARY KEY (id_producto, id_categoria),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto) ON DELETE CASCADE,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria) ON DELETE CASCADE
);

-- Tabla de tiendas
CREATE TABLE tiendas (
    id_tienda      INT PRIMARY KEY AUTO_INCREMENT,
    provincia      VARCHAR(100),
    ciudad         VARCHAR(100),
    codigo_postal  VARCHAR(10)
);

-- Tabla de pedidos
CREATE TABLE pedido (
    id_pedido          INT PRIMARY KEY AUTO_INCREMENT,
    nombre_envio       VARCHAR(100) NOT NULL,
    apellido1_envio    VARCHAR(50) NOT NULL,
    apellido2_envio    VARCHAR(50) NOT NULL,
    estado             ENUM('pendiente', 'procesando', 'enviado', 'entregado', 'cancelado') NOT NULL DEFAULT 'pendiente',
    tipo_pedido        ENUM('domicilio', 'tienda') NOT NULL DEFAULT 'domicilio',
    fecha              DATE NOT NULL,
    id_usuario         INT NOT NULL,
    id_metodo          INT,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_metodo) REFERENCES metodos_pago(id_metodo) ON DELETE SET NULL
);

-- Tabla de productos en el pedido
CREATE TABLE pedido_productos (
    id_pedido      INT NOT NULL,
    id_variantes   INT NOT NULL,
    cantidad       INT NOT NULL DEFAULT 1,
    total_producto  DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    PRIMARY KEY (id_pedido, id_variantes),
    FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido) ON DELETE CASCADE,
    FOREIGN KEY (id_variantes) REFERENCES producto_variantes(id_variantes) ON DELETE RESTRICT
);

-- Asociación de producto del pedido con tienda para recogida
CREATE TABLE pedido_producto_tienda (
    id_pedido      INT NOT NULL,
    id_variantes   INT NOT NULL,
    id_tienda      INT NOT NULL,
    PRIMARY KEY (id_pedido, id_variantes),
    FOREIGN KEY (id_pedido, id_variantes) REFERENCES pedido_productos(id_pedido, id_variantes) ON DELETE CASCADE,
    FOREIGN KEY (id_tienda) REFERENCES tiendas(id_tienda) ON DELETE RESTRICT
);

-- Tabla de devoluciones
CREATE TABLE devoluciones (
    id_devolucion  INT PRIMARY KEY AUTO_INCREMENT,
    descripcion    TEXT,
    id_pedido      INT NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido) ON DELETE CASCADE
);