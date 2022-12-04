PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
CREATE TABLE clientes (
             cedula INTEGER PRIMARY KEY,
             nombre TEXT NOT NULL,
             apellido1 TEXT NOT NULL,
             apellido2 TEXT,
             edad INTEGER NOT NULL,
             direccion TEXT NOT NULL,
             telefono TEXT NOT NULL UNIQUE,
             fecha_nacimiento TEXT NOT NULL,
             email TEXT NOT NULL UNIQUE,
             sexo TEXT NOT NULL 
);
INSERT INTO "clientes" VALUES(1,'Nombre','Primer Apellido','Segundo Apellido',39,'Direccion','Telefono','01/01/2000','E-mail','Femenino');
INSERT INTO "clientes" VALUES(304640365,'Albin','Vazquez','Solano',25,'Cachi','64610845','18/08/1992','abvazquezs26@gmail.com','Masculino');
CREATE TABLE usuarios (
             usuario TEXT PRIMARY KEY,
             clave TEXT NOT NULL,
             cliente INTEGER NOT NULL,
             FOREIGN KEY (cliente) REFERENCES clientes(cedula) 
);
INSERT INTO "usuarios" VALUES('admin','admin',304640365);
INSERT INTO "usuarios" VALUES('progra','clave',1);
CREATE TABLE categorias (
             cod_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre TEXT NOT NULL UNIQUE,
             descripcion TEXT NOT NULL 
);
INSERT INTO "categorias" VALUES(1,'Catg. 1','Descrip. 1');
CREATE TABLE editoriales (
             cod_editorial INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre TEXT NOT NULL UNIQUE,
             descripcion TEXT NOT NULL,
             direccion TEXT NOT NULL,
             email TEXT NOT NULL 
);
INSERT INTO "editoriales" VALUES(1,'Edit. 1','Descrip. 1','Dir. 1','email');
CREATE TABLE autores (
             cod_autor INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre TEXT NOT NULL,
             apellido1 TEXT NOT NULL,
             apellido2 TEXT 
);
INSERT INTO "autores" VALUES(1,'Autor 1','Aplld. 1','Aplld. 2');
INSERT INTO "autores" VALUES(2,'Autor 2','Aplld. 1','Aplld. 2');
CREATE TABLE libros (
             cod_libro INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre TEXT NOT NULL UNIQUE,
             descripcion TEXT NOT NULL,
             autor INTEGER,
             categoria INTEGER,
             editorial INTEGER,
             FOREIGN KEY (autor) REFERENCES autores(cod_autor),
             FOREIGN KEY (categoria) REFERENCES categorias(cod_categoria),
             FOREIGN KEY (editorial) REFERENCES editoriales(cod_editorial)
);
INSERT INTO "libros" VALUES(1,'Libro 1','Descp. 1',2,1,1);
INSERT INTO "libros" VALUES(2,'Libro 2','Descp. 2',1,1,1);
INSERT INTO "libros" VALUES(3,'Libro 3','Descp. 3',2,1,1);
CREATE TABLE cantidades (
             libro INTEGER PRIMARY KEY,
             cantidad INTEGER DEFAULT 5,
             FOREIGN KEY (libro) REFERENCES libros(cod_libro)
);
INSERT INTO "cantidades" VALUES(1,3);
INSERT INTO "cantidades" VALUES(2,4);
INSERT INTO "cantidades" VALUES(3,4);
INSERT INTO "cantidades" VALUES(4,5);
INSERT INTO "cantidades" VALUES(5,5);
INSERT INTO "cantidades" VALUES(6,5);
INSERT INTO "cantidades" VALUES(7,4);
CREATE TABLE prestamos (
             cod_prestamo INTEGER PRIMARY KEY AUTOINCREMENT,
             cliente INTEGER NOT NULL,
             libro INTEGER NOT NULL,
             fecha_prestamo TEXT NOT NULL, 
             fecha_devolucion TEXT NOT NULl,
             FOREIGN KEY (cliente) REFERENCES clientes(cedula),
             FOREIGN KEY (libro) REFERENCES libros(cod_libro)
);
INSERT INTO "prestamos" VALUES(18,1,1,'2018-08-11','2018-08-14');
INSERT INTO "prestamos" VALUES(19,1,7,'2018-08-11','2018-08-14');
INSERT INTO "prestamos" VALUES(20,304640365,1,'2018-08-08','2018-08-11');
INSERT INTO "prestamos" VALUES(21,304640365,3,'2018-08-11','2018-08-14');
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('editoriales',1);
INSERT INTO "sqlite_sequence" VALUES('categorias',1);
INSERT INTO "sqlite_sequence" VALUES('autores',2);
INSERT INTO "sqlite_sequence" VALUES('libros',7);
INSERT INTO "sqlite_sequence" VALUES('prestamos',21);
CREATE TRIGGER insertCantidad AFTER INSERT ON libros
BEGIN
    INSERT INTO cantidades (libro) VALUES (new.cod_libro);
END;
CREATE VIEW vistaLibros AS
select l.cod_libro, l.nombre, l.descripcion, a.nombre, c.nombre, e.nombre, cd.cantidad from autores a, categorias c, editoriales e, cantidades cd inner join libros l on l.autor=a.cod_autor and l.categoria=c.cod_categoria and l.editorial=e.cod_editorial and cd.libro=l.cod_libro;
CREATE TRIGGER updateCantidad AFTER INSERT ON prestamos
BEGIN
       UPDATE cantidades SET cantidad = cantidad-1 WHERE libro=new.libro;
END;
CREATE VIEW vistaPrestamos AS
select cod_prestamo, cliente, nombre, fecha_prestamo, fecha_devolucion from libros inner join prestamos on cod_libro=libro;
COMMIT;
