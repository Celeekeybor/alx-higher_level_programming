-- Prints records with a non-empty name column in a table in the database
SELECT score, name FROM second_table
    WHERE name IS NOT NULL
    ORDER BY score DESC;
