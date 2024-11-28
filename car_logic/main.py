import time
import threading
import argparse
import paho.mqtt.client as mqtt
from . import setupControllers
from .connections import APIController

def parse_args():
    """Parse command-line arguments using argparse."""
    parser = argparse.ArgumentParser(description="Raspcar: A car controlled by sensors and MQTT.")
    
    # Command-line arguments for baseUrl, MQTT broker, and port
    parser.add_argument('--baseUrl', type=str, required=True, help="Base URL of the API")
    parser.add_argument('--mqttBroker', type=str, help="MQTT broker address (optional, will be fetched from API if not provided)")
    parser.add_argument('--mqttPort', type=int, help="MQTT broker port (optional, will be fetched from API if not provided)")
    parser.add_argument('--baseTopic', type=str, default="raspcar", help="Base topic for MQTT")

    return parser.parse_args()

class Raspcar:
    def __init__(self, baseUrl: str, mqtt_broker="localhost", mqtt_port=1883, base_topic="raspcar"):
        """Initialize Raspcar, fetch configuration, and set up controllers."""
        self.baseUrl = baseUrl
        self.base_topic = base_topic
        
        # Initialize APIController to fetch config
        self.api = APIController(baseUrl)

        # Fetch the configuration from the API
        self.fetch_config()

        # Initialize controllers
        self.motors, self.sensors, self.api, self.mqtt, self.db = setupControllers(self.baseUrl, self.mqtt_broker, self.mqtt_port, self.base_topic)

        # Initialize other components
        self.ultrasonic = self.sensors.distanceSensor  # Ultrasonic sensor from SensorController
        self.mqtt_client = self.mqtt.client

        # Flag to control thread stopping
        self.stop_thread = False

        # Connect to MQTT broker
        self.connectMQTT()

    def fetch_config(self):
        """Fetch configuration from API."""
        config = self.api.getData("config")
        print(f"Config fetched from API: {config}")

        if config.get("mqtt"):
            mqtt_config = config["mqtt"]
            self.mqtt_broker = mqtt_config.get("broker", "localhost")
            self.mqtt_port = mqtt_config.get("port", 1883)
            self.base_topic = mqtt_config.get("topic", "raspcar")

    def connectMQTT(self):

        def on_message(client, userdata, msg):
            payload = msg.payload.decode("utf-8")
            print(f"Received message: {payload}")

            # If message controls motors, process it here
            if payload == "STOP":
                self.motors.stop()
            elif payload == "FORWARD":
                self.motors.forward()
            elif payload == "BACKWARD":
                self.motors.backward()

        # Set the MQTT client callback
        self.mqtt_client.on_message = on_message

        # Connect to the broker
        self.mqtt_client.connect(self.mqtt_broker, self.mqtt_port)
        self.mqtt_client.loop_start()

    def send_sensor_data(self):
        """Send sensor data concurrently but at different intervals."""
        def send_light_sensor_data():
            while not self.stop_thread:
                light_data = self.sensors.readLightSensor()
                print(f"Light Sensor Data: {light_data}")
                self.mqtt.sendData(light_data, "lightSensor")
                time.sleep(2)

        def send_accelerometer_data():
            while not self.stop_thread:
                accel_data = self.sensors.readAccelerometer()
                print(f"Accelerometer Data: {accel_data}")
                self.mqtt.sendData(accel_data, "accelerometer")
                time.sleep(3)

        def send_environment_sensor_data():
            while not self.stop_thread:
                env_data = self.sensors.readEnvironmentSensor()
                print(f"Environment Sensor Data: {env_data}")
                self.mqtt.sendData(env_data, "environmentSensor")
                time.sleep(4)

        def send_distance_sensor_data():
            while not self.stop_thread:
                dist_data = self.sensors.readDistanceSensor()
                print(f"Distance Sensor Data: {dist_data}")
                self.mqtt.sendData(dist_data, "distanceSensor")
                time.sleep(5)

        # Start the threads for each sensor
        threading.Thread(target=send_light_sensor_data, daemon=True).start()
        threading.Thread(target=send_accelerometer_data, daemon=True).start()
        threading.Thread(target=send_environment_sensor_data, daemon=True).start()
        threading.Thread(target=send_distance_sensor_data, daemon=True).start()

    def monitor_ultrasonic_interrupt(self):
        """Monitor ultrasonic distance and trigger interrupt if an obstacle is detected."""
        while not self.stop_thread:
            distance = self.ultrasonic.measureDistance()
            print(f"Ultrasonic Distance: {distance} cm")
            if distance < 5:  # Interrupt condition
                print("Obstacle detected! Stopping motors and backing up.")
                self.motors.stop()
                time.sleep(1)
                self.motors.backward()
                time.sleep(2)
                self.motors.stop()
            time.sleep(1)

    def run(self):
        """Start the main execution, including sensor data collection and ultrasonic interrupt monitoring."""
        # Start concurrent sensor data sending
        self.send_sensor_data()

        # Start monitoring ultrasonic interrupt
        threading.Thread(target=self.monitor_ultrasonic_interrupt, daemon=True).start()

        # Keep the main thread running
        while not self.stop_thread:
            time.sleep(1)

    def stop(self):
        """Stop all threads and operations."""
        self.stop_thread = True
        self.mqtt_client.disconnect()
        print("Raspcar stopped.")

if __name__ == "__main__":
    # Parse arguments and initialize Raspcar
    args = parse_args()
    raspcar = Raspcar(
        baseUrl=args.baseUrl,
        mqtt_broker=args.mqttBroker,
        mqtt_port=args.mqttPort,
        base_topic=args.baseTopic
    )
    
    try:
        # Run Raspcar
        raspcar.run()
    except KeyboardInterrupt:
        # Graceful exit on CTRL+C
        print("Stopping Raspcar...")
        raspcar.stop()
