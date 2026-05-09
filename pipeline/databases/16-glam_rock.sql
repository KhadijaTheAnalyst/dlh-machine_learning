-- List the lifespan of each glam rock band, ordered by lifespan in descending order.
-- Assume that if a band is still active, it has split in 2020.

SELECT
    band_name,
    (IFNULL(split, 2020) - formed) AS "lifespan"
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;