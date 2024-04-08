-- File name: C:\Users
atha\OneDrive\Desktop\CS\NEA\studycsmysql.sql
-- Created by 簐奘 


--
-- Table structure for table `topics`
--

CREATE TABLE `topics` (
  `topicID` TEXT NOT NULL,
  `topicname` TEXT NULL,
  PRIMARY KEY (`topicID` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `questionID` TEXT NOT NULL,
  `topicID` TEXT NULL,
  `question` TEXT NULL,
  `ans1` TEXT NULL,
  `ans2` TEXT NULL,
  `ans3` TEXT NULL,
  `ans4` TEXT NULL,
  `correct` TEXT NULL,
  `difficulty` DOUBLE NULL DEFAULT 0,
  `success` INT NULL DEFAULT 0,
  `attempts` INT NULL DEFAULT 0,
  PRIMARY KEY (`questionID` ASC),
  CONSTRAINT `topicID_topics_topicID` FOREIGN KEY (`topicID`) REFERENCES `topics` (`topicID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `ID` TEXT NOT NULL,
  `USERNAME` TEXT NOT NULL,
  `PASSWORD` TEXT NOT NULL,
  `NAME` TEXT NOT NULL,
  `SURNAME` TEXT NOT NULL,
  `JOINDATE` TEXT NOT NULL,
  PRIMARY KEY (`ID` ASC)
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Table structure for table `questionsuccess`
--

CREATE TABLE `questionsuccess` (
  `ID` TEXT NOT NULL,
  `questionID` INT NOT NULL DEFAULT 0,
  `attempted` INT NULL DEFAULT 0,
  `success` INT NULL DEFAULT 0,
  `inclasttest` BOOL NULL DEFAULT 0,
  PRIMARY KEY (`ID` ASC,`questionID` ASC),
  CONSTRAINT `questionID_questions_questionID` FOREIGN KEY (`questionID`) REFERENCES `questions` (`questionID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ID_accounts_ID` FOREIGN KEY (`ID`) REFERENCES `accounts` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) DEFAULT CHARSET=utf8 ENGINE=InnoDB;

--
-- Dumping data for table `topics`
--

INSERT INTO `topics` (`topicID`,`topicname`) VALUES ('FOP','Fundamentals of Programming'),('FOA','Fundamentals of Algorithms'),('DS','Fundamentals of Data Structures'),('PS','Systematic Approach to Problem Solving'),('TC','Theory of Computation'),('DR','Fundamentals of Data Representation'),('CS','Fundamentals of Computer Systems'),('COA','Fundamentals of Computer Organisation and Architecture'),('COC','Consequences of uses of Computing'),('CON','Fundamentals of Communication and Networking');

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`questionID`,`topicID`,`question`,`ans1`,`ans2`,`ans3`,`ans4`,`correct`,`difficulty`,`success`,`attempts`) VALUES ('1','DR','what is binary 0001 in denary ','1','0','10','1000','1',0.666667,6,9),('2','DR','an image is captured at 200 x 400 pixels with a color depth of 4 bits. how big will the file be in MB','1280000','320000','0.4','0.16','3',1.000000,9,9),('3','FOP','which answer correctly denotes a for loop that will run four times','for i in range(4):','for i in range(four):','for i in range(3):','for in range(4):','1',1.000000,6,6),('4','FOA','which type of variable can be accessed from anywhere in the program','array','local','global','constant','3',0.833333,5,6);

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`ID`,`USERNAME`,`PASSWORD`,`NAME`,`SURNAME`,`JOINDATE`) VALUES ('NatRit020634','NRitchie03','123456','Nathan','Ritchie','2022-06-02 22:55:34'),('JohJoh070234','jjohn04','1234','john','johnson','2022-02-07 22:55:34'),('admin','123','123','123','123','06-02-2020'),('MicLin011019','mlinger0','6BwpToQYV','Michaelina','Linger','2021-10-01 03:02:19'),('ShaBil130804','sbillett1','3ujEEFqT','Shamus','Billett','2021-08-13 01:41:04'),('IdaVau020338','ivaud2','XoW0bXy','Idalia','Vaud','2022-03-02 09:40:38'),('ChrDen151049','cdenny3','fsZz0Oecxdj1','Chrissie','Denny','2021-10-15 01:57:49'),('BenPla020111','bplanke4','55d2pAm2A9h','Benny','Planke','2022-01-02 00:43:11'),('CinBed030225','cbedome5','nxHteK5','Cinderella','Bedome','2022-02-03 11:46:25'),('GerPol290129','gpoltun6','5Aq1jmCL9Xu','Gerti','Poltun','2022-01-29 14:44:29'),('SidYea200355','syearns7','jm0fG0YTmr','Sid','Yearns','2022-03-20 02:51:55'),('FarPra060956','fprandin8','4DsVtDFWe','Farah','Prandin','2021-09-06 08:41:56'),('AudDar150806','adarracott9','4wlwHFcxRyNy','Audy','Darracott','2021-08-15 00:04:06'),('QwQ300342','q','q','Qw','Q','2022-03-30 20:52:42'),('AswAwd300303','awd','awd','Aswe','Awd','2022-03-30 20:58:03');

--
-- Dumping data for table `questionsuccess`
--

INSERT INTO `questionsuccess` (`ID`,`questionID`,`attempted`,`success`,`inclasttest`) VALUES ('admin',1,8,6,0),('AudDar150806',1,0,0,0),('AudDar150806',2,0,0,0),('AudDar150806',3,0,0,0),('AudDar150806',4,0,0,0),('BenPla020111',1,0,0,0),('BenPla020111',2,0,0,0),('BenPla020111',3,0,0,0),('BenPla020111',4,0,0,0),('ChrDen151049',1,0,0,0),('ChrDen151049',2,0,0,0),('ChrDen151049',3,0,0,0),('ChrDen151049',4,0,0,0),('CinBed030225',1,0,0,0),('CinBed030225',2,0,0,0),('CinBed030225',3,0,0,0),('CinBed030225',4,0,0,0),('FarPra060956',1,0,0,0),('FarPra060956',2,0,0,0),('FarPra060956',3,0,0,0),('FarPra060956',4,0,0,0),('GerPol290129',1,0,0,0),('GerPol290129',2,0,0,0),('GerPol290129',3,0,0,0),('GerPol290129',4,0,0,0),('IdaVau020338',1,0,0,0),('IdaVau020338',2,0,0,0),('IdaVau020338',3,0,0,0),('IdaVau020338',4,0,0,0),('JohJoh070234',1,0,0,0),('JohJoh070234',2,0,0,0),('JohJoh070234',3,0,0,0),('JohJoh070234',4,0,0,0),('MicLin011019',1,0,0,0),('MicLin011019',2,0,0,0),('MicLin011019',3,0,0,0),('MicLin011019',4,0,0,0),('NatRit020634',1,1,0,0),('NatRit020634',2,1,1,0),('NatRit020634',3,1,1,0),('NatRit020634',4,1,1,0),('ShaBil130804',1,0,0,0),('ShaBil130804',2,0,0,0),('ShaBil130804',3,0,0,0),('ShaBil130804',4,0,0,0),('SidYea200355',1,0,0,0),('SidYea200355',2,0,0,0),('SidYea200355',3,0,0,0),('SidYea200355',4,0,0,0),('admin',2,8,8,0),('admin',3,5,5,0),('admin',4,5,4,0);
