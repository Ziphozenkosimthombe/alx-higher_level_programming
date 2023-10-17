--  script that lists all records of the table second_table of the database hbtn_0c_0 
-- Results should display both the score and the name 
-- Records should be ordered by score
-- database name will be passed as an argument of the mysql command

SELECT score, name
FROM second_table
GROUP BY score
DESC;
