-- script that computes the score average of all records in the table second_table of the database hbtn_0c_0
-- The result column name should be average.
-- database name will be passed as an argument of the mysql command

SELECT score
COUNT(score) AS average
FROM second_table
GROUP BY score;
