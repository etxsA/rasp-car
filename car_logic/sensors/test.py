import time
from . import SensorController

def display_menu():
    print("\nSensor Controller Menu:")
    print("1. Read Light Sensor (ADS1115)")
    print("2. Read Accelerometer (ADXL345)")
    print("3. Read Environment Sensor (BMP280)")
    print("4. Read Distance Sensor (Ultrasonic)")
    print("5. Read All Sensors")
    print("6. Exit")

def main():
    controller = SensorController()  # Create an instance of the SensorController class

    try:
        while True:
            display_menu()
            choice = input("Select an option (1-6): ")

            if choice == '1':
                light_data = controller.readLightSensor()
                print("Light Sensor Data:", light_data)
            elif choice == '2':
                accel_data = controller.readAccelerometer()
                print("Accelerometer Data:", accel_data)
            elif choice == '3':
                env_data = controller.readEnvironmentSensor()
                print("Environment Sensor Data:", env_data)
            elif choice == '4':
                dist_data = controller.readDistanceSensor()
                print("Distance Sensor Data:", dist_data)
            elif choice == '5':
                all_data = controller.readAllSensors()
                print("All Sensor Data:", all_data)
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please choose a number from 1 to 6.")

            # Pause briefly to allow user to see action output
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nProgram interrupted with KeyboardInterrupt. Exiting...")
    finally:
        del controller  # Ensure all sensor resources are cleaned up

if __name__ == "__main__":
    main()
