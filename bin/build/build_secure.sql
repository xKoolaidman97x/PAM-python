USE PAM;
DROP TABLE IF EXISTS secure;
CREATE TABLE secure(
	passID INT UNIQUE KEY AUTO_INCREMENT,
	login varchar(50) UNIQUE,
	email varchar(150),
	username varchar(50),
	password varchar(80)
);

SELECT * FROM secure;
DESCRIBE secure;

