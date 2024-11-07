import time
import argparse
import requests
from .sensors import SensorController
from .motors.movements import MovementController

def getApiEndpoints(baseUrl):
    """Constructs API endpoints for each sensor based on the base URL."""
    return {
        "lightSensor": f"http://{baseUrl}/light_sensor",
        "accelerometer": f"http://{baseUrl}/accelerometer",
        "environmentSensor": f"http://{baseUrl}/environment_sensor",
        "distanceSensor": f"http://{baseUrl}/distance_sensor"
    }

def displayMainMenu():
    print("\nMain Menu:")
    print("1. Control Motors")
    print("2. Sensor Control")
    print("3. Send Data to API")
    print("4. Exit")

def displaySensorMenu():
    print("\nSensor Control Menu:")
    print("1. Read Light Sensor (ADS1115)")
    print("2. Read Accelerometer (ADXL345)")
    print("3. Read Environment Sensor (BMP280)")
    print("4. Read Distance Sensor (Ultrasonic)")
    print("5. Read All Sensors")
    print("6. Back to Main Menu")

def displayApiMenu():
    print("\nSend Data to API Menu:")
    print("1. Send Light Sensor Data")
    print("2. Send Accelerometer Data")
    print("3. Send Environment Sensor Data")
    print("4. Send Distance Sensor Data")
    print("5. Send All Sensor Data")
    print("6. Back to Main Menu")

def controlMotors(motorController):
    print("\nMotor Control Options:")
    print("1. Move Forward")
    print("2. Move Backward")
    print("3. Turn Left")
    print("4. Turn Right")
    print("5. Stop")
    choice = input("Select an option (1-5): ")

    if choice == '1':
        motorController.moveForward()
        print("Moving forward")
    elif choice == '2':
        motorController.moveBackward()
        print("Moving backward")
    elif choice == '3':
        motorController.turnLeft()
        print("Turning left")
    elif choice == '4':
        motorController.turnRight()
        print("Turning right")
    elif choice == '5':
        motorController.stop()
        print("Motors stopped")
    else:
        print("Invalid option. Please choose a number from 1 to 5.")

def sendDataToApi(sensorData, endpoint):
    """Sends data to the specified API endpoint."""
    try:
        response = requests.post(endpoint, json=sensorData)
        if response.status_code == 200:
            print(f"Data sent to {endpoint} successfully.")
        else:
            print(f"Failed to send data to {endpoint}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to {endpoint}: {e}")

def main(baseUrl):
    # Create instances of the MovementController and SensorController classes
    motorController = MovementController()
    sensorController = SensorController()
    apiEndpoints = getApiEndpoints(baseUrl)

    try:
        while True:
            displayMainMenu()
            choice = input("Select an option (1-4): ")

            if choice == '1':
                controlMotors(motorController)
            elif choice == '2':
                # Sensor Control Submenu
                while True:
                    displaySensorMenu()
                    sensorChoice = input("Select a sensor option (1-6): ")

                    if sensorChoice == '1':
                        lightData = sensorController.readLightSensor()
                        print("Light Sensor Data:", lightData)
                    elif sensorChoice == '2':
                        accelData = sensorController.readAccelerometer()
                        print("Accelerometer Data:", accelData)
                    elif sensorChoice == '3':
                        envData = sensorController.readEnvironmentSensor()
                        print("Environment Sensor Data:", envData)
                    elif sensorChoice == '4':
                        distData = sensorController.readDistanceSensor()
                        print("Distance Sensor Data:", distData)
                    elif sensorChoice == '5':
                        allData = sensorController.readAllSensors()
                        print("All Sensor Data:", allData)
                    elif sensorChoice == '6':
                        break
                    else:
                        print("Invalid option. Please choose a number from 1 to 6.")
                    time.sleep(0.5)

            elif choice == '3':
                # Send to API Submenu
                while True:
                    displayApiMenu()
                    apiChoice = input("Select an API option (1-6): ")

                    if apiChoice == '1':
                        lightData = sensorController.readLightSensor()
                        sendDataToApi(lightData, apiEndpoints["lightSensor"])
                    elif apiChoice == '2':
                        accelData = sensorController.readAccelerometer()
                        sendDataToApi(accelData, apiEndpoints["accelerometer"])
                    elif apiChoice == '3':
                        envData = sensorController.readEnvironmentSensor()
                        sendDataToApi(envData, apiEndpoints["environmentSensor"])
                    elif apiChoice == '4':
                        distData = sensorController.readDistanceSensor()
                        sendDataToApi(distData, apiEndpoints["distanceSensor"])
                    elif apiChoice == '5':
                        # Send all sensor data to API
                        allData = sensorController.readAllSensors()
                        for sensor, data in allData.items():
                            endpoint = apiEndpoints.get(sensor)
                            if endpoint:
                                sendDataToApi(data, endpoint)
                        print("All sensor data sent to API.")
                    elif apiChoice == '6':
                        break
                    else:
                        print("Invalid option. Please choose a number from 1 to 6.")
                    time.sleep(0.5)

            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please choose a number from 1 to 4.")

    except KeyboardInterrupt:
        print("\nProgram interrupted with KeyboardInterrupt. Exiting...")
    finally:
        # Clean up resources
        del motorController
        del sensorController

if __name__ == "__main__":
    # Parse the base URL from command-line arguments
    parser = argparse.ArgumentParser(description="Sensor and Motor Controller with API integration.")
    parser.add_argument("baseUrl", type=str, help="The base URL for the API server (e.g., http://yourapi.com)")
    args = parser.parse_args()
    
    # Run the main program with the provided base URL
    main(args.baseUrl)
