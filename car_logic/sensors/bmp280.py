# A simple implementation of BMP280 without external dependencies
# All memory locations and registers where obtained from the datashet
# https://cdn-shop.adafruit.com/datasheets/BST-BMP280-DS001-11.pdf
import smbus

from typing import Dict

class BMP280:

    def __init__(self, address=0x76, seaLevelPressure=1013.25) -> None:
        """Initializes the sensor, reads the calibration data, and prepares it
        for reading the temperature, pressure, and calculation of altitude.

        Args:
            address (hexadecimal, optional): I2C address of the sensor. Defaults to 0x76.
            seaLevelPressure (float, optional): Reference Sea Level Pressure in hPa. Defaults to 1013.25.
        """ 
        self.address = address
        self.bus = smbus.SMbus(1) # Only one bus in the rasp
        self.calibrationParams = self._readCalibrationData()
        self.seaLevelPressure = seaLevelPressure

        # Start setup
        self._setupSensor()

    def _setupSensor(self) -> None:
        """Simply config the sensore and prepare to read, setting config registers according to datasheet
        """
        # Write config registers
        self.bus.write_byte_data(self.address, 0xF4, 0x27)  # Setting control meas
        self.bus.write_byte_data(self.address, 0xF5, 0x27)

    def _readCalibrationData(self) -> Dict[str, int]:

        calib = self.bus.read_i2c_bloc_data(self.address, 0x88, 24)

        params = {
            'dig_T1': calib[1] << 8 | calib[0],
            'dig_T2': self._signed(calib[3] << 8 | calib[2]),
            'dig_T3': self._signed(calib[5] << 8 | calib[4]),
            'dig_P1': calib[7] << 8 | calib[6],
            'dig_P2': self._signed(calib[9] << 8 | calib[8]),
            'dig_P3': self._signed(calib[11] << 8 | calib[10]),
            'dig_P4': self._signed(calib[13] << 8 | calib[12]),
            'dig_P5': self._signed(calib[15] << 8 | calib[14]),
            'dig_P6': self._signed(calib[17] << 8 | calib[16]),
            'dig_P7': self._signed(calib[19] << 8 | calib[18]),
            'dig_P8': self._signed(calib[21] << 8 | calib[20]),
            'dig_P9': self._signed(calib[23] << 8 | calib[22]),
        }
        
        return params
    
    def _signed(self, value: int) -> int:
        """Helper function to convert from unsigned to signed

        Args:
            value (unsiged int ): Unsigned short to convert

        Returns:
            int: The signed version of the short
        """
        return value - 65536 if value > 32767 else value

    def readData(self) -> Dict[str, float]:


        # Raw data
        data = self.bus.read_i2c_block_data(self.address, 0xF7, 6)

        # Combining bits to form integer
        adcP = data[0] << 12 | data[1] << 4 | data[2] >> 4
        adcT = data[3] << 12 | data[4] << 4 | data[5] >> 4

        # Use class priv methods to calc the different values

        temperature = self._calculateTemperature(adcT)
        pressure = self._calculatePressure(adcP)
        altitude = self._calculateAltitude(pressure)

        return {"temperature": temperature, 
                "pressure": pressure,
                "altitude": altitude }
    
    def _calculateTemperature(self, adcT: float) -> float:
        """Calculate Temperature using formula provided in the datasheet

        Args:
            adcT (float): Analog data of temperature

        Returns:
            float: Proccesd value of temperature
        """
        var1 = (((adcT >> 3) - (self.calibrationParams['dig_T1'] << 1)) *
                self.calibrationParams['dig_T2']) >> 11
        var2 = (((((adcT >> 4) - self.calibrationParams['dig_T1']) *
                  ((adcT >> 4) - self.calibrationParams['dig_T1'])) >> 12) *
                self.calibrationParams['dig_T3']) >> 14
        tFine = var1 + var2
        temperature = (tFine * 5 + 128) >> 8
        self.tFine = tFine
        return temperature / 100.
    
    def _calculatePressure(self, adcP: float) -> float:
        """Calculation according to datasheet for pressure

        Args:
            adcP (float): Analog raw data of pressure

        Returns:
            float: Pressure in hPa
        """
        var1 = (self.tFine / 2.0) - 64000.0
        var2 = var1 * var1 * self.calibrationParams['dig_P6'] / 32768.0
        var2 = var2 + var1 * self.calibrationParams['dig_P5'] * 2.0
        var2 = (var2 / 4.0) + (self.calibrationParams['dig_P4'] * 65536.0)
        var1 = (self.calibrationParams['dig_P3'] * var1 * var1 / 524288.0 +
                self.calibrationParams['dig_P2'] * var1) / 524288.0
        var1 = (1.0 + var1 / 32768.0) * self.calibrationParams['dig_P1']
        if var1 == 0:
            return 0  # Avoid division by zero
        pressure = 1048576.0 - adcP
        pressure = ((pressure - var2 / 4096.0) * 6250.0) / var1
        var1 = self.calibrationParams['dig_P9'] * pressure * pressure / 2147483648.0
        var2 = pressure * self.calibrationParams['dig_P8'] / 32768.0
        pressure = pressure + (var1 + var2 + self.calibrationParams['dig_P7']) / 16.0
        
        return pressure / 100.0  # Convert to hPa
    
    def _calculateAltitude(self, pressure: float) -> float:
        """Calculate altitude based on the pressure provided

        Args:
            pressure (float): Pressure in hPa

        Returns:
            float: Current altitude
        """
        altitude = 44330.0 * (1.0 - (pressure / self.seaLevelPressure) ** (1/5.255))
        return altitude
    
    def __del__(self):
        """Just close the bus when destructed
        """
        self.bus.close()