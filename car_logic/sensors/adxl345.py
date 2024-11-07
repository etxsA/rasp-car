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


    def __init__(self, address=0x53, rangeSetting=0x00) -> None: 
        """Initializes the ADXL345 sensor, sets it to measurement mode and changes the data format

        Args:
            address (hexadecimal, optional): i2c Address of the sensor. Defaults to 0x53.
             rangeSetting (hexadecimal): Range setting 
             (0x00 for ±2g, 0x01 for ±4g, 0x02 for ±8g, 0x03 for ±16g) : Defaults to 0x00
        """
        self.address = address
        self.bus = smbus.SMBus(1)
        self.rangeSetting = rangeSetting
        # Initialization 
        self._setupSensor(self.rangeSetting)

        # Enable Events

    def _setupSensor(self, rangeSetting) -> None: 
        """Config bytes for activating mesurement mode and resolution of sensor output(data_format)

        Args:
            rangeSetting (hexadecimal): Range setting for the accelerometer (±2g, ±4g, ±8g, ±16g)
        """
        # Power control register (0x2D): Set measurement mode
        self.bus.write_byte_data(self.address, 0x2D, 0x08)  # 0000 1000 (Measurement mode)
        
        # Data format register (0x31): Set full resolution and ±2g range
        dataFormat = 0x08 | rangeSetting
        self.bus.write_byte_data(self.address, 0x31, dataFormat)  # 0000 1000 (Full resolution, ±2g)
    
    def enableTapDetection(self, threshold=30, duration=20, latent=80, window=100) -> None:
        """Enable single and doble tap detection

        Args:
            threshold (int, optional): Tap threshold value(62.5). Defaults to 30.
            duration (int, optional): Tap duration in milliseconds (625 µs/LSB). Defaults to 20.
            latent (int, optional):   Latency for double tap (1.25 ms/LSB). Defaults to 80.
            window (int, optional): Double tap time window (1.25 ms/LSB). Defaults to 100.
        """
        self.bus.write_byte_data(self.address, 0x1D, threshold)  # Set tap threshold
        self.bus.write_byte_data(self.address, 0x21, duration)   # Set tap duration
        self.bus.write_byte_data(self.address, 0x22, latent)     # Set latency for double-tap
        self.bus.write_byte_data(self.address, 0x23, window)     # Set window for double-tap
        self.bus.write_byte_data(self.address, 0x2A, 0x7F)      # Enable tap axes
        self.bus.write_byte_data(self.address, 0x2E, 0x60)      # Enable single and double tap interrupts

    def enableFreeFallDetection(self, threshold=7, time=45) -> None:
        """
        Enables free-fall detection on the ADXL345.

        Args:
            threshold (int, optional): Free fall threshold in LSB (62.5 mg/LSB). Defaults to 7.
            time (int, optional): Minimum time for free-fall detection in milliseconds (5 ms/LSB). Defaults to 45.
        """ 
        self.bus.write_byte_data(self.address, 0x28, threshold)  # Free-fall threshold
        self.bus.write_byte_data(self.address, 0x29, time)       # Free-fall time
        self.bus.write_byte_data(self.address, 0x2E, 0x04)      # Enable free-fall interrupt

    def enableMotionDetection(self, actThreshold=30, inactThreshold=15, time=10) -> None:
        """
        Enables activity and inactivity detection on the ADXL345.

        Args:
            actThreshold (int, optional): Activity threshold in LSB (62.5 mg/LSB). Defaults to 30.
            inactThreshold (int, optional): Inactivity threshold in LSB (62.5 mg/LSB). Defaults to 15.
            time (int, optional): Inactivity time in seconds. Defaults to 10.
        """
        self.bus.write_byte_data(self.address, 0x24, actThreshold)   # Activity threshold
        self.bus.write_byte_data(self.address, 0x25, inactThreshold) # Inactivity threshold
        self.bus.write_byte_data(self.address, 0x26, time)            # Inactivity time
        self.bus.write_byte_data(self.address, 0x27, 0xF0)            # Activity/inactivity control
        self.bus.write_byte_data(self.address, 0x2E, 0x18)            # Enable activity/inactivity interrupts

    def _readEvents(self) -> str:
        """
        Reads the INT_SOURCE register to determine which event occurred.

        Returns:
            str: The detected event as a string (e.g., "tap", "double tap", "free fall", "motion", or "none").
        """
        interruptSource = self.bus.read_byte_data(self.address, 0x30)
        # Map the INT_SOURCE bits to specific events
        if interruptSource & 0x60:
            return "tap" if interruptSource & 0x40 else "double tap"
        elif interruptSource & 0x04:
            return "free fall"
        elif interruptSource & 0x18:
            return "motion"
        else:
            return "none"

    def readData(self) -> Dict[str, float]:
        """Read acceleration x,y,z also any event related to it.

        Returns:
            Dict[str, float]: A dictionary containing the acceleration and the triggered events,
            event as a string ("tap", "double tap", "free fall", "motion", or "none").
        """
        # Read raw data for each axis (16 bits per axis)
        data = self.bus.read_i2c_block_data(self.address, 0x32, 6)

        # Convert the data to signed 16-bit integers
        x = self._convertData(data[1] << 8 | data[0])
        y = self._convertData(data[3] << 8 | data[2])
        z = self._convertData(data[5] << 8 | data[4])

        # Scale factor in full resolution mode for the selected range
        scaleFactors = {0x00: 0.004, 0x01: 0.008, 0x02: 0.016, 0x03: 0.032}  # g/LSB for each range
        scaleFactor = scaleFactors.get(self.rangeSetting, 0.004)

        # Scale the values based on sensitivity (4 mg/LSB for the full resolution mode
        # Convert to g all  values
        x = x * scaleFactor  
        y = y * scaleFactor
        z = z * scaleFactor  

        # Read Current event 
        event = self._readEvents()

        return {"x": x, "y": y, "z": z, "events": event}

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