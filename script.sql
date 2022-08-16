CREATE DATABASE tbSistemaImc;
USE tbSistemaImc;

CREATE TABLE tbImc ( 
    idImc INT PRIMARY KEY AUTO_INCREMENT,
    alturaUsuario VARCHAR(4) , 
    pesoUsuario SMALLINT , 
    imcUsuario SMALLINT 
);