PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;

CREATE TABLE usuarios ( 
             id integer primary key autoincrement,
             nombre text not null, 
             apellidos text, 
             email text not null, 
             passwd text not null,
             fecha numeric, 
             constraint uqEmail unique(email)
);
             
CREATE TABLE notas ( 
             id integer primary key autoincrement,
             usuarioId integer not null, 
             titulo text not null, 
             descripcion text not null, 
             fecha numeric, 
       	     foreign key (usuarioId) references usuarios(id) 
);

commit; 
