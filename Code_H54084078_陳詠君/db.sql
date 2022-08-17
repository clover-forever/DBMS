SET SQL_SAFE_UPDATES = 0;

CREATE DATABASE `singer_database`;
SHOW DATABASES;
USE `singer_database`;
DROP database `singer_database`;

DROP TABLE IF EXISTS `Ceremony`;

CREATE TABLE `Ceremony` (
  `ce_id` varchar(255) NOT NULL,
  `host_name` varchar(255) DEFAULT NULL,
  `ce_place` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ce_id`)
) ;

LOCK TABLES `Ceremony` WRITE;

UNLOCK TABLES;

DROP TABLE IF EXISTS `Singer`;

CREATE TABLE `Singer` (
  `SSN` varchar(255) NOT NULL,
  `s_name` varchar(255) DEFAULT NULL,
  `birthday` varchar(255) DEFAULT NULL, 				
  `zodiac_sign` varchar(255) DEFAULT NULL,
  `sex` varchar(1) DEFAULT NULL,
  `com_id` varchar(255) DEFAULT NULL,
  primary key(SSN)
) ;

alter table `Singer` 					-- ///////////////////
add FOREIGN KEY (`com_id`) 
REFERENCES `Company` (`com_id`)
on delete set null;

ALTER TABLE `singer`
MODIFY COLUMN `sex` varchar(255);

LOCK TABLES `Singer` WRITE;

UNLOCK TABLES;

DROP TABLE IF EXISTS `Album`;

CREATE TABLE `Album` (
	`a_id` varchar(255) NOT NULL,
	`a_date` varchar(255) DEFAULT NULL,
	`title` varchar(255) DEFAULT NULL,
	`SSN` varchar(255) default null,
	`ce_id` varchar(255) default null,
	PRIMARY KEY (`a_id`),
	FOREIGN KEY (`SSN`) REFERENCES `Singer` (`SSN`) on delete set null,
	FOREIGN KEY (`ce_id`) REFERENCES `Ceremony` (`ce_id`) on delete set null
);

LOCK TABLES `Album` WRITE;

UNLOCK TABLES;

DROP TABLE IF EXISTS `Concert`;

CREATE TABLE `Concert` (
  `con_id` varchar(255) NOT NULL,
  `place` varchar(255) DEFAULT NULL,
  `con_year` varchar(255) DEFAULT NULL,
  `con_name` varchar(255) DEFAULT NULL,
  `SSN` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`con_id`),
  FOREIGN KEY (`SSN`) REFERENCES `Singer` (`SSN`) on delete set null
);

LOCK TABLES `Concert` WRITE;

UNLOCK TABLES;

DROP TABLE IF EXISTS `Company`;

CREATE TABLE `Company` (
  `com_id` varchar(255) NOT NULL ,
  `com_name` varchar(255) DEFAULT NULL,
  `revenue` varchar(255) DEFAULT NULL,
  `SSN` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`com_id`),
  KEY `SSN` (`SSN`),
  FOREIGN KEY (`SSN`) REFERENCES `SInger` (`SSN`) on delete set null
) ;

ALTER TABLE `Company`
MODIFY COLUMN `revenue` int;

LOCK TABLES `Company` WRITE;

UNLOCK TABLES;


INSERT into `Ceremony` values ("1", "Anne", "高雄");
INSERT into `Ceremony` values ("2", "Bob", "高雄");
INSERT into `Ceremony` values ("3", "Anne", "台北");
INSERT into `Ceremony` values ("4", "Bob", "新竹");
INSERT into `Ceremony` values ("5", "Alie", "高雄");
INSERT into `Ceremony` values ("6", "Zoe", "花蓮");
INSERT into `Ceremony` values ("7", "Anne", "新北");
INSERT into `Ceremony` values ("8", "Lulu", "屏東");
INSERT into `Ceremony` values ("9", "Cathy", "桃園");
INSERT into `Ceremony` values ("10", "Kelly", "桃園");


insert into `company` values ("com1","公司1","1000",NULL);
insert into `company` values ("com2","公司2","10000",NULL);
insert into `company` values ("com3","公司3","2000",NULL);
insert into `company` values ("com4","公司4","50",NULL);
insert into `company` values ("com5","公司5","600",NULL);
insert into `company` values ("com6","公司6","800",NULL);
insert into `company` values ("com7","公司7","100",NULL);
insert into `company` values ("com8","公司8","1000",NULL);
insert into `company` values ("com9","公司9","20000",NULL);
insert into `company` values ("com10","公司10","30",NULL);

UPDATE `company`
SET `SSN` = "A1"
WHERE `com_id` = "com1";

UPDATE `company`
SET `SSN` = "A2"
WHERE `com_id` = "com2";
UPDATE `company`
SET `SSN` = "A3"
WHERE `com_id` = "com3";
UPDATE `company`
SET `SSN` = "A4"
WHERE `com_id` = "com4";
UPDATE `company`
SET `SSN` = "A5"
WHERE `com_id` = "com5";
UPDATE `company`
SET `SSN` = "A6"
WHERE `com_id` = "com6";
UPDATE `company`
SET `SSN` = "A9"
WHERE `com_id` = "com7";
UPDATE `company`
SET `SSN` = "A10"
WHERE `com_id` = "com8";
UPDATE `company`
SET `SSN` = "A11"
WHERE `com_id` = "com9";
UPDATE `company`
SET `SSN` = "A12"
WHERE `com_id` = "com10";

insert into `singer` value ("A1", "王力宏", "1999-08-08", "雙子座", "M", "com1");   
insert into `singer` value ("A2", "羅小祥", "2000-08-25", "獅子座", "M", "com2"); 
insert into `singer` value ("A3", "楊小林", "2001-06-18", "雙子座", "F", "com3"); 
insert into `singer` value ("A4", "周小倫", "1985-11-20", "天蠍座", "M", "com4"); 
insert into `singer` value ("A5", "蔡小林", "1983-03-01", "雙魚座", "F", "com5"); 
insert into `singer` value ("A6", "田小甄", "1983-03-30", "牡羊座", "F", "com6"); 
insert into `singer` value ("A7", "陳小樺", "1981-06-18", "雙子座", "F", "com6"); 
insert into `singer` value ("A8", "任小萱", "1981-10-31", "天蠍座", "F", "com6"); 
insert into `singer` value ("A9", "郭小靜", "1990-04-25", "金牛座", "F", "com7"); 
insert into `singer` value ("A10", "陳九零", "1997-10-05", "天平座", "M", "com8"); 
insert into `singer` value ("A11", "郭小城", "1950-01-25", "魔羯座", "M", "com9"); 
insert into `singer` value ("A12", "金小五", "1988-01-27", "水平座", "M", "com10"); 
insert into `singer` value ("A13", "任小齊", "1968-03-27", "牡羊座", "M", "com1");  

insert into `album` values ("album1", "1999", "專輯1", "A1", NULL); -- null: 沒得獎

insert into `album` values ("album2", "2000", "專輯2", "A1", NULL);
insert into `album` values ("album3", "1998", "專輯3", "A2", 1);
insert into `album` values ("album4", "1997", "專輯4", "A4", 3);
insert into `album` values ("album5", "1996", "專輯5", "A6", 5);
insert into `album` values ("album6", "2001", "專輯6", "A6", 7);
insert into `album` values ("album7", "2002", "專輯7", "A7", NULL);
insert into `album` values ("album8", "2003", "專輯8", "A8", NULL);
insert into `album` values ("album9", "2004", "專輯9", "A9", NULL);
insert into `album` values ("album10", "1995", "專輯10", "A10", 10);


insert into `concert` values ("con1", "高雄", "1999", "演唱會1", "A1");

insert into `concert` values ("con2", "新竹", "1998", "演唱會2", "A1");
insert into `concert` values ("con3", "台北", "1994", "演唱會3", "A5");
insert into `concert` values ("con4", "新北", "1989", "演唱會4", "A6");
insert into `concert` values ("con5", "南投", "1988", "演唱會5", "A7");
insert into `concert` values ("con6", "台南", "2000", "演唱會6", "A7");
insert into `concert` values ("con7", "台東", "2001", "演唱會7", "A7");
insert into `concert` values ("con8", "宜蘭", "1999", "演唱會8", "A10");
insert into `concert` values ("con9", "屏東", "1999", "演唱會9", "A12");
insert into `concert` values ("con10", "高雄", "1999", "演唱會10", "A12");


DELETE from `ceremony` where 1;
SELECT * from `company`;