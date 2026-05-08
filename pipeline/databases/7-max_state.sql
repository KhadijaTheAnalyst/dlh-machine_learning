-- Calculate the maximum temperature for each city and order the results by state in descending order.
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
