-- Compute and store weighted average score for a user
-- Weighted average = SUM(score * weight) / SUM(weight)


DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
    DECLARE weighted_avg FLOAT;
    
    -- Calculate weighted average score
    -- Join corrections with projects to get weights
    -- Score * Weight for each correction, sum them, divide by total weight

    SELECT SUM(c.score * p.weight) / SUM(p.weight) INTO weighted_avg
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Update the user's weighted average score
   UPDATE users
   SET average_score = weighted_avg
   WHERE id = user_id;
END$$
DELIMITER ;
