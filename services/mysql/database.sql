CREATE TABLE IF NOT EXISTS photoresistor (
  id INT AUTO_INCREMENT PRIMARY KEY,
  voltage DOUBLE NOT NULL,
  lightLevel DOUBLE NOT NULL,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS accelerometer (
  id INT AUTO_INCREMENT PRIMARY KEY,
  x DOUBLE NOT NULL,
  y DOUBLE NOT NULL,
  z DOUBLE NOT NULL,
  events VARCHAR(20) NOT NULL,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS distance (
  id INT AUTO_INCREMENT PRIMARY KEY,
  distance DOUBLE NOT NULL,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS pressure (
  id INT AUTO_INCREMENT PRIMARY KEY,
  temperature DOUBLE NOT NULL,
  pressure DOUBLE NOT NULL,
  altitude DOUBLE NOT NULL,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
