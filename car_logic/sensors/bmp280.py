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