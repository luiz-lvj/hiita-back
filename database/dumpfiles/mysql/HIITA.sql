CREATE DATABASE IF NOT EXISTS `hiita` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `hiita`;

CREATE TABLE IF NOT EXISTS `USERNAME`(
	`ID` int(8) NOT NULL AUTO_INCREMENT,
	`CPF` int NOT NULL,
	`NOME` varchar(100) NOT NULL,
	`EMAIL` varchar(100) NOT NULL,
	`SENHA` varchar(100) NOT NULL,
    PRIMARY KEY(`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

/*****************************************/

CREATE TABLE IF NOT EXISTS `PERSONAL`(
	`ID` int(8) NOT NULL AUTO_INCREMENT,
	`CREF` int NOT NULL,
	`NOME` varchar(100) NOT NULL,
    PRIMARY KEY(`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*****************************************/



CREATE TABLE IF NOT EXISTS `FICHA`(
	`ID` int(8) NOT NULL AUTO_INCREMENT,
	`USERNAME_ID` int(8) NOT NULL,
	`PERSONAL_ID` int(8) NOT NULL,
	`TITULO` varchar(100) NOT NULL,
	`DESCRICAO` varchar(100) NOT NULL,
	CONSTRAINT FOREIGN KEY (`USERNAME_ID`)
	REFERENCES `USERNAME` (`ID`),
	CONSTRAINT FOREIGN KEY (`PERSONAL_ID`)
	REFERENCES `PERSONAL` (`ID`),
    PRIMARY KEY(`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

/*****************************************/
CREATE TABLE IF NOT EXISTS `TREINO`(
	`ID` int(8) NOT NULL AUTO_INCREMENT,
	`USERNAME_ID` int(8) NOT NULL,
	`FICHA_ID` int(8) NOT NULL,
	`DATAHORA` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT FOREIGN KEY (`FICHA_ID`)
	REFERENCES `FICHA` (`ID`),
	CONSTRAINT FOREIGN KEY (`USERNAME_ID`)
	REFERENCES `USERNAME` (`ID`),
    PRIMARY KEY(`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

/*****************************************/
CREATE TABLE IF NOT EXISTS `EXERCICIO`(
	`ID` int(8) NOT NULL AUTO_INCREMENT,
	`FICHA_ID` int NOT NULL,										
	`NOME_EXERCICIO` varchar(100) NOT NULL,
	`DESCRICAO` varchar(100) NOT NULL,
	CONSTRAINT FOREIGN KEY (`FICHA_ID`)
	REFERENCES `FICHA` (`ID`),
    PRIMARY KEY(`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;


/*****************************************/
INSERT INTO `USERNAME` (`ID`,`CPF`,`NOME`,`EMAIL`,`SENHA`) VALUES 
(1, 12345678, 'RYU', 'AAAA@A.com', '2013a0402'),
(2, 25423544, 'LUCA', 'BBBB@A.com','2014B0402'),
(3, 33333312, 'BENICIO','CCCC@A.com','2015C0402'),
(4, 10, 'NEYMAR', 'neymarjr@gmail.com', 'hexa');

/*****************************************/

INSERT INTO `PERSONAL` (`ID`,`CREF`,`NOME`) VALUES
(1, 876543, 'Jefferson'),
(2, 546844, 'Pedro'),
(3, 357664, 'Matheus'),
(NULL, 101011, 'Rodrigo Lasmar'),
(NULL, 101010, 'Tite');

/*****************************************/

INSERT INTO `FICHA` (`ID`,`USERNAME_ID`,`PERSONAL_ID`,`TITULO`,`DESCRICAO`) VALUES 
(1, 1, 1, 'flexao', 'tipo aberta'),
(2, 2, 2, 'abdominal','tipo TACF'),
(3, 3, 3, 'barra','do tipo supinada'),
(NULL, 4, 4, 'Fisioterapia', 'Recuperação do tornozelo'),
(NULL, 4, 5, 'Futebol 1', 'Treino Tatico'),
(NULL, 4, 5, 'Futebol 2', 'Treino Fisico');


/*****************************************/

INSERT INTO `EXERCICIO` (`ID`,`FICHA_ID`,`NOME_EXERCICIO`,`DESCRICAO`) VALUES 
(1, 1, 'flexao mao fechada','tipo aberta'),
(2, 2, 'abdominal prancha','tipo TACF'),
(3, 3, 'barra supinada', 'do tipo supinada'),
(NULL, 4, 'Choque Eletrico', '30 min'),
(NULL, 4, 'Alongamento do tornozelo com elastico', '3x10'),
(NULL, 4, 'Piscina', '10 min'),
(NULL, 5, 'Alongamento', '5 min'),
(NULL, 5, 'Aquecimento Bobinho 10x1', '5 min'),
(NULL, 5, 'Aquecimento Bobinho 10x2', '5 min'),
(NULL, 5, 'Posicionamento Tatico 4-4-2', '20x posicionamento de ataque'),
(NULL, 5, 'Posicionamento Tatico 4-4-2', '20x posicionamento de defesa'),
(NULL, 5, 'Posicionamento Tatico 4-3-3', '10x posicionamento de ataque'),
(NULL, 5, 'Posicionamento Tatico 4-3-3', '10x posicionamento de defesa'),
(NULL, 5, 'Treino de penaltis', '10 min'),
(NULL, 5, 'Banheira de gelo', '10 min'),
(NULL, 6, 'Corrida leve', '30 min com 60%VM'),
(NULL, 6, 'Sprint', '10x100m 90%VM'),
(NULL, 6, 'Corrida recuperativa', '5 min trotando'),
(NULL, 6, 'Corrida Moderada', '10x100m 75%VM'),
(NULL, 6, 'Banheira de gelo', '10 min');
/*****************************************/

INSERT INTO TREINO (`ID`,`USERNAME_ID`,`FICHA_ID`,`DATAHORA`) VALUES
(1, 1, 1, '2022-11-20 09:30:00'),
(2, 2, 2, '2022-11-25 19:30:00'),
(3, 3, 3, '2022-11-27 21:30:00');