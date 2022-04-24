CREATE TABLE IF NOT EXISTS schema_version (
    version             integer NOT NULL,
    date                bigint NOT NULL
);

CREATE TABLE IF NOT EXISTS events (
    timestamp           double precision NOT NULL,
    name                varchar NOT NULL,
    seconds             double precision NOT NULL
);

CREATE INDEX IF NOT EXISTS event_names ON events(name);
