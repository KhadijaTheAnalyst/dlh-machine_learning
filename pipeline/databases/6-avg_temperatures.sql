-- Calculate the average temperature for each city and order the results by average temperature in descending order.
SELECT avg(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
