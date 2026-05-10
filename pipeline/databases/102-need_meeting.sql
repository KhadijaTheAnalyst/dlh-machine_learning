-- Create a view of students who need a meeting
-- Students with score < 80 and no recent meeting

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL 
     OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH));

--What is a VIEW?
-- View = Virtual Table

-- Not real data, just a query stored
-- Always shows current data
-- Can be queried like a table
-- Useful for complex filters