CREATE TABLE usuario (
    id_usuario     INT            PRIMARY KEY AUTO_INCREMENT,
    nombre         VARCHAR(50)    NOT NULL,
    apellido1      VARCHAR(50)    NOT NULL,
    apellido2      VARCHAR(50),
    email          VARCHAR(100)   NOT NULL UNIQUE,
    contrasena     VARCHAR(100)   NOT NULL,
    is_admin          BOOLEAN        NOT NULL DEFAULT FALSE
);

CREATE TABLE cesta (
    id_cesta       INT            PRIMARY KEY AUTO_INCREMENT,
    id_usuario     INT            NOT NULL UNIQUE,
    fecha_creacion DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
      ON DELETE CASCADE
);

CREATE TABLE productos (
    id_producto    INT            PRIMARY KEY AUTO_INCREMENT,
    nombre         VARCHAR(100)   NOT NULL, 
    tipo_producto  ENUM('chico', 'chica', 'unisex') NOT NULL
);

CREATE TABLE producto_imagenes (
    id_imagen      INT            PRIMARY KEY AUTO_INCREMENT,
    id_producto    INT            NOT NULL,
    imagen_url     VARCHAR(255)   NOT NULL,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto) ON DELETE CASCADE
);


CREATE TABLE producto_variantes (
    id_variantes   INT            PRIMARY KEY AUTO_INCREMENT,
    id_producto    INT            NOT NULL,
    color          VARCHAR(50),
    talla          VARCHAR(10),
    stock          INT            NOT NULL DEFAULT 0,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto) ON DELETE CASCADE
);

CREATE TABLE cesta_productos (
    id_cesta       INT            NOT NULL,
    id_variantes   INT            NOT NULL,
    cantidad       INT            NOT NULL DEFAULT 1,
    PRIMARY KEY (id_cesta, id_variantes),
    FOREIGN KEY (id_cesta) REFERENCES cesta(id_cesta) ON DELETE CASCADE,
    FOREIGN KEY (id_variantes) REFERENCES producto_variantes(id_variantes) ON DELETE CASCADE
);

CREATE TABLE categorias (
    id_categoria   INT            PRIMARY KEY AUTO_INCREMENT,
    nombre         VARCHAR(100)   NOT NULL
);

CREATE TABLE producto_categoria (
    id_producto    INT            NOT NULL,
    id_categoria   INT            NOT NULL,
    PRIMARY KEY (id_producto, id_categoria),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto) ON DELETE CASCADE,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria) ON DELETE CASCADE
);

CREATE TABLE tiendas (
    id_tienda      INT            PRIMARY KEY AUTO_INCREMENT,
    provincia      VARCHAR(100),
    ciudad         VARCHAR(100),
    codigo_postal  VARCHAR(10)
);

CREATE TABLE pedido (
    id_pedido      INT PRIMARY KEY AUTO_INCREMENT,
    nombre         VARCHAR(100)   NOT NULL,
    apellido1      VARCHAR(50)    NOT NULL,
    apellido2      VARCHAR(50)    NOT NULL,
    estado         VARCHAR(50),
    tipo_pedido    VARCHAR(50),
    fecha          DATE           NOT NULL,
    id_usuario     INT            NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE
);

CREATE TABLE pedido_productos (
    id_pedido      INT            NOT NULL,
    id_variantes   INT            NOT NULL,
    cantidad       INT            NOT NULL DEFAULT 1,
    PRIMARY KEY (id_pedido, id_variantes),
    FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido) ON DELETE CASCADE,
    FOREIGN KEY (id_variantes) REFERENCES producto_variantes(id_variantes) ON DELETE RESTRICT
);

CREATE TABLE pedido_tienda (
    id_pedido      INT            NOT NULL,
    id_tienda      INT            NOT NULL,
    PRIMARY KEY (id_pedido, id_tienda),
    FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido) ON DELETE CASCADE,
    FOREIGN KEY (id_tienda) REFERENCES tiendas(id_tienda) ON DELETE RESTRICT
);

CREATE TABLE detalles_pedido (
    id_pedido      INT            PRIMARY KEY,
    tarjeta        VARCHAR(20)    NOT NULL,
    fecha_caducidad DATE          NOT NULL,
    csv            VARCHAR(4)     NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido) ON DELETE CASCADE
);

CREATE TABLE devoluciones (
    id_devolucion  INT            PRIMARY KEY AUTO_INCREMENT,
    descripcion    TEXT,
    id_pedido      INT            UNIQUE,
    FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido) ON DELETE CASCADE
);



