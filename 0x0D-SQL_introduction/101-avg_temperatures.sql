--  script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

SELECT city, AVG(value)
FROM temperatures
GROUP BY city
ORDER avg_temp
DESC;
