-- Create an index idx_name_first on the table names
-- and the first letter of name.
DROP INDEX IF EXISTS idx_name_first ON names;
CREATE INDEX idx_name_first ON names (SUBSTRING(name, 1, 1));
