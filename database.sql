create database megatron;

create table users (
    id int(5) auto_increment primary key,
    username varchar(50) not null,
    password varchar(70) not null,
    level int(3)
)ENGINE=InnoDB;