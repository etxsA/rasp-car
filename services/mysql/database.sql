-- Definition of the squema and some other starting things. 
CREATE TABLE IF NOT EXISTS photoresistor (
  voltage DOUBLE,
  lightLevel DOUBLE,
  timestamp TIME
);

CREATE TABLE IF NOT EXISTS accelerometer (
  x DOUBLE,
  y DOUBLE,
  z DOUBLE,
  events VARCHAR(20),
  timestamp TIME
);

CREATE TABLE IF NOT EXISTS distance (
  distance DOUBLE, 
  timestamp TIME
);

CREATE TABLE IF NOT EXISTS pressure (
  temperature DOUBLE,
  pressure DOUBLE,
  altitude DOUBLE,
  timestamp TIME
);