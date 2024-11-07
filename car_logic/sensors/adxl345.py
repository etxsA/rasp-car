# A simple implementation of adxl345 without external dependencies
# All memory locations and registers where obtained from the datasheet, also how to perfom the respective calculations is stated there
# https://www.analog.com/media/en/technical-documentation/data-sheets/adxl345.pdf

import smbus
from typing import Dict


class ADXL345:
    """
    ADXL345 accelerometer class to measure acceleration on the X, Y, and Z axes,
    and any event of the sensor using I2C communication.
    
    This class provides methods to initialize the ADXL345 sensor, configure its settings, 
    and read acceleration data from each axis.
    """


    def __init__(self, address=0x53) -> None: 
        """Initializes the ADXL345 sensor, sets it to measurement mode and changes the data format

        Args:
            address (hexadecimal, optional): i2c Address of the sensor. Defaults to 0x53.
        """
        self.address = address
        self.bus = smbus.SMBus(1)

        # Initialization 
        self._setupSensor()

    def _setupSensor(self) -> None: 
        """Config bytes for activating mesurement mode and resolution of sensor output(data_format)
        """
        # Power control register (0x2D): Set measurement mode
        self.bus.write_byte_data(self.address, 0x2D, 0x08)  # 0000 1000 (Measurement mode)
        
        # Data format register (0x31): Set full resolution and ±2g range
        self.bus.write_byte_data(self.address, 0x31, 0x08)  # 0000 1000 (Full resolution, ±2g)
    
    def readData(self) -> Dict[str, float]:
        """Read acceleration x,y,z also any event related to it.

        Returns:
            Dict[str, float]: A dictionary containing the acceleration and the triggered events
        """
        # Read raw data for each axis (16 bits per axis)
        data = self.bus.read_i2c_block_data(self.address, 0x32, 6)

        # Convert the data to signed 16-bit integers
        x = self._convertData(data[1] << 8 | data[0])
        y = self._convertData(data[3] << 8 | data[2])
        z = self._convertData(data[5] << 8 | data[4])

        # Scale the values based on sensitivity (4 mg/LSB for the full resolution mode
        # Convert to g all  values
        x = x * 0.004  
        y = y * 0.004  
        z = z * 0.004  

        return {"x": x, "y": y, "z": z}

    def _convertData(self, value:int) -> int:
        """Convert the raw data, to a signed intenteger

        Args:
            value (int): Raw integer data

        Returns:
            int: Signed integer
        """
        # If the value is greater than 32767, it is a negative value in 2's complement form
        return value - 65536 if value > 32767 else value
    
    def __del__ (self):
        """Destructor, just close the bus
        """
        self.bus.close()