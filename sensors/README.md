# Description

## SETUP 
To work with each one of the sensors, you need to install a specific package, in this case we use primarly the adafruit library, below is relation of each package according to the sensor. 

|Sensor|Used Package|
|---|---|
|BME/BMP-280 | adafruit-circuitpython-bmp280 / adafruit-circuitpython-bme280|
| ||

_* All of the packages are listed in the project requirements_
```bash
pip3 install RPi.GPIO
```

## How to wire it up 
![Schematic](./sketch.png)
This is an example view, not strictly needed. You can use the pins as you wish. The showed layout is already declared as default.

- ENA -> 32 (GPIO12)
- IN1 -> 35 (GPIO19)
- IN2 -> 37 (GPIO26)
- ENB -> 40 (GPIO21)
- IN3 -> 36 (GPIO16)
- IN4 -> 38 (GPIO20)

The class __MovementController__ declared in _movements.py_ sets the pins, in case you chose other, specify them to the constructor: 
```python 
def __init__(self,
                  ENA:int=32, IN1:int=35, IN2:int=37,
                  ENB:int=40, IN3:int=36, IN4:int=38, p:bool=True) -> None:
```

## Usage

The class __MovementController__ provides with methods for modifying the movements of the motor, as listed below:
- __foward()__: Foward movement
- __backwards()__: Backwards movement
- __right()__: right turn movement
- __left()__: left turn movement
- __spinRight()__: right spin movement
- __spinLeft()__: left spin movement
- __stop()__: Stop all motor movement

All of the movement functions can take time as an optional parameter, to specify wait time after executing the movement, __default = 0.5s__

```python
move = MovementController()
move.foward(1) # 1 Second wait
```
When performing a movement, the action will be printed by default: 
```
>
Moving Foward
```
To prevent the behaviour, when creating an object of the controller, set the default parameter __p to False__

## Testing 
Follow any previous setup and run the _test.py_ script

```bash
> python test.py
```



