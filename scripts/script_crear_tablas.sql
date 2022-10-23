CREATE TABLE usuarios (
	usuario varchar(10),
	pass varchar(20),
	PRIMARY KEY (usuario)
); 

CREATE TABLE alumno (
	usuario varchar(10),
	id_curso varchar(10) not null,
	usuario_pictograma boolean not null default 0,
	tipo_discapacidad varchar(20) not null default 'ninguna',
	PRIMARY KEY (usuario)
); 

CREATE TABLE profesor (
	usuario varchar(10),
	id_curso varchar(10),
	PRIMARY KEY (usuario)
); 

CREATE TABLE admin (
	usuario varchar(10),
	PRIMARY KEY (usuario)
); 

CREATE TABLE curso (
	id_curso varchar(10),
	tutor varchar(10) not null,
	PRIMARY KEY (id_curso)
); 

CREATE TABLE mensaje (
	id_mensaje varchar(20),
	id_chat varchar(10) not null,
	PRIMARY KEY (id_mensaje)
); 

CREATE TABLE chat (
	id_chat varchar(10),
	PRIMARY KEY (id_chat)
); 

CREATE TABLE tarea (
	id_tarea varchar(10),
	tipo_tarea varchar(20),
	descripcion varchar(140),
	id_mensaje varchar(20),	
	PRIMARY KEY (id_tarea)
);

CREATE TABLE comanda (
	id_tarea varchar(10),
	material varchar(20),
	cantidad (int),
	aula varchar(10),
	PRIMARY KEY (id_tarea)
);

CREATE TABLE menus (
	id_tarea varchar(10),
	tipo varchar(20),
	postre varchar(140),
	cantidad (int),
	cantidad_postre (int),
	PRIMARY KEY (id_tarea)
); 




