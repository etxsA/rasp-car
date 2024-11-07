from .sensors import Ultrasonic
from .sensors import BMP280
from .sensors import ADXL345

ultratest = Ultrasonic()
bmptest = BMP280()
acctest = ADXL345()


print(f"Distance in cm: {ultratest.measureDistance()}")
print(bmptest.readData())
print(acctest.readData())




