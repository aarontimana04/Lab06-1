CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    task VARCHAR(255) NOT NULL,
    priority VARCHAR(50) NOT NULL
);

INSERT INTO items (task, priority) VALUES
('doctor appointment', 'high'),
('buy dinner', 'low'),
('lomo saltado', 'high');
