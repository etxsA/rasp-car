# Rasp-Car
A Raspberry pi 4b car, this is a project implementing the use of python to code and build a functioning car

## Code Requirements 
To execute any of the code in the subfolders, ensure you are running on a python virtual environment (venv). If no, create one and use it from the termimal: 
```bash
python3 -m venv rasp-car
source rasp-car/bin/activate
```

If you need to get out of the venv, just use __deactivate__
```bash
deactivate
```

Ensuring you are in a venv, install the requirements using: 
```bash
pip3 install -r requirements.txt
```

Now you can run any part of the code, ensure you read the documentation provided in every part and in the code.

## File Descriptions

### Connections

This folder contains the files used to communicate between the different sensors via HTTP requests. Each sensor is mapped to an endpoint with API urls.

### Motors

The motors folder provides functionality to control motor movements using a Raspberry Pi and a motor driver. It includes code to initialize and manage motor directions (forward, backward, left, right, and spins) through GPIO pins, along with a test script to verify motor operations.

### Sensors
  
This folder provides setup instructions and code for controlling motor movements and connecting sensors to a Raspberry Pi. It includes necessary library installations, wiring guidance, and a class to manage motor actions. Testing scripts are also provided to verify the setup and functionality.

### setGPIO.py

This script provides utility functions for configuring and controlling GPIO pins on a Raspberry Pi. It includes functions to configure specific pins as outputs, and set output states for those pins. These functions are designed to handle errors and offer optional print feedback to indicate the status of operations.

### setupControllers.py

This script provides a function to initialize and configure multiple controllers, including motor, sensor, API, MQTT, and database controllers. It retrieves configuration data from an API endpoint and uses optional parameters to override defaults for MQTT and database settings. If the API lacks necessary configurations, it raises an error. This setup ensures all controllers are ready for coordinated operation in a connected environment.

### test.py

This script provides a command-line interface to control motors, read sensor data, and manage data transmission through API, MQTT, and database connections. It initializes controllers for each component, enabling flexible interaction with motors and sensors and configurable data handling options.

