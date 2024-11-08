import time
import argparse
from . import setupControllers

def displayMainMenu():
    print("\nMain Menu:")
    print("1. Control Motors")
    print("2. Sensor Control")
    print("3. Send Data to API")
    print("4. Send Data to MQTT")
    print("5. Exit")

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

def displayMqttMenu():
    print("\nSend Data to MQTT Menu:")
    print("1. Send Light Sensor Data")
    print("2. Send Accelerometer Data")
    print("3. Send Environment Sensor Data")
    print("4. Send Distance Sensor Data")
    print("5. Send All Sensor Data")
    print("6. Back to Main Menu")

def controlMotors(motor):
    print("\nMotor Control Options:")
    print("1. Move Forward")
    print("2. Move Backward")
    print("3. Turn Left")
    print("4. Turn Right")
    print("5. Stop")
    choice = input("Select an option (1-5): ")

    if choice == '1':
        motor.moveForward()
        print("Moving forward")
    elif choice == '2':
        motor.moveBackward()
        print("Moving backward")
    elif choice == '3':
        motor.turnLeft()
        print("Turning left")
    elif choice == '4':
        motor.turnRight()
        print("Turning right")
    elif choice == '5':
        motor.stop()
        print("Motors stopped")
    else:
        print("Invalid option. Please choose a number from 1 to 5.")


def main(baseUrl, mqttBroker, mqttPort, mqttTopic):
    # Create instances of the MovementController and sensors classes
    motor, sensors, apiC, mqttC = setupControllers(baseUrl, mqttBroker, mqttPort, mqttTopic)

    try:
        while True:
            displayMainMenu()
            choice = input("Select an option (1-5): ")

            if choice == '1':
                controlMotors(motor)
            elif choice == '2':
                # Sensor Control Submenu
                while True:
                    displaySensorMenu()
                    sensorChoice = input("Select a sensor option (1-6): ")

                    if sensorChoice == '1':
                        lightData = sensors.readLightSensor()
                        print("Light Sensor Data:", lightData)
                    elif sensorChoice == '2':
                        accelData = sensors.readAccelerometer()
                        print("Accelerometer Data:", accelData)
                    elif sensorChoice == '3':
                        envData = sensors.readEnvironmentSensor()
                        print("Environment Sensor Data:", envData)
                    elif sensorChoice == '4':
                        distData = sensors.readDistanceSensor()
                        print("Distance Sensor Data:", distData)
                    elif sensorChoice == '5':
                        allData = sensors.readAllSensors()
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
                        lightData = sensors.readLightSensor()
                        apiC.sendData(lightData, "lightSensor")
                    elif apiChoice == '2':
                        accelData = sensors.readAccelerometer()
                        apiC.sendData(accelData, "accelerometer")
                    elif apiChoice == '3':
                        envData = sensors.readEnvironmentSensor()
                        apiC.sendData(envData, "environmentSensor")
                    elif apiChoice == '4':
                        distData = sensors.readDistanceSensor()
                        apiC.sendData(distData, "distanceSensor")
                    elif apiChoice == '5':
                        # Send all sensor data to API
                        allData = sensors.readAllSensors()
                        for sensor, data in allData.items():
                            endpoint = apiC.endpoints.get(sensor)
                            if endpoint:
                                apiC.sendData(data, endpoint)
                        print("All sensor data sent to API.")
                    elif apiChoice == '6':
                        break
                    else:
                        print("Invalid option. Please choose a number from 1 to 6.")
                    time.sleep(0.5)

            elif choice == '4':
                # Send to MQTT Submenu
                while True:
                    displayMqttMenu()
                    mqttChoice = input("Select an MQTT option (1-6): ")

                    if mqttChoice == '1':
                        lightData = sensors.readLightSensor()
                        mqttC.sendData(lightData, "lightSensor")
                    elif mqttChoice == '2':
                        accelData = sensors.readAccelerometer()
                        mqttC.sendData(accelData, "accelerometer")
                    elif mqttChoice == '3':
                        envData = sensors.readEnvironmentSensor()
                        mqttC.sendData(envData, "environmentSensor")
                    elif mqttChoice == '4':
                        distData = sensors.readDistanceSensor()
                        mqttC.sendData(distData, "distance")
                    elif mqttChoice == '5':
                        # Send all sensor data to MQTT
                        allData = sensors.readAllSensors()
                        for sensor, data in allData.items():
                            topics = mqttC.topics
                            if sensor in topics.keys():
                                mqttC.sendData(data, sensor)
                        print("All sensor data sent to MQTT.")
                    elif mqttChoice == '6':
                        break
                    else:
                        print("Invalid option. Please choose a number from 1 to 6.")
                    time.sleep(0.5)

            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please choose a number from 1 to 5.")

    except KeyboardInterrupt:
        print("\nProgram interrupted with KeyboardInterrupt. Exiting...")
    finally:
        del mqttC
        del motor
        del sensors

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sensor and Motor Controller with API and MQTT integration.")
    parser.add_argument("baseUrl", type=str, help="The base URL for the API server (e.g., http://yourapi.com)")
    parser.add_argument("mqttBroker", nargs='?', type=str, help="The address of the MQTT broker")
    parser.add_argument("mqttPort", nargs='?', type=int, help="The port of the MQTT broker")
    parser.add_argument("mqttTopic", nargs='?', type=str, help="The base topic for MQTT (e.g., sensors)")
    args = parser.parse_args()
    
    main(args.baseUrl, args.mqttBroker, args.mqttPort, args.mqttTopic)
