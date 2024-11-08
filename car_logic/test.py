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

def controlSensor(sensors):
    while True:
        print("\nRead Sensor Data Menu:")
        print("1. Read Light Sensor Data")
        print("2. Read Accelerometer Data")
        print("3. Read Environment Sensor Data")
        print("4. Read Distance Sensor Data")
        print("5. Read All Sensor Data")
        print("6. Back to Main Menu")

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

def controlApi(apiC, sensors):
    while True:
        print("\nSend Data to API Menu:")
        print("1. Send Light Sensor Data")
        print("2. Send Accelerometer Data")
        print("3. Send Environment Sensor Data")
        print("4. Send Distance Sensor Data")
        print("5. Send All Sensor Data")
        print("6. Back to Main Menu")

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
                apiC.sendData(data, sensor)
            print("All sensor data sent to API.")
        elif apiChoice == '6':
            break
        else:
            print("Invalid option. Please choose a number from 1 to 6.")
        time.sleep(0.5)

def controlMqtt(mqttC, sensors):
    while True:
        print("\nSend Data to MQTT Menu:")
        print("1. Send Light Sensor Data")
        print("2. Send Accelerometer Data")
        print("3. Send Environment Sensor Data")
        print("4. Send Distance Sensor Data")
        print("5. Send All Sensor Data")
        print("6. Back to Main Menu")

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

def controlMotors(motor):
    while True: 
        print("\nMovement Controller Menu:")
        print("1. Move Forward")
        print("2. Move Backward")
        print("3. Turn Right")
        print("4. Turn Left")
        print("5. Spin Right")
        print("6. Spin Left")
        print("7. Stop")
        print("8. Exit")
        choice = input("Select an option (1-8): ")

        if choice == '1':
            motor.foward()
        elif choice == '2':
            motor.backwards()
        elif choice == '3':
            motor.right()
        elif choice == '4':
            motor.left()
        elif choice == '5':
            motor.spinRight()
        elif choice == '6':
            motor.spinLeft()
        elif choice == '7':
            motor.stop()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 8.")
        # Pause briefly to allow user to see action output
        time.sleep(0.5)


def main(baseUrl, mqttBroker, mqttPort, mqttTopic):
    # Create instances of the MovementController and sensors classes
    motor, sensors, apiC, mqttC = setupControllers(baseUrl, mqttBroker, mqttPort, mqttTopic)

    try:
        while True:
            displayMainMenu()
            choice = input("Select an option (1-5): ")

            # Send to each corresponding submenu
            if choice == '1':
                controlMotors(motor)
            elif choice == '2':
                controlSensor(sensors)
            elif choice == '3':
                controlApi(apiC, sensors)
            elif choice == '4':
                controlMqtt(mqttC, sensors)
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
