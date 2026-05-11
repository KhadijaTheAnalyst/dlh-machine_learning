-- Works with MySQL 8.0.13+
-- Create a composite index on the first letter of the name column and the score column
-- This optimizes searches by first letter and score

CREATE INDEX idx_name_first_score ON names((LEFT(name, 1)), score);