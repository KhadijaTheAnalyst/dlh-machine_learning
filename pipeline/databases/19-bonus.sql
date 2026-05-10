-- Create a stored procedure named `AddBonus` that takes three parameters:
-- `p_user_id` (INT), `p_project_name` (VARCHAR(255)), and `p_score` (INT).
-- The procedure should perform the following steps:
-- 1. Check if a project with the name `p_project_name` exists in the `projects` table.
-- 2. If the project does not exist, insert a new project with the name `p_project_name` and retrieve its ID.
-- 3. Insert a new record into the `corrections` table with the `user_id`, `project_id`, and `score` provided as parameters.
-- Assume that the `projects` table has columns `id` (INT, AUTO_INCREMENT) and `name` (VARCHAR(255)).
-- Assume that the `corrections` table has columns `user_id` (INT), `project_id` (INT), and `score` (INT).
-- Use appropriate error handling to ensure that the procedure executes smoothly.
-- Note: The procedure should be created in a way that it can be called multiple times without causing issues, such as duplicate entries in the `projects` table.
-- Example of calling the procedure:
-- CALL AddBonus(1, 'Project Alpha', 10);
-- p_ is procedure parameter prefix, v_ is variable prefix, and s_ is select result prefix.

DELIMITER $$

CREATE PROCEDURE AddBonus (
    IN p_user_id INT,
    IN p_project_name VARCHAR(255),
    IN p_score INT
)
BEGIN
    DECLARE v_project_id INT;

    SELECT id INTO v_project_id
    FROM projects
    WHERE name = p_project_name
    LIMIT 1;

    IF v_project_id IS NULL THEN
        INSERT INTO projects (name)
        VALUES (p_project_name);

        SET v_project_id = LAST_INSERT_ID();
    END IF;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (p_user_id, v_project_id, p_score);

END$$

DELIMITER ;
