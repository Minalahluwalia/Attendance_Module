CREATE DATABASE IF NOT EXISTS `login` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `login`;

CREATE TABLE IF NOT EXISTS `accounts` (
	`id` int(11) NOT NULL AUTO_INCREMENT ,
  	`username` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`email` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB  auto_increment=2  DEFAULT CHARSET=utf8;
    
INSERT INTO `accounts` (`id`, `username`, `password`, `email`) VALUES (101, 'test', 'test', 'test@test.com');

    CREATE TABLE IF NOT EXISTS `signup` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`username` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`email` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB auto_increment=2 CHARSET=utf8;

INSERT INTO `signup` (`id`, `username`, `password`, `email`) VALUES (1, 'test', 'test', 'test@test.com');

select * from `signup`;
SELECT * FROM accounts WHERE username = 'ronaldo'  AND password = 'ronaldo'
