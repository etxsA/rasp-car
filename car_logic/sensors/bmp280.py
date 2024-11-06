# A simple implementation of BMP280 without external dependencies
# All memory locations and registers where obtained from the datashet
# https://cdn-shop.adafruit.com/datasheets/BST-BMP280-DS001-11.pdf
import smbus
import time

from typing import Dict

class BMP280:

    def __init__(self, address=0x76) -> None:
        
        self.bus = smbus.SMbus(1) # Only one bus in the rasp
        self.address = address
        self.calibrationParams = self._readCalibrationData()
    

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
    
    def _signed(self, value) -> int:
        """Helper function to convert from unsigned to signed

        Args:
            value (unsiged int ): Unsigned short to convert

        Returns:
            int: The signed version of the short
        """
        return value - 65536 if value > 32767 else value