from .sensors import Ultrasonic
from .sensors import BMP280
from .sensors import ADXL345
from .sensors import ADS1115

ultratest = Ultrasonic()
bmptest = BMP280()
acctest = ADXL345()
photorestest = ADS1115(gain=0x01)



print(f"Distance in cm: {ultratest.measureDistance()}")
print(bmptest.readData())
print(acctest.readData())
print(photorestest.readData())




