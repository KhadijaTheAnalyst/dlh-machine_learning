-- This query calculates the total rating for each TV genre by summing up the ratings from the tv_show_ratings table.
-- It uses a LEFT JOIN to include all TV genres, even those that have no ratings, and COALESCE to return 0 for genres without ratings.
-- The results are grouped by TV genre ID and ordered by rating in descending order.

SELECT tv_genres.name, COALESCE(SUM(tv_show_ratings.rate), 0) AS rating
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_show_ratings
ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.id
ORDER BY rating DESC;
