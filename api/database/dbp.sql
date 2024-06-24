
create table gender(
    id_gender serial not null,
    gender_name varchar(50) not null,
    constraint pk_gender primary key(id_gender)
);

insert into gender(gender_name) values('Male');
insert into gender(gender_name) values('Female');

create table person(
    id_person serial not null,
    card_id_person varchar(13) not null unique,
    first_name varchar(100) not null,
    last_name varchar(100) not null,
    phone varchar(15) not null,
    address varchar(100) not null,
    gender integer not null,
    date_born date not null,
    constraint pk_person primary key(id_person),
    constraint fk_gender_person foreign key(gender) references gender(id_gender) 
);

insert into person(card_id_person, first_name, last_name, phone, address, gender, date_born) values('1003938410', 'Mario', 'Salazar', '0979432426', 'Ibarra - El Tejar', 1, '1995-02-02');

insert into person(card_id_person, first_name, last_name, phone, address, gender, date_born) values('1003938477', 'Elenita', 'Rueda', '0979432410', 'Ibarra - San Francisco del Tejar', 1, '1995-12-02');

create table rol_user(
    id_rol serial not null,
    rol_name varchar(100) not null,
    constraint pk_rol_user primary key(id_rol)
);



insert into rol_user(rol_name) values('Rol user Manager');
insert into rol_user(rol_name) values('Rol user Employed');
insert into rol_user(rol_name) values('Rol user Secretary');

select*from rol_user;

create table users(
    id_user serial not null,
    user_name varchar(100) not null unique,
    email varchar(100) not null unique,
    password varchar(200) not null,
    login_code varchar(10) not null,
    user_state integer not null,
    register_date date not null,
    person integer not null,
    constraint pk_user primary key(id_user),
    constraint fk_person_user foreign key(person) references person(id_person)
);

insert into users(user_name, email, password, login_code, user_state, register_date, person) values('ADM-1003938410', 'elenitarueda@gmail.com', 'password-elenita', '0000', '1', '2023-04-06', 1);

select*from users;

alter table users add column rol_user integer;
update users set rol_user = 1 where id_user = 1;

alter table users 
add constraint fk_rol_users foreign key(rol_user) references rol_user(id_rol);

/*

conda create -n nombreenv python=x.x
source activate nombreenv
conda env list
Para instalar paquetes dentro de nuestro entorno virtual podemos hacerlo mediante pip o con el instalador de anaconda.

pip install nombredelpaquete
o bien

conda install nombredelpaquete
De igual manera podemos ver los paquetes y la versión que tiene instalado nuestro entorno

conda list -n nombreenv

*/

-- Language Database
-- Language programming
-- Language Design

create table language_type(
	id_langtype serial not null,
	langtype_name varchar(25) not null,
	constraint pk_idlt primary key(id_langtype)
);

insert into language_type(langtype_name) values('Language Database');
insert into language_type(langtype_name) values('Language programming');
insert into language_type(langtype_name) values('Language Design');



create table language_programming(
	id_language serial not null,
	language_name varchar(50) not null,
	language_type integer not null,
	image varchar(100) not null,	
	constraint pk_language primary key(id_language),
	constraint fk_lt foreign key(language_type) references language_type(id_langtype)
);

insert into language_programming (language_name, language_type, image) values ('MySQL 5.7 / 8.0', 1, 'https://bit.ly/41HBY09');
insert into language_programming (language_name, language_type, image) values ('MariaDB 10.5', 1, 'https://bit.ly/3UIHEVi');
insert into language_programming (language_name, language_type, image) values ('PostgreSQL 13.5 / 12.7 / 11.12', 1, 'https://bit.ly/3A62sMS');
insert into language_programming (language_name, language_type, image) values ('SQL Server 2019 XE / 2017 XE', 1, 'https://bit.ly/3A62sMS');
insert into language_programming (language_name, language_type, image) values ('Oracle 11g XE', 1, 'https://bit.ly/3UIHEVi');

insert into language_programming (language_name, language_type, image) values ('Python', 2, 'https://bit.ly/3mHTMcq');
insert into language_programming (language_name, language_type, image) values ('C#', 2, 'https://bit.ly/40ivgfQ');
insert into language_programming (language_name, language_type, image) values ('C++', 2, 'https://bit.ly/43Kx6c8');
insert into language_programming (language_name, language_type, image) values ('JavaScript', 2, 'https://bit.ly/3La2hX3');
insert into language_programming (language_name, language_type, image) values ('PHP', 2, 'https://bit.ly/40lbUqu');
insert into language_programming (language_name, language_type, image) values ('Java', 2, 'https://bit.ly/3A6kH4O');
insert into language_programming (language_name, language_type, image) values ('Go', 2, 'https://bit.ly/3MTsjzb');
insert into language_programming (language_name, language_type, image) values ('Ruby', 2, 'https://bit.ly/3N1sUyK');

insert into language_programming (language_name, language_type, image) values ('HTML 5', 3, 'https://bit.ly/3KLovgM');
insert into language_programming (language_name, language_type, image) values ('CSS 3', 3, 'https://bit.ly/41xV1tw');


create table knowledge_level(
	id_knowledge_level serial not null,
	name_levknowledge varchar(50) not null,
	constraint pk_knowledge_level primary key(id_knowledge_level)
);

insert into knowledge_level(name_levknowledge) values('None Knowledge');
insert into knowledge_level(name_levknowledge) values('Slow Knowledge');
insert into knowledge_level(name_levknowledge) values('Middle Knowledge');
insert into knowledge_level(name_levknowledge) values('High Knowledge');
insert into knowledge_level(name_levknowledge) values('Expert Knowledge');


create table language_learned(
	id_langlearn serial not null,
	description varchar(500) not null,
	knowledge_level integer not null,
	language_programming integer not null,
	user_language integer not null,
	constraint pk_language_learned primary key(id_langlearn),
	constraint fk_lk_ll foreign key(knowledge_level) references knowledge_level(id_knowledge_level),
	constraint fk_lp_ll foreign key(language_programming) references language_programming(id_language),
	constraint fk_uc_ll foreign key(user_language) references users(id_user)
);

select*from language_learned;

insert into language_learned (description, knowledge_level, language_programming, user_language)
values('Python es un lenguaje de programación de alto nivel y de propósito general. Puede utilizarse 
para diversas tareas, desde el análisis y la visualización de datos hasta el desarrollo web, la creación de prototipos y la automatización.', 3, 6, 1);

insert into language_learned (description, knowledge_level, language_programming, user_language)
values('JavaScript es un lenguaje de programación ligero que los desarrolladores web suelen utilizar para crear interacciones más dinámicas al 
desarrollar páginas web, aplicaciones, servidores e incluso juegos.', 4, 9, 1);

insert into language_learned (description, knowledge_level, language_programming, user_language)
values('El Preprocesador de Hipertexto (PHP – Hypertext Preprocessor) es un lenguaje de scripting del lado del servidor, gratuito y de código abierto, utilizado 
muy comúnmente en el desarrollo web. Según Web Technology Surveys, PHP es utilizado por el 77,6% de todos los sitios web.', 3, 10, 1);

insert into language_learned (description, knowledge_level, language_programming, user_language)
values('Java es un lenguaje de programación propietario de Oracle. Es un lenguaje de programación de alto nivel y de propósito general que permite a los 
programadores crear todo tipo de aplicaciones con facilidad.', 4, 11, 1);

insert into language_learned (description, knowledge_level, language_programming, user_language)
values('Go, o Golang fue creado para desarrollar APIs, aplicaciones de escritorio basadas en GUI y aplicaciones web. Aunque es un lenguaje joven, 
Go es uno de los lenguajes de programación de más rápido crecimiento.', 5, 12, 1);


insert into language_learned (description, knowledge_level, language_programming, user_language)
values('MySQL es un sistema de administración de bases de datos relacionales. Es un software de código abierto desarrollado por Oracle. 
Se considera como la base de datos de código abierto más utilizada en el mundo.', 3, 1, 1);
insert into language_learned (description, knowledge_level, language_programming, user_language)
values('PostgreSQL es un sistema de bases de datos de código abierto, altamente estable, que proporciona soporte a diferentes funciones de SQL, como claves 
foráneas, subconsultas, disparadores y diferentes tipos y funciones definidas por el usuario. Además, aumenta el lenguaje SQL 
ofreciendo varias funciones que escalan y reservan meticulosamente las cargas de trabajo de datos.', 5, 3, 1);
insert into language_learned (description, knowledge_level, language_programming, user_language)
values('Microsoft SQL Server es uno de los principales sistemas de gestión de bases de datos relacional del mercado que presta servicio a un 
amplio abanico de aplicaciones de software destinadas a la inteligencia empresarial y análisis sobre entornos corporativos.
Basada en el lenguaje Transact-SQL, incorpora un conjunto de extensiones de programación propias de lenguaje estándar y 
su aplicación está disponible para usarse tanto a nivel on premise o bajo una modalidad cloud.', 4, 4, 1);

insert into language_learned (description, knowledge_level, language_programming, user_language)
values('HTML es el lenguaje con el que se define el contenido de las páginas web. Básicamente se trata de un conjunto de etiquetas que sirven para definir el texto y otros 
elementos que compondrán una página web, como imágenes, listas, vídeos, etc.', 4, 14, 1);
insert into language_learned (description, knowledge_level, language_programming, user_language)
values('El CSS es lo que se llama un lenguaje de hojas de estilo en cascada y se utiliza para estilizar elementos escritos en un lenguaje de marcado como HTML. 
Separa el contenido de la representación visual del sitio.', 5, 15, 1);

select*from knowledge_level;


update knowledge_level set name_levknowledge = 'Zero level of knowledge' where id_knowledge_level = 1;
update knowledge_level set name_levknowledge = 'Basic knowledge level' where id_knowledge_level = 2;
update knowledge_level set name_levknowledge = 'Intermediate knowledge level' where id_knowledge_level = 3;
update knowledge_level set name_levknowledge = 'Advanced intermediate knowledge level' where id_knowledge_level = 4;
update knowledge_level set name_levknowledge = 'Advanced level of knowledge' where id_knowledge_level = 5;
update knowledge_level set name_levknowledge = 'Expert knowledge level' where id_knowledge_level = 6;

select*from language_learned;

create table education (
id_education serial not null,
institution varchar(100) not null,
major varchar(100) not null,
year_start integer not null,
year_end integer not null,
description varchar(500) not null,
user_education integer not null,
constraint pk_education primary key(id_education),
constraint fk_user_education foreign key(user_education) references users(id_user)
);

drop table language_learned;
drop table knowledge_level;
drop table language_programming;
drop table language_type;

