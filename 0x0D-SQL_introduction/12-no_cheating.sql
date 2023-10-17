-- script that updates the score of Bob to 10 in the table second_table.
-- not allowed to use Bob’s id value, only the name field.
-- database name will be passed as an argument of the mysql command

UPDATE second_table
SET name = 'Bob'
WHERE id = 10;

