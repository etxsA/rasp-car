-- Definition of the squema and some other starting things. 
CREATE TABLE IF NOT EXISTS photoresistor (
  analog_voltage INT,
  voltage DOUBLE,
  timestamp TIME
);

CREATE TABLE IF NOT EXISTS accelerometer (
  x_axis DOUBLE,
  y_axis DOUBLE,
  z_axis DOUBLE,
  free_fall BOOLEAN,
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