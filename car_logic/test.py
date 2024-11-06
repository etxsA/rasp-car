from .sensors import Ultrasonic
from .sensors import BMP280
ultratest = Ultrasonic()
bmptest = BMP280()

print(f"Distance in cm: {ultratest.measureDistance()}")
print(bmptest.readData())




