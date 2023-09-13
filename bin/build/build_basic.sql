USE PAM;
DROP TABLE IF EXISTS basic_passes;
CREATE TABLE basic_passes(
	passID INT NOT NULL UNIQUE KEY AUTO_INCREMENT,
	login varchar(50) UNIQUE,
	email varchar(150),
	username varchar(50),
	password varchar(80)
);

SELECT * FROM basic_passes;
DESCRIBE basic_passes;

