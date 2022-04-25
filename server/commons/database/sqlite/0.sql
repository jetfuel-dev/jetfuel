CREATE TABLE IF NOT EXISTS schema_version (
    version             INTEGER NOT NULL,
    date                INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    user_id             TEXT PRIMARY KEY,
    email               TEXT UNIQUE,
    api_token           TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS events (
    user_id             TEXT,
    timestamp           REAL NOT NULL,
    name                TEXT NOT NULL,
    period_min          REAL NOT NULL,
    period_max          REAL NOT NULL,
    period_mean         REAL NOT NULL,
    period_count        INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);

CREATE INDEX IF NOT EXISTS event_names ON events(name);

CREATE INDEX IF NOT EXISTS event_timesamps ON events(timestamp);
