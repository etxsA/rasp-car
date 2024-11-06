import RPi.GPIO as GPIO
from typing import List


def setGPIOmode(p=True) -> None:
    """Function ensures GPIO.BOARD mode is set.
    Args:
        p    (bool): If True output is enabled

    """
    current_mode = GPIO.getmode()
    
    if(current_mode == GPIO.BOARD):
        if(p):
            print("BOARD mode already set")
        return
    else:
        if(p):
            print("Other GPIO mode set previously, setting it to BOARD")
        GPIO.setmode(GPIO.BOARD)

def setPinsAsOut(pins: List[int], p=True) -> bool:
    """Sets pins in list to work in output mode.
    Args:
        pins (List[int]): List of pins to setup
        p    (bool): If True output is enabled
    Returns:
        bool: True if succes, False if failed
    """
    try:
        for pin in pins: 
            GPIO.setup(pin, GPIO.OUT)
        return True
    
    except Exception as e:
        if(p):
            print(e)
        return False
    
def setOutput(pins: List[int], states: List[bool]) -> bool:
    """Sets output of provided pins according to a state List corresponding to each pin
    Args:
        pins (List[int]): List of pin numbers to set output
        states (List[bool]): List of states(0, 1) to set pins to
    Returns:
        bool: If different size arrays fails, returns False
    """
    # Ensure Same Size
    if(len(pins) != len(states)):
        return False
    # Setup pin by pin
    for pin, state in enumerate(states):
        if(state):
            GPIO.output(pins[pin], GPIO.HIGH)
        else:  
            GPIO.output(pins[pin], GPIO.LOW)
    
    return True