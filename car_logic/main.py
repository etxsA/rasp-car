import time
import threading
import argparse
import paho.mqtt.client as mqtt
from . import setupControllers

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

        # Connect to MQTT broker
        self.connectMQTT()

    def fetch_config(self):
        """Fetch the configuration from the API."""
        try:
            # Fetch configuration from /config endpoint
            config = self.api.getData("config")
            
            # Extract MQTT config if available
            mqtt_config = config.get("mqtt", {})
            self.mqtt_broker = mqtt_config.get("broker", "localhost")
            self.mqtt_port = mqtt_config.get("port", 1883)
            self.mqtt_topic = mqtt_config.get("topic", "raspcar")
            
            print(f"Config fetched from API: {config}")
        except Exception as e:
            print(f"Error fetching config from API: {e}")
            # Use defaults if config fetch fails
            self.mqtt_broker = "localhost"
            self.mqtt_port = 1883
            self.mqtt_topic = "raspcar"

    def connectMQTT(self):
        """Set up MQTT connection and subscription."""
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect(self.mqtt_broker, self.mqtt_port)
        self.mqtt_client.loop_start()

        # Subscribe to motor control topic
        self.mqtt_client.subscribe(f"{self.base_topic}/motorControl")

    def on_connect(self, client, userdata, flags, rc):
        """Handle MQTT connection."""
        print(f"Connected to MQTT Broker with result code {rc}")
        self.mqtt_client.subscribe(f"{self.base_topic}/motorControl")

    def on_message(self, client, userdata, msg):
        """Handle incoming MQTT messages."""
        message = msg.payload.decode()
        print(f"Received message: {message}")
        
        if message == "FORWARD":
            self.motors.foward()
        elif message == "BACKWARD":
            self.motors.backward()
        elif message == "STOP":
            self.motors.stop()
        else:
            print(f"Unknown message: {message}")

    def send_sensor_data(self):
        """Send sensor data concurrently at different time intervals."""
        def send_light_data():
            while not self.stop_thread:
                light_data = self.sensors.readLightSensor()
                print(f"Light Sensor Data: {light_data}")
                self.mqtt.sendData(light_data, "lightSensor")
                time.sleep(2)  # Send light sensor data every 2 seconds

        def send_accel_data():
            while not self.stop_thread:
                accel_data = self.sensors.readAccelerometer()
                print(f"Accelerometer Data: {accel_data}")
                self.mqtt.sendData(accel_data, "accelerometer")
                time.sleep(3)  # Send accelerometer data every 3 seconds

        def send_env_data():
            while not self.stop_thread:
                env_data = self.sensors.readEnvironmentSensor()
                print(f"Environment Sensor Data: {env_data}")
                self.mqtt.sendData(env_data, "environmentSensor")
                time.sleep(5)  # Send environment sensor data every 5 seconds

        def send_distance_data():
            while not self.stop_thread:
                dist_data = self.sensors.readDistanceSensor()
                print(f"Distance Sensor Data: {dist_data}")
                self.mqtt.sendData(dist_data, "distanceSensor")
                time.sleep(1)  # Send distance sensor data every 1 second

        # Start the threads for each sensor data
        threading.Thread(target=send_light_data, daemon=True).start()
        threading.Thread(target=send_accel_data, daemon=True).start()
        threading.Thread(target=send_env_data, daemon=True).start()
        threading.Thread(target=send_distance_data, daemon=True).start()

    def handle_ultrasonic_interrupt(self):
        """Check the ultrasonic sensor and stop the motors if an obstacle is too close."""
        while not self.stop_thread:
            distance = self.ultrasonic.readData()
            print(f"Distance from obstacle: {distance} cm")
            if distance < 10:  # If object is closer than 10 cm
                print("Object too close, stopping motors and backing up.")
                self.motors.stop()
                self.motors.backward()
                time.sleep(2)  # Back up for 2 seconds
                self.motors.stop()
            time.sleep(0.1)  # Check every 100ms

    def run(self):
        """Start the program's main loop."""
        try:
            # Start the ultrasonic interrupt handling in a separate thread
            threading.Thread(target=self.handle_ultrasonic_interrupt, daemon=True).start()

            # Start sending sensor data concurrently
            self.send_sensor_data()

            # Keep the program running
            while True:
                time.sleep(1)

        except KeyboardInterrupt:
            print("Shutting down...")
            self.stop_thread = True
            self.mqtt_client.loop_stop()
            self.mqtt_client.disconnect()

if __name__ == "__main__":
    args = parse_args()
    raspcar = Raspcar(baseUrl=args.baseUrl, mqtt_broker=args.mqttBroker, mqtt_port=args.mqttPort, base_topic=args.baseTopic)
    raspcar.run()
