-- MySQL dump 10.13  Distrib 5.5.37, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: ipu
-- ------------------------------------------------------
-- Server version	5.5.37-0ubuntu0.12.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `add`
--

DROP TABLE IF EXISTS `add`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `add` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `name` varchar(255) NOT NULL,
  `sername` varchar(255) NOT NULL,
  `login` varchar(255) NOT NULL,
  `password` int(11) NOT NULL,
  `adress` varchar(255) NOT NULL,
  `firm` varchar(255) NOT NULL,
  `model` varchar(255) NOT NULL,
  `met_id` varchar(255) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `add`
--

LOCK TABLES `add` WRITE;
/*!40000 ALTER TABLE `add` DISABLE KEYS */;
INSERT INTO `add` VALUES (1,'ddddd','dfd','dfd','dfd',34343,'dfdf','df','dfd','fdfdfd',1,'2014-06-23'),(2,'dfsdfsdfs','sdfs','dfsdf','dsfds',45454,'dfsdfs','dfsd','fsdf','sdfdsfs',1,'2014-06-23'),(3,'fsdfsd','dsfs','fsdf','sdfs',334,'dfs','fsd','fsd','fsdfsd',1,'2014-06-23'),(4,'sdfsdfds','sdf','sdfdsf','sdfsd',3434,'3dfsd','fsdf','sdfsd','fsdf',1,'2014-06-23'),(5,'gdfgdfgd','dfd','sdfs','dfs',454,'dfd','gdfg','df','gdfgdf',1,'2014-06-23'),(6,'fsdfsdfs','dfd','dfd','fdfd',3443,'dfsdfs','dfsd','fsd','fsd',1,'2014-06-23'),(7,'sdfdsfsd','fd','fsdf','sdfsdf',4534,'sdfds','fsd','fds','fsdf',1,'2014-06-23'),(8,'gdfgdfgdf','asdf','adsf','sdfasd',454,'fdgvdg','df','gdf','gdfgdf',1,'2014-06-23'),(9,'fsdfsd','sdfds','fsdf','sdfsd',4534,'dfsdfsd','fsd','fsd','fsd',1,'2014-06-23'),(10,'dfgdfgdfgdfgdf','sdfds','fsdfsd','fdsfsd',3453453,'dsfgdfg','df','gdfgdfg','dfgdfgdfg',1,'2014-06-23');
/*!40000 ALTER TABLE `add` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chat`
--

DROP TABLE IF EXISTS `chat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `answer` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `chat_user_id` (`user_id`),
  CONSTRAINT `chat_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat`
--

LOCK TABLES `chat` WRITE;
/*!40000 ALTER TABLE `chat` DISABLE KEYS */;
INSERT INTO `chat` VALUES (1,'cerf','oki',2,'2014-06-23'),(2,'lol','vcb',2,'2014-06-23'),(3,'lol','vce',2,'2014-06-23'),(4,'fsdfsdfds','cer',2,'2014-06-23'),(5,'Показания в программе  Показания на счетчике  Проблема: asdf','cerh',2,'2014-06-23'),(6,'сука блять сука','yu',2,'2014-06-23');
/*!40000 ALTER TABLE `chat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meter`
--

DROP TABLE IF EXISTS `meter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `adress` varchar(255) NOT NULL,
  `firm` varchar(255) NOT NULL,
  `model` varchar(255) NOT NULL,
  `met_id` varchar(255) NOT NULL,
  `record_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `meter_record_id` (`record_id`),
  KEY `meter_user_id` (`user_id`),
  CONSTRAINT `meter_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `meter_ibfk_2` FOREIGN KEY (`record_id`) REFERENCES `record` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meter`
--

LOCK TABLES `meter` WRITE;
/*!40000 ALTER TABLE `meter` DISABLE KEYS */;
INSERT INTO `meter` VALUES (2,9,'dfdf','df','dfd','fdfdfd',3),(3,10,'dfsdfs','dfsd','fsdf','sdfdsfs',4),(4,11,'dfs','fsd','fsd','fsdfsd',5),(5,12,'3dfsd','fsdf','sdfsd','fsdf',6),(6,13,'3dfsd','fsdf','sdfsd','fsdf',7),(7,14,'3dfsd','fsdf','sdfsd','fsdf',8),(8,15,'3dfsd','fsdf','sdfsd','fsdf',9),(9,16,'3dfsd','fsdf','sdfsd','fsdf',10),(10,17,'3dfsd','fsdf','sdfsd','fsdf',11),(11,18,'3dfsd','fsdf','sdfsd','fsdf',12),(12,19,'3dfsd','fsdf','sdfsd','fsdf',13),(13,2,'Мо','dfgв','ав','ав',5),(14,20,'dfd','gdfg','df','gdfgdf',14),(15,21,'dfsdfs','dfsd','fsd','fsd',15),(16,22,'fdgvdg','df','gdf','gdfgdf',16),(17,23,'sdfds','fsd','fds','fsdf',17),(18,24,'dsfgdfg','df','gdfgdfg','dfgdfgdfg',18),(19,25,'dfsdfsd','fsd','fsd','fsd',19);
/*!40000 ALTER TABLE `meter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `record`
--

DROP TABLE IF EXISTS `record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data` int(11) NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `record`
--

LOCK TABLES `record` WRITE;
/*!40000 ALTER TABLE `record` DISABLE KEYS */;
INSERT INTO `record` VALUES (1,12344,'2014-06-11 04:19:20'),(2,50729,'2014-06-23 15:16:40'),(3,65570,'2014-06-23 15:17:14'),(4,18008,'2014-06-23 15:43:07'),(5,53403,'2014-06-23 15:43:57'),(6,70491,'2014-06-23 15:45:29'),(7,74427,'2014-06-23 15:45:29'),(8,77954,'2014-06-23 15:45:29'),(9,86300,'2014-06-23 15:45:29'),(10,7449,'2014-06-23 15:45:29'),(11,77667,'2014-06-23 15:45:29'),(12,75599,'2014-06-23 15:45:29'),(13,47205,'2014-06-23 15:45:29'),(14,20687,'2014-06-23 17:12:13'),(15,40588,'2014-06-23 17:13:21'),(16,77754,'2014-06-23 17:17:10'),(17,95734,'2014-06-23 17:17:10'),(18,82950,'2014-06-23 17:20:28'),(19,33814,'2014-06-23 17:20:28');
/*!40000 ALTER TABLE `record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(255) NOT NULL,
  `password` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `sername` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'11',1,'Иван','Ивановушкин','disp'),(2,'22',2,'Андрей','Дибрович','user'),(4,'123',0,'Василий','Иванов','user'),(5,'sdfsd',4534,'dfs','fsdf','user'),(6,'sdfsd',4534,'dfs','fsdf','user'),(7,'dfd',34343,'dfd','dfd','user'),(8,'dfd',34343,'dfd','dfd','user'),(9,'dfd',34343,'dfd','dfd','user'),(10,'dsfds',45454,'sdfs','dfsdf','user'),(11,'sdfs',334,'dsfs','fsdf','user'),(12,'sdfsd',3434,'sdf','sdfdsf','user'),(13,'sdfsd',3434,'sdf','sdfdsf','user'),(14,'sdfsd',3434,'sdf','sdfdsf','user'),(15,'sdfsd',3434,'sdf','sdfdsf','user'),(16,'sdfsd',3434,'sdf','sdfdsf','user'),(17,'sdfsd',3434,'sdf','sdfdsf','user'),(18,'sdfsd',3434,'sdf','sdfdsf','user'),(19,'sdfsd',3434,'sdf','sdfdsf','user'),(20,'dfs',454,'dfd','sdfs','user'),(21,'fdfd',3443,'dfd','dfd','user'),(22,'sdfasd',454,'asdf','adsf','user'),(23,'sdfsdf',4534,'fd','fsdf','user'),(24,'fdsfsd',3453453,'sdfds','fsdfsd','user'),(25,'sdfsd',4534,'sdfds','fsdf','user');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-06-23 18:12:31
