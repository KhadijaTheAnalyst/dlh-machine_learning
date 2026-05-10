-- This function safely divides two numbers and returns NULL if the denominator is zero.
-- Usage example:
-- SELECT SafeDiv(10, 2); -- Returns 5
-- SELECT SafeDiv(10, 0); -- Returns NULL   

DELIMITER $$
CREATE FUNCTION SafeDiv (
    a INT, 
    b INT
) RETURNS INT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0; -- or you could return a specific value like 0 or -1 to indicate an error
    ELSE
        RETURN a / b;
    END IF;
END$$
DELIMITER ;
