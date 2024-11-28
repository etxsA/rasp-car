import paho.mqtt.client as mqtt
from .motors.movements import MovementController
import time

# Define the MQTT broker details
BROKER = "broker.hivemq.com"  # HiveMQ public broker
PORT = 1883                  # MQTT port
TOPIC = "equipo3/control"         # Replace with your topic

controller = MovementController()
# Callback function when a connection is established
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to HiveMQ broker")
        client.subscribe(TOPIC)  # Subscribe to the topic
    else:
        print(f"Failed to connect, return code {rc}")

# Callback function when a message is received
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic: {msg.topic}")

    choice = msg.payload.decode()

    if choice == "FORWARD":
        controller.foward()
    elif choice == "BACKWARD":
        controller.backwards()
    elif choice == "RIGHT":
        controller.right()
    elif choice == "LEFT":
        controller.left()
    elif choice == '5':
        controller.spinRight()
    elif choice == '6':
        controller.spinLeft()
    elif choice == "STOP":
        controller.stop()
    else:
        print("Invalid option. Please choose a number from 1 to 8.")
    # Pause briefly to allow user to see action output
    time.sleep(0.2)

# Create an MQTT client
client = mqtt.Client()

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(BROKER, PORT, 60)

# Loop forever to process network traffic and messages
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nDisconnected from broker")
    client.disconnect()
