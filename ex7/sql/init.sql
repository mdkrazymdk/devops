CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL
);

INSERT INTO notes (content) VALUES ('Success! Database works.');
INSERT INTO notes (content) VALUES ('Docker vs Local Postgres resolved.');
