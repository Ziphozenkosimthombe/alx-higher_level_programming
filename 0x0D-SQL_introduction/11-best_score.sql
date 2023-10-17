-- script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0
-- Results should display both the score and the name
-- Records should be ordered by score
--  database name will be passed as an argument of the mysql command

SELECT score, name
FROM second_table
ORDER BY score
WHERE score >= 10
DESC;
