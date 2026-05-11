-- Create an index on the first letter of the name column
-- This optimizes searches by first letter
-- Works with MySQL 8.0.13+

CREATE INDEX idx_name_first ON names((LEFT(name, 1)));
