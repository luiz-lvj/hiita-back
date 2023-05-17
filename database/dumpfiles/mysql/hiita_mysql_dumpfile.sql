-- MySQL dump 10.13  Distrib 8.0.30, for Linux (x86_64)
--
-- Host: localhost    Database: hiita
-- ------------------------------------------------------
-- Server version	8.0.30-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `EXERCICIO`
--

DROP TABLE IF EXISTS `EXERCICIO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EXERCICIO` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `FICHA_ID` int NOT NULL,
  `NOME_EXERCICIO` varchar(100) NOT NULL,
  `DESCRICAO` varchar(100) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FICHA_ID` (`FICHA_ID`),
  CONSTRAINT `EXERCICIO_ibfk_1` FOREIGN KEY (`FICHA_ID`) REFERENCES `FICHA` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EXERCICIO`
--

LOCK TABLES `EXERCICIO` WRITE;
/*!40000 ALTER TABLE `EXERCICIO` DISABLE KEYS */;
INSERT INTO `EXERCICIO` VALUES (1,1,'flexao mao fechada','tipo aberta'),(2,2,'abdominal prancha','tipo TACF'),(3,3,'barra supinada','do tipo supinada'),(4,4,'Choque Eletrico','30 min'),(5,4,'Alongamento do tornozelo com elastico','3x10'),(6,4,'Piscina','10 min'),(7,5,'Alongamento','5 min'),(8,5,'Aquecimento Bobinho 10x1','5 min'),(9,5,'Aquecimento Bobinho 10x2','5 min'),(10,5,'Posicionamento Tatico 4-4-2','20x posicionamento de ataque'),(11,5,'Posicionamento Tatico 4-4-2','20x posicionamento de defesa'),(12,5,'Posicionamento Tatico 4-3-3','10x posicionamento de ataque'),(13,5,'Posicionamento Tatico 4-3-3','10x posicionamento de defesa'),(14,5,'Treino de penaltis','10 min'),(15,5,'Banheira de gelo','10 min'),(16,6,'Corrida leve','30 min com 60%VM'),(17,6,'Sprint','10x100m 90%VM'),(18,6,'Corrida recuperativa','5 min trotando'),(19,6,'Corrida Moderada','10x100m 75%VM'),(20,6,'Banheira de gelo','10 min');
/*!40000 ALTER TABLE `EXERCICIO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FICHA`
--

DROP TABLE IF EXISTS `FICHA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `FICHA` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `USERNAME_ID` int NOT NULL,
  `PERSONAL_ID` int NOT NULL,
  `TITULO` varchar(100) NOT NULL,
  `DESCRICAO` varchar(100) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `USERNAME_ID` (`USERNAME_ID`),
  KEY `PERSONAL_ID` (`PERSONAL_ID`),
  CONSTRAINT `FICHA_ibfk_1` FOREIGN KEY (`USERNAME_ID`) REFERENCES `USERNAME` (`ID`),
  CONSTRAINT `FICHA_ibfk_2` FOREIGN KEY (`PERSONAL_ID`) REFERENCES `PERSONAL` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FICHA`
--

LOCK TABLES `FICHA` WRITE;
/*!40000 ALTER TABLE `FICHA` DISABLE KEYS */;
INSERT INTO `FICHA` VALUES (1,1,1,'flexao','tipo aberta'),(2,2,2,'abdominal','tipo TACF'),(3,3,3,'barra','do tipo supinada'),(4,4,4,'Fisioterapia','Recuperação do tornozelo'),(5,4,5,'Futebol 1','Treino Tatico'),(6,4,5,'Futebol 2','Treino Fisico');
/*!40000 ALTER TABLE `FICHA` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PERSONAL`
--

DROP TABLE IF EXISTS `PERSONAL`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PERSONAL` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `CREF` int NOT NULL,
  `NOME` varchar(100) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PERSONAL`
--

LOCK TABLES `PERSONAL` WRITE;
/*!40000 ALTER TABLE `PERSONAL` DISABLE KEYS */;
INSERT INTO `PERSONAL` VALUES (1,876543,'Jefferson'),(2,546844,'Pedro'),(3,357664,'Matheus'),(4,101011,'Rodrigo Lasmar'),(5,101010,'Tite');
/*!40000 ALTER TABLE `PERSONAL` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TREINO`
--

DROP TABLE IF EXISTS `TREINO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TREINO` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `USERNAME_ID` int NOT NULL,
  `FICHA_ID` int NOT NULL,
  `DATAHORA` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  KEY `FICHA_ID` (`FICHA_ID`),
  KEY `USERNAME_ID` (`USERNAME_ID`),
  CONSTRAINT `TREINO_ibfk_1` FOREIGN KEY (`FICHA_ID`) REFERENCES `FICHA` (`ID`),
  CONSTRAINT `TREINO_ibfk_2` FOREIGN KEY (`USERNAME_ID`) REFERENCES `USERNAME` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TREINO`
--

LOCK TABLES `TREINO` WRITE;
/*!40000 ALTER TABLE `TREINO` DISABLE KEYS */;
INSERT INTO `TREINO` VALUES (1,1,1,'2022-11-20 09:30:00'),(2,2,2,'2022-11-25 19:30:00'),(3,3,3,'2022-11-27 21:30:00'),(4,4,4,'2022-12-02 09:33:40'),(5,4,4,'2022-12-02 09:40:30'),(6,4,4,'2022-12-02 10:40:10'),(7,4,6,'2022-12-02 10:40:43');
/*!40000 ALTER TABLE `TREINO` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USERNAME`
--

DROP TABLE IF EXISTS `USERNAME`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `USERNAME` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `CPF` int NOT NULL,
  `NOME` varchar(100) NOT NULL,
  `EMAIL` varchar(100) NOT NULL,
  `SENHA` varchar(100) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USERNAME`
--

LOCK TABLES `USERNAME` WRITE;
/*!40000 ALTER TABLE `USERNAME` DISABLE KEYS */;
INSERT INTO `USERNAME` VALUES (1,12345678,'RYU','AAAA@A.com','2013a0402'),(2,25423544,'LUCA','BBBB@A.com','2014B0402'),(3,33333312,'BENICIO','CCCC@A.com','2015C0402'),(4,10,'NEYMAR','neymarjr@gmail.com','hexa'),(5,9999,'Ronaldo','r9@gmail.com','penta'),(6,11,'Romario','r11@gmail.com','tetra');
/*!40000 ALTER TABLE `USERNAME` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-05 10:10:45
