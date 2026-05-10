-- This procedure computes the average score for a user based on their corrections and
-- updates the users table with the computed average score.
-- The procedure takes a user_id as input, calculates the average score from the corrections
-- table, and updates the average_score column in the users table for that user.
-- Example of calling the procedure:
-- CALL ComputeAverageScoreForUser(1);

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
BEGIN
    DECLARE avg_score FLOAT;

    SELECT AVG(score) INTO avg_score
    FROM corrections c
    WHERE c.user_id = user_id;

    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END$$
DELIMITER ;
