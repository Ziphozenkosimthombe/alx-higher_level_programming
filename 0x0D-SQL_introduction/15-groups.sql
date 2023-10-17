-- script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0
-- The result should display:
-- the score
-- the number of records for this score with the label number
--  list should be sorted by the number of records(descending)
-- database name will be passed as an argument to the mysql command

SELECT score,
COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number
DESC;