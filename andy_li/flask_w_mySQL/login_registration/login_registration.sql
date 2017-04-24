-- MySQL Workbench Synchronization
-- Generated: 2017-04-13 18:38
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: iandyli

-- SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
-- SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
-- SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';
-- 
-- CREATE SCHEMA IF NOT EXISTS `login_registration` DEFAULT CHARACTER SET utf8 ;
-- 
-- CREATE TABLE IF NOT EXISTS `login_registration`.`users` (
--   `id` INT(11) NOT NULL AUTO_INCREMENT,
--   `first_name` VARCHAR(255) NOT NULL,
--   `last_name` VARCHAR(255) NOT NULL,
--   `email` VARCHAR(255) NOT NULL,
--   `password` VARCHAR(255) NOT NULL,
--   `salt` VARCHAR(255) NOT NULL,
--   PRIMARY KEY (`id`))
-- ENGINE = InnoDB
-- DEFAULT CHARACTER SET = utf8;
-- 
-- 
-- SET SQL_MODE=@OLD_SQL_MODE;
-- SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
-- SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

select * from users;