from . import ADS1115
from . import ADXL345 
from . import BMP280
from . import Ultrasonic
from typing import Dict

class SensorController:
    """
    SensorController class to manage multiple sensors including ADS1115 (light sensor),
    ADXL345 (accelerometer), BMP280 (temperature, pressure, altitude), and Ultrasonic (distance).
    Provides methods to initialize, read, and manage data from each sensor.
    """
    def __init__(self):
        """Initializes each sensor with its default or specified configuration."""
        # Initialize sensors
        self.lightSensor = ADS1115()
        self.accelerometer = ADXL345()
        self.environmentSensor = BMP280()
        self.distanceSensor = Ultrasonic()
        print("Sensor Controller initialized with ADS1115, ADXL345, BMP280, and Ultrasonic sensors.")

    def readLightSensor(self) -> Dict[str, float]:
        """
        Reads data from the ADS1115 light sensor.

        Returns:
            dict: Dictionary with voltage and light level percentage.
        """
        return self.lightSensor.readData()

    def readAccelerometer(self) -> Dict[str, float]:
        """
        Reads data from the ADXL345 accelerometer, including x, y, z axis acceleration
        and detected events.

        Returns:
            dict: Dictionary containing x, y, z axis acceleration in g and any events.
        """
        return self.accelerometer.readData()

    def readEnvironmentSensor(self) -> Dict[str, float]:
        """
        Reads data from the BMP280 sensor, including temperature, pressure, and altitude.

        Returns:
            dict: Dictionary containing temperature (°C), pressure (hPa), and altitude (m).
        """
        return self.environmentSensor.readData()

    def readDistanceSensor(self) -> Dict[str, float]:
        """
        Reads data from the Ultrasonic distance sensor.

        Returns:
            dict: Dictionary containing distance in centimeters.
        """
        return self.distanceSensor.measureDistance()

    def readAllSensors(self) -> Dict[str, Dict[str, float]]:
        """
        Reads data from all sensors and combines it into a single dictionary.

        Returns:
            dict: Dictionary with readings from all sensors.
        """
        return {
            "lightSensor": self.readLightSensor(),
            "accelerometer": self.readAccelerometer(),
            "environmentSensor": self.readEnvironmentSensor(),
            "distanceSensor": self.readDistanceSensor()
        }

    def __del__(self):
        """Destructor to ensure cleanup of resources for each sensor."""
        del self.lightSensor
        del self.accelerometer
        del self.environmentSensor
        del self.distanceSensor
