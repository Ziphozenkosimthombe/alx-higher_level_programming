-- script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0
-- database name will be passed as an argument of the mysql command

SELECT COUNT(*) AS total FROM `first_table`
WHERE id = 89;
