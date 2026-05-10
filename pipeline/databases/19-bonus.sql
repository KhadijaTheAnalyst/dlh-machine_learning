-- Add a bonus to a user for completing a project correction. 
--If the project doesn't exist, create it first.

DELIMITER $$
CREATE PROCEDURE AddBonus (user_id INT, project_name VARCHAR(255), score INT)
BEGIN
    -- Step 1: Declare variable to store project_id
    DECLARE project_id INT;
    
    -- Step 2: Try to find the project
    SELECT id INTO project_id FROM projects WHERE name = project_name;
    
    -- Step 3: If project doesn't exist, create it
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SELECT LAST_INSERT_ID() INTO project_id;
    END IF;
    
    -- Step 4: Insert the correction
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END$$
DELIMITER ;


-- SELECT id                        -- Get the ID column
-- INTO project_id                  -- Store it in variable project_id
-- FROM projects                    -- From the projects table
-- WHERE name = project_name;       -- Where name matches the input parameter