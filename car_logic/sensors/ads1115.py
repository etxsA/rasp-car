import smbus
import time
from typing import Dict

class ADS1115:
    """
    ADS1115 ADC class to read voltage and light level from a photoresistor connected to the A0 pin.
    """

    def __init__(self, address=0x48, gain=0x02) -> None:
        """
        Initializes the ADS1115 with the specified I2C address and gain setting.

        Args:
            address (int): I2C address of the ADS1115. Defaults to 0x48.
            gain (int): Gain setting to set max input voltage (0x00 for ±6.144V, 0x01 for ±4.096V,
                        0x02 for ±2.048V, 0x03 for ±1.024V, etc.). Defaults to 0x02 for ±2.048V.
        """
        self.address = address
        self.bus = smbus.SMBus(1)
        self.gain = gain
        self._configure_adc()

    def _configure_adc(self) -> None:
        """
        Configures the ADS1115 to read from A0 with the specified gain.
        This configuration is set only once during initialization.
        """
        config = 0x4000  # Single-ended A0
        config |= 0x8000  # Start single conversion
        config |= self.gain << 9  # Set gain
        config |= 0x0100  # Set data rate to 128 SPS
        config |= 0x0003  # Single-shot mode

        toWrite = [(config >> 8) & 0xFF, config & 0xFF]
        # Write the configuration to the ADC
        self.bus.write_i2c_block_data(self.address, 0x01, toWrite)

    def readData(self) -> Dict[str, float]:
        """
        Reads the voltage from the A0 pin and converts it to a light level (percentage).

        Returns:
            dict: A dictionary containing the voltage and light level.
        """
        try:
            # Wait for conversion to complete (takes ~8 ms at 128 SPS)
            time.sleep(0.008)

            # Read the conversion result from the data register
            result = self.bus.read_i2c_block_data(self.address, 0x00, 2)
            rawValue = (result[0] << 8) | result[1]
            rawValue = self._convertData(rawValue)

            # Calculate the voltage based on gain
            voltage = self._convertToVoltage(rawValue)

            # Calculate light level as a percentage (assuming max light = max voltage)
            lightLevel = (voltage / self.maxVoltage()) * 100

            return {"voltage": voltage, "lightLevel": lightLevel}
        except Exception as e:
            print(f"Error reading from ADS1115: {e}")
            return {"voltage": 0.0, "lightLevel": 0.0}

    def _convertData(self, value: int) -> int:
        """Convert the raw data to a signed integer

        Args:
            value (int): Raw integer data

        Returns:
            int: Signed integer
        """
        return value - 65536 if value > 32767 else value

    def _convertToVoltage(self, rawValue: int) -> float:
        """
        Converts the raw ADC value to a voltage based on the gain setting.

        Args:
            rawValue (int): The raw ADC reading from the ADS1115.

        Returns:
            float: The converted voltage.
        """
        fsValues = {
            0x00: 6.144,
            0x01: 4.096,
            0x02: 2.048,
            0x03: 1.024,
            0x04: 0.512,
            0x05: 0.256
        }
        maxVoltage = fsValues.get(self.gain, 2.048)  # Default to ±2.048V
        voltage = (rawValue / 32768.0) * maxVoltage
        return voltage

    def maxVoltage(self) -> float:
        """
        Returns the maximum voltage for the current gain setting.

        Returns:
            float: The maximum input voltage.
        """
        fsValues = {
            0x00: 6.144,
            0x01: 4.096,
            0x02: 2.048,
            0x03: 1.024,
            0x04: 0.512,
            0x05: 0.256
        }
        return fsValues.get(self.gain, 2.048)  # Default to ±2.048V

    def __del__(self) -> None:
        """
        Destructor to clean up the I2C bus when the object is deleted.
        """
        self.bus.close()

