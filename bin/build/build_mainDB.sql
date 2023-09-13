USE PAM;
DROP TABLE IF EXISTS main_db;
CREATE TABLE main_db(
	passID INT NOT NULL KEY AUTO_INCREMENT,
	name varchar(500),
	url varchar(500),
	username varchar(250),
	password varchar(250),
    note varchar(150)
);

SELECT * FROM main_db;
DESCRIBE main_db;
