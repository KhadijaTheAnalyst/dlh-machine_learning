-- List all shows with their genre IDs. If a show has multiple genres, it should be listed multiple times, once for each genre.
SELECT
tv_shows.title, tv_show_genres.genre_id
FROM
tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
