-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: khatabill
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `admin_id` int NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'admin','1234');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bill_items`
--

DROP TABLE IF EXISTS `bill_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill_items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `bill_id` int NOT NULL,
  `product_id` int NOT NULL,
  `product_name` varchar(255) DEFAULT NULL,
  `quantity` int DEFAULT '1',
  `price` decimal(10,2) NOT NULL,
  `unit` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `bill_id` (`bill_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `bill_items_ibfk_1` FOREIGN KEY (`bill_id`) REFERENCES `bills` (`id`) ON DELETE CASCADE,
  CONSTRAINT `bill_items_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=120 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill_items`
--

LOCK TABLES `bill_items` WRITE;
/*!40000 ALTER TABLE `bill_items` DISABLE KEYS */;
INSERT INTO `bill_items` VALUES (1,1,1,NULL,1,44.00,'kg'),(2,2,1,NULL,10,44.00,'kg'),(3,3,10,NULL,5,5.00,'packet'),(4,4,2,NULL,1,70.00,'kg'),(5,5,9,NULL,1,40.00,'packet'),(11,13,7,'Masur Dal',5,60.00,'kg'),(12,14,11,'Butter Milk',2,30.00,'packet'),(13,15,2,'Rice ',1,70.00,'kg'),(15,17,4,'Wheat',1,60.00,'kg'),(16,18,1,'Sugar',1,44.00,'kg'),(20,11,2,'Rice ',2,70.00,'kg'),(23,21,16,'Sugar (1/2)',1,22.00,'unit'),(25,23,10,'Chips (₹5)',5,5.00,'packet'),(28,25,6,'Moog Dal',5,80.00,'kg'),(29,26,1,'Sugar',2,48.00,'kg'),(30,27,12,'Parle - G',2,5.00,'packet'),(31,28,17,'Mari Gold',10,10.00,'packet'),(32,29,2,'Rice ',4,70.00,'kg'),(33,30,11,'Butter Milk',3,30.00,'packet'),(34,31,5,'Toor Dal',4,150.00,'kg'),(36,33,5,'Toor Dal',1,150.00,'kg'),(37,34,20,'Gooday Biscuit (₹5)',2,10.00,'packet'),(38,35,10,'Chips (₹5)',4,5.00,'packet'),(39,36,19,'Pohe (1 KG)',1,60.00,'kg'),(40,37,8,'Milk',2,70.00,'liter'),(41,38,8,'Milk',5,70.00,'liter'),(42,39,1,'Sugar',5,48.00,'kg'),(44,41,20,'Gooday Biscuit (₹10)',10,10.00,'packet'),(45,42,8,'Milk',4,70.00,'liter'),(46,43,10,'Chips (₹5)',5,10.00,'packet'),(47,44,8,'Milk',3,70.00,'liter'),(48,45,1,'Sugar',5,48.00,'kg'),(49,46,11,'Butter Milk',4,30.00,'packet'),(50,47,4,'Wheat',5,60.00,'kg'),(51,48,1,'Sugar',5,48.00,'kg'),(52,49,16,'Sugar (1/2)',1,22.00,'unit'),(53,50,1,'Sugar',1,48.00,'kg'),(54,50,19,'Pohe (1 KG)',1,60.00,'kg'),(55,50,8,'Milk',1,70.00,'liter'),(73,51,21,'Oil',1,170.00,'kg'),(74,51,1,'Sugar',1,48.00,'kg'),(75,51,2,'Basmati Rice ',1,70.00,'kg'),(76,51,4,'Wheat',1,60.00,'kg'),(77,51,5,'Toor Dal',1,150.00,'kg'),(78,51,6,'Moog Dal',1,140.00,'kg'),(79,51,7,'Masur Dal',1,60.00,'kg'),(80,51,8,'Milk',1,70.00,'liter'),(81,51,9,'Dahi',1,40.00,'packet'),(82,51,10,'Chips (₹5)',1,10.00,'packet'),(83,51,11,'Butter Milk',1,30.00,'packet'),(84,51,12,'Parle - G',1,5.00,'packet'),(85,51,16,'Sugar (1/2)',1,22.00,'unit'),(86,51,17,'Mari Gold',1,10.00,'packet'),(87,51,19,'Pohe (1 KG)',1,60.00,'kg'),(88,51,20,'Gooday Biscuit (₹10)',2,10.00,'packet'),(89,51,22,'Mari Light Biscuit',1,10.00,'packet'),(103,52,10,'Chips (₹5)',4,10.00,'packet'),(104,52,16,'Sugar (1/2)',1,22.00,'unit'),(105,52,17,'Mari Gold',4,10.00,'packet'),(106,52,20,'Gooday Biscuit (₹10)',2,10.00,'packet'),(107,53,9,'Dahi',1,40.00,'packet'),(108,54,9,'Dahi',5,40.00,'packet'),(109,55,27,'Trimax Pen',1,45.00,'pic'),(110,56,24,'Notebook (200 Pages)',2,80.00,'pic'),(111,57,30,'Sprite',2,20.00,'pic'),(113,58,44,'Amul Butter',4,30.00,'packet'),(114,58,10,'Chips (₹5)',5,10.00,'packet'),(115,59,9,'Dahi',1,40.00,'packet'),(116,60,8,'Milk',2,70.00,'liter'),(117,61,16,'Sugar (1/2)',1,22.00,'unit'),(118,61,10,'Chips (₹5)',4,10.00,'packet'),(119,61,11,'Butter Milk',2,30.00,'packet');
/*!40000 ALTER TABLE `bill_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bills`
--

DROP TABLE IF EXISTS `bills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bills` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int NOT NULL,
  `total_amount` decimal(10,2) DEFAULT '0.00',
  `status` enum('PAID','PENDING') DEFAULT 'PENDING',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `bills_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bills`
--

LOCK TABLES `bills` WRITE;
/*!40000 ALTER TABLE `bills` DISABLE KEYS */;
INSERT INTO `bills` VALUES (1,1,44.00,'PAID','2026-02-23 12:28:34'),(2,2,440.00,'PAID','2026-02-23 12:30:44'),(3,3,25.00,'PAID','2026-02-23 13:20:11'),(4,4,70.00,'PAID','2026-02-23 13:26:08'),(5,5,40.00,'PAID','2026-02-23 13:53:44'),(10,1,0.00,'PAID','2026-02-24 14:01:10'),(11,7,480.00,'PAID','2026-02-24 15:29:06'),(12,9,170.00,'PAID','2026-02-24 15:34:19'),(13,6,300.00,'PAID','2026-02-24 15:38:43'),(14,6,60.00,'PAID','2026-02-24 15:42:03'),(15,5,70.00,'PAID','2026-02-24 15:44:34'),(16,3,0.00,'PAID','2026-02-24 15:46:19'),(17,6,60.00,'PAID','2026-02-24 15:48:40'),(18,4,44.00,'PAID','2026-02-24 15:50:28'),(19,1,340.00,'PAID','2026-02-25 04:14:23'),(21,1,22.00,'PAID','2026-02-25 13:22:14'),(22,7,340.00,'PAID','2026-02-25 13:31:57'),(23,11,25.00,'PAID','2026-02-25 13:35:46'),(24,1,170.00,'PAID','2026-02-25 15:12:25'),(25,7,400.00,'PAID','2026-02-25 15:15:57'),(26,3,96.00,'PAID','2026-02-26 05:31:21'),(27,7,10.00,'PAID','2026-02-26 12:37:47'),(28,9,100.00,'PAID','2026-02-26 14:10:55'),(29,7,280.00,'PAID','2026-02-26 14:30:59'),(30,14,90.00,'PAID','2026-02-26 15:39:04'),(31,2,600.00,'PAID','2026-02-26 16:29:02'),(32,1,510.00,'PAID','2026-02-27 05:52:02'),(33,2,150.00,'PAID','2026-02-27 05:54:29'),(34,7,20.00,'PAID','2026-02-27 18:28:00'),(35,14,20.00,'PAID','2026-02-27 18:28:49'),(36,14,60.00,'PAID','2026-03-02 05:25:40'),(37,17,140.00,'PAID','2026-03-02 05:29:47'),(38,20,350.00,'PAID','2026-03-03 06:12:33'),(39,16,240.00,'PAID','2026-03-04 14:51:17'),(40,1,850.00,'PAID','2026-03-04 15:14:11'),(41,2,100.00,'PAID','2026-03-04 15:42:44'),(42,14,280.00,'PAID','2026-03-04 15:43:30'),(43,21,50.00,'PAID','2026-03-05 14:06:34'),(44,21,210.00,'PAID','2026-03-06 13:57:46'),(45,1,240.00,'PAID','2026-03-06 13:58:09'),(46,2,120.00,'PAID','2026-03-06 13:58:27'),(47,2,300.00,'PAID','2026-03-08 05:06:26'),(48,5,240.00,'PAID','2026-03-08 05:10:43'),(49,3,22.00,'PAID','2026-03-08 05:12:31'),(50,4,178.00,'PAID','2026-03-08 05:41:59'),(51,1,975.00,'PAID','2026-03-08 05:55:26'),(52,22,122.00,'PAID','2026-03-08 06:26:31'),(53,17,40.00,'PAID','2026-03-08 07:22:54'),(54,21,200.00,'PAID','2026-03-08 07:25:37'),(55,1,45.00,'PAID','2026-03-08 16:45:59'),(56,1,160.00,'PAID','2026-03-10 04:48:39'),(57,5,40.00,'PAID','2026-03-10 04:53:25'),(58,6,170.00,'PAID','2026-03-10 13:09:12'),(59,2,40.00,'PENDING','2026-03-10 13:22:10'),(60,1,140.00,'PENDING','2026-03-10 14:09:50'),(61,21,122.00,'PENDING','2026-03-10 14:10:26');
/*!40000 ALTER TABLE `bills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `opening_balance` decimal(10,2) DEFAULT '0.00',
  `password` varchar(255) DEFAULT NULL,
  `is_active` tinyint DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'Swarnil Ligade','7821866264','swarnilligade72005@gmail.com','',0.00,NULL,1),(2,'Sushil Rawool','9146245439','sushilrawool@gmail.com','',0.00,NULL,1),(3,'Ajit Kupale','7821866265','ajitkupale@gmail.com','',0.00,NULL,1),(4,'Sonali Lahvate','9325129717','sonali@gmail.com','',0.00,NULL,1),(5,'Shreyash  Mahajan','9850021236','shreyash@gmail.com','',0.00,NULL,1),(6,'Dipak Patil','9852264321','deepakpatil@gmail.com','',0.00,NULL,1),(7,'Nisha ','7385966265','nisha@gmail.com','',0.00,NULL,1),(9,'Sarthak','7854566921','sarthak@gmail.com','',0.00,NULL,1),(10,'Sharvari','7896322336','sharvari@gmail.com','',0.00,NULL,1),(11,'Neha','78956336624','neha@gmail.com','',0.00,NULL,1),(13,'Aditya','9852231250','aditya@gmail.com','',0.00,NULL,1),(14,'Sanchi','8408095744','Sanchi@gmail.com','',0.00,NULL,1),(15,'Om ','7896623354','om@gmail.com','',0.00,NULL,1),(16,'Ruturaj','8408095766','Ruturaj@gmail.com','',0.00,NULL,1),(17,'Manaswi','8428605988','Manaswi@gmail.com','',100.00,NULL,1),(18,'Santosh','8956623133','santosh@gmail.com','',0.00,NULL,1),(19,'Sagar','8748596233','sagar@gmail.com','',0.00,NULL,1),(20,'Kedar','7889995662','kedar@gmail.com','',0.00,NULL,1),(21,'Samruddhi','7895566231','samruddhi@gmail.com','',0.00,NULL,1),(22,'Disha','7854566965','disha@gamil.com','kolhapur\r\n',0.00,NULL,1);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `bill_id` int DEFAULT NULL,
  `customer_id` int DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `payment_mode` varchar(50) DEFAULT NULL,
  `payment_status` varchar(20) DEFAULT NULL,
  `payment_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `bill_id` (`bill_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`bill_id`) REFERENCES `bills` (`id`),
  CONSTRAINT `payments_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `pending_bills`
--

DROP TABLE IF EXISTS `pending_bills`;
/*!50001 DROP VIEW IF EXISTS `pending_bills`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `pending_bills` AS SELECT 
 1 AS `customer_id`,
 1 AS `customer_name`,
 1 AS `bill_id`,
 1 AS `pending_amount`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `quantity` int DEFAULT '0',
  `unit` varchar(50) NOT NULL DEFAULT 'unit',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Sugar',48.00,1,'kg'),(2,'Basmati Rice ',70.00,1,'kg'),(4,'Wheat',60.00,1,'kg'),(5,'Toor Dal',150.00,1,'kg'),(6,'Moog Dal',140.00,1,'kg'),(7,'Masur Dal',60.00,1,'kg'),(8,'Milk',70.00,1,'liter'),(9,'Dahi',40.00,1,'packet'),(10,'Chips (₹5)',10.00,1,'packet'),(11,'Butter Milk',30.00,1,'packet'),(12,'Parle - G',5.00,1,'packet'),(13,'Parle - G',10.00,1,'packet'),(15,'Parle - G',20.00,1,'packet'),(16,'Sugar (1/2)',22.00,500,'unit'),(17,'Mari Gold',10.00,1,'packet'),(18,'Sugar',24.00,250,'gram'),(19,'Pohe (1 KG)',60.00,1,'kg'),(20,'Gooday Biscuit (₹10)',10.00,1,'packet'),(21,'Oil',180.00,1,'kg'),(22,'Mari Light Biscuit',10.00,1,'packet'),(23,'Notebook (100 Pages)',40.00,1,'pic'),(24,'Notebook (200 Pages)',80.00,1,'pic'),(25,'Pen',10.00,1,'pic'),(26,'Apsara Pencil',8.00,1,'pic'),(27,'Trimax Pen',45.00,1,'pic'),(28,'Eraser',1.00,6,'pic'),(29,'Sharpner',6.00,1,'pic'),(30,'Sprite',20.00,1,'pic'),(31,'Mango Cold Drink',20.00,1,'pic'),(32,'Thumbs Up',20.00,1,'pic'),(33,'Sting',20.00,1,'pic'),(34,'Jeera Soda',20.00,1,'pic'),(35,'Khari',12.00,1,'packet'),(36,'Khari (RS-20)',20.00,1,'packet'),(37,'Butter ',20.00,1,'packet'),(38,'Bread',20.00,1,'packet'),(39,'Toast',20.00,1,'packet'),(40,'Cream Roll',10.00,1,'pic'),(41,'Coconut',20.00,1,'packet'),(42,'Bun Maska Pav',15.00,1,'packet'),(43,'Peach Butter',20.00,1,'packet'),(44,'Amul Butter',30.00,1,'packet'),(45,'Rin Bar',10.00,1,'pic'),(46,'Vim Bar',10.00,1,'pic'),(47,'Surf Excel Bar',10.00,1,'pic'),(48,'Surf Excel Powder',10.00,1,'pic'),(49,'Wheel Bar',10.00,1,'pic'),(50,'Wheel Powder',10.00,1,'pic');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `sales_report`
--

DROP TABLE IF EXISTS `sales_report`;
/*!50001 DROP VIEW IF EXISTS `sales_report`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `sales_report` AS SELECT 
 1 AS `bill_date`,
 1 AS `total_sales`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','1234');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `pending_bills`
--

/*!50001 DROP VIEW IF EXISTS `pending_bills`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `pending_bills` AS select `c`.`id` AS `customer_id`,`c`.`name` AS `customer_name`,`b`.`id` AS `bill_id`,(`b`.`total_amount` - ifnull(sum(`p`.`amount`),0)) AS `pending_amount` from ((`customers` `c` join `bills` `b` on((`c`.`id` = `b`.`customer_id`))) left join `payments` `p` on((`b`.`id` = `p`.`bill_id`))) where (`b`.`status` = 'PENDING') group by `c`.`id`,`c`.`name`,`b`.`id`,`b`.`total_amount` having (`pending_amount` > 0) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `sales_report`
--

/*!50001 DROP VIEW IF EXISTS `sales_report`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `sales_report` AS select cast(`b`.`created_at` as date) AS `bill_date`,sum(`b`.`total_amount`) AS `total_sales` from `bills` `b` group by cast(`b`.`created_at` as date) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-10 20:54:36
