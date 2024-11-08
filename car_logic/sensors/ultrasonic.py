# Really Simple implementation of HC-SR04
import RPi.GPIO as GPIO
import time

from .. import setGPIO as sg
from typing import Dict

# Trig to GPIO 4 -> Pin 7
# Echo to GPIO 6 -> Pin 31

class Ultrasonic:
    """
    Ultrasonic sensor class to measure distance using the HC-SR04 sensor.

    This class configures the specified GPIO pins for the ultrasonic sensor's trigger
    and echo, allowing distance measurement by calculating the time taken for a pulse
    to return to the echo pin. The sensor emits an ultrasonic pulse, which bounces
    back when it encounters an object, and the time taken for this pulse to return is
    used to calculate the distance based on the speed of sound.

    Attributes:
    -----------
    trig : int
        GPIO pin number for the trigger pin.
    echo : int
        GPIO pin number for the echo pin.

    Methods:
    --------
    __init__(trig=7, echo=31, p=False):
        Initializes the ultrasonic sensor by setting up the trigger and echo pins.
    measureDistance(p=False) -> float:
        Measures the distance to an object in front of the sensor in centimeters.
    """

    def __init__(self, trig=7, echo=31, p=False) -> None:
        """
        Initializes the Ultrasonic sensor with specified GPIO pins for the trigger
        and echo. Sets up the GPIO mode, configures the pins, and prepares the sensor
        for measuring distance.

        Parameters:
        -----------
        trig : int
            GPIO pin number for the trigger pin (default is 7).
        echo : int
            GPIO pin number for the echo pin (default is 31).
        p : bool
            Print mode for debugging, if set to True(Not used at the moment) (default is False).
        """
        sg.setGPIOmode(False)
        GPIO.setup(trig, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)

        self.trig = trig
        self.echo = echo

        GPIO.output(trig, GPIO.LOW)
        time.sleep(2)  # Allow sensor to settle

    def measureDistance(self) -> Dict[str, float]:
        """
        Sends a pulse from the trigger pin and measures the time taken for the
        pulse to return to the echo pin, calculating the distance based on the speed
        of sound. Returns the distance in centimeters.

        Parameters:
        -----------
        p : bool
            If set to True, prints the calculated distance for debugging purposes (default is False).

        Returns:
        --------
        float
            The distance to an object in front of the sensor in centimeters.
        """
        # Send a pulse to the trig pin
        GPIO.output(self.trig, GPIO.HIGH)
        time.sleep(0.00001)  # Pulse for 10 microseconds
        GPIO.output(self.trig, GPIO.LOW)

        # Measure the time of the pulse
        start_time = time.time()
        while GPIO.input(self.echo) == 0:
            start_time = time.time()

        end_time = time.time()
        while GPIO.input(self.echo) == 1:
            end_time = time.time()

        # Calculate the duration and distance
        duration = end_time - start_time
        distance = (duration * 34300) / 2  # 34300 cm/s is the speed of sound
        return {"distance": distance}

    def __del__(self):
        """Destructor to clean up GPIO resources when the object is deleted."""
        GPIO.cleanup()