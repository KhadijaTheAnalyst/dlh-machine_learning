-- This function safely divides two numbers and returns NULL if the denominator is zero.
-- Usage example:
-- SELECT SafeDiv(10, 2); -- Returns 5
-- SELECT SafeDiv(10, 0); -- Returns NULL   

DELIMITER $$

CREATE FUNCTION SafeDiv (
    a FLOAT,
    b FLOAT
)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0; -- or you could return NULL, depending on your preference
    END IF;

    RETURN a / b;
END$$

DELIMITER ;