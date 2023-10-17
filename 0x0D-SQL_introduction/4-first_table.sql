--  script that creates a table called first_table in the current database in MySQL server.
-- first_table description:
-- id INT
-- name VARCHAR(256)
-- database name will be passed as an argument of the mysql command
-- If the table first_table already exists, your script should not fail
-- not allowed to use the SELECT or SHOW statements

CREATE TABLE IF EXISTS first_table
(
	id INT,
	name VARCHAR(256)
);
