-- create-author-table
-- depends: 
CREATE TABLE author (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    description TEXT NOT NULL CHECK (char_length(description) <= 400),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL
);

