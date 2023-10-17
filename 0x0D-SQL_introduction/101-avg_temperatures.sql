--  script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

SELECT city, AVG(avg_temp)
FROM temperature
GROUP BY city
ORDER avg_temp
DESC;
