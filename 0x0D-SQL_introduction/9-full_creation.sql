--  script that creates a table second_table in the database hbtn_0c_0
-- add multiples rows.
-- second_table description:
-- id INT
-- name VARCHAR(256)
-- score INT
-- database name will be passed as an argument to the mysql command
-- If the table second_table already exists, your script should not fail
--  not allowed to use the SELECT and SHOW statements

CREATE TABLE IF NOT EXISTS second_table
(
	id INT,
	name VARCHAR(256),
	score INT,
	PIMARY KEY(id));

INSERT INTO second_table(name, score)
VALUES('John', 10),
('Alex', 3),
('Bob', 14),
('George', 8);
