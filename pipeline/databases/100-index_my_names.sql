-- Create an index on the first letter of the name column
-- This optimizes searches by first letter
-- Works with MySQL 8.0.13+

CREATE INDEX idx_name_first ON names((LEFT(name, 1)));

How it works:

-- CREATE INDEX idx_name_first - Creates index named idx_name_first
-- ON names - On the names table
-- ((LEFT(name, 1))) - On the first character of name column
-- LEFT(name, 1) - Gets the first letter