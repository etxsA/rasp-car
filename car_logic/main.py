import time
import threading
import argparse
import paho.mqtt.client as mqtt
from . import setupControllers
from . import APIController

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
        self.stop_thread = False  # Initialize stop_thread attribute
        self.api = APIController(baseUrl)
        
        # Fetch the configuration from the API
        self.fetch_config()

        # Initialize controllers
        self.motors, self.sensors, self.api, self.mqtt, self.db = setupControllers(baseUrl, mqtt_broker, mqtt_port, base_topic)

        # Initialize MQTT client
        self.mqtt.client.on_connect = self.on_connect
        self.mqtt.client.on_message = self.on_message
        self.mqtt.client.connect(mqtt_broker, mqtt_port)
        self.mqtt.client.loop_start()

        # Start threads for sensor data sending and ultrasonic interrupt
        self.start_sensor_threads()

    def on_connect(self, client, userdata, flags, rc):
        """Handle MQTT connection."""
        print(f"Connected to MQTT broker with result code {rc}")
        # Subscribe to the motor control topic
        client.subscribe(f"{self.base_topic}/motor_control")

    def on_message(self, client, userdata, msg):
        """Handle MQTT messages to control the motors."""
        message = msg.payload.decode()
        print(f"Received MQTT message: {message}")

        # Control motors based on received message
        if message == "forward":
            self.motors.foward()
        elif message == "backward":
            self.motors.backward()
        elif message == "stop":
            self.motors.stop()
        # Add more motor control conditions as needed

    def fetch_config(self):
        """Fetch the configuration from the API."""
        print("Fetching configuration from API...")
        config = self.api.getData("config")
        print("Configuration fetched:", config)

    def start_sensor_threads(self):
        """Start separate threads for each sensor to send data at different intervals."""
        # Start thread for each sensor
        threading.Thread(target=self.send_light_sensor_data, daemon=True).start()
        threading.Thread(target=self.send_accelerometer_data, daemon=True).start()
        threading.Thread(target=self.send_environment_sensor_data, daemon=True).start()
        threading.Thread(target=self.send_distance_sensor_data, daemon=True).start()
        threading.Thread(target=self.ultrasonic_interrupt, daemon=True).start()

    def send_light_sensor_data(self):
        """Send light sensor data at intervals."""
        while not self.stop_thread:
            light_data = self.sensors.readLightSensor()
            print(f"Light Sensor Data: {light_data}")
            self.mqtt.sendData(light_data, "lightSensor")
            time.sleep(2)  # Adjust the interval as needed

    def send_accelerometer_data(self):
        """Send accelerometer data at intervals."""
        while not self.stop_thread:
            accel_data = self.sensors.readAccelerometer()
            print(f"Accelerometer Data: {accel_data}")
            self.mqtt.sendData(accel_data, "accelerometer")
            time.sleep(3)  # Adjust the interval as needed

    def send_environment_sensor_data(self):
        """Send environment sensor data at intervals."""
        while not self.stop_thread:
            env_data = self.sensors.readEnvironmentSensor()
            print(f"Environment Sensor Data: {env_data}")
            self.mqtt.sendData(env_data, "environmentSensor")
            time.sleep(5)  # Adjust the interval as needed

    def send_distance_sensor_data(self):
        """Send distance sensor data at intervals."""
        while not self.stop_thread:
            dist_data = self.sensors.readDistanceSensor()
            print(f"Distance Sensor Data: {dist_data}")
            self.mqtt.sendData(dist_data, "distanceSensor")
            time.sleep(4)  # Adjust the interval as needed

    def ultrasonic_interrupt(self):
        """Monitor ultrasonic sensor and trigger interrupt if too close."""
        while not self.stop_thread:
            distance = self.sensors.readDistanceSensor()
            print(f"Ultrasonic Distance: {distance} cm")
            
            if distance < 10:  # Threshold for interruption
                print("Object detected too close! Stopping motors and backing up.")
                self.motors.stop()
                time.sleep(1)
                self.motors.backward()
                time.sleep(2)  # Back up for 2 seconds
                self.motors.stop()
                time.sleep(1)  # Wait for a bit before resuming
            time.sleep(0.5)  # Check the distance every 0.5 seconds

    def run(self):
        """Run the Raspcar logic."""
        try:
            while not self.stop_thread:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Stopping Raspcar...")
            self.stop_thread = True
            self.mqtt.client.disconnect()
            self.mqtt.client.loop_stop()
            print("Raspcar stopped.")

# Main entry point
if __name__ == "__main__":
    args = parse_args()

    # Initialize Raspcar with parsed arguments
    raspcar = Raspcar(
        baseUrl=args.baseUrl,
        mqtt_broker=args.mqttBroker,
        mqtt_port=args.mqttPort,
        base_topic=args.baseTopic
    )

    # Start Raspcar
    raspcar.run()
