import threading
import json
import paho.mqtt.client as mqtt
from .database import get_db
from . import schemas
from . import crud
from .routers.config import configuration 

# MQTT configuration
MQTT_BROKER = "your_mqtt_broker_address" 
MQTT_PORT = 1883
baseTopic = "your/base/topic"

# Define the topics for each sensor
SENSOR_TOPICS = {
    "lightSensor": f"{baseTopic}/photoresistor",
    "accelerometer": f"{baseTopic}/accelerometer",
    "environmentSensor": f"{baseTopic}/pressure",
    "distanceSensor": f"{baseTopic}/distance"
}

# MQTT on_message callback
def on_message(client, userdata, message):
    payload = message.payload.decode()
    print(f"Received MQTT message: {payload} on topic: {message.topic}")

    # Parse payload as JSON string to dict
    try:
        data = json.loads(payload)
    except json.JSONDecodeError as e:
        print("Error parsing MQTT message:", e)
        return

    # Create a new database session
    db = next(get_db())

    # Route the message to the appropriate CRUD function based on topic
    if message.topic == SENSOR_TOPICS["lightSensor"]:
        # Create an instance of PhotoresistorCreate from data
        photoresistor_data = schemas.PhotoresistorCreate(**data)
        crud.create_photoresistor(db, photoresistor_data)
    elif message.topic == SENSOR_TOPICS["accelerometer"]:
        # Assuming you have a schema for Accelerometer
        accelerometer_data = schemas.AccelerometerCreate(**data)
        crud.create_accelerometer(db, accelerometer_data)
    elif message.topic == SENSOR_TOPICS["environmentSensor"]:
        # Assuming you have a schema for Pressure
        pressure_data = schemas.PressureCreate(**data)
        crud.create_pressure(db, pressure_data)
    elif message.topic == SENSOR_TOPICS["distanceSensor"]:
        # Assuming you have a schema for Distance
        distance_data = schemas.DistanceCreate(**data)
        crud.create_distance(db, distance_data)
    else:
        print("Unknown topic:", message.topic)

    # Close the database session
    db.close()

# MQTT subscriber setup
def start_mqtt():
    client = mqtt.Client()
    client.on_message = on_message

    # Connect to the broker
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    # Subscribe to each sensor topic
    for topic in SENSOR_TOPICS.values():
        client.subscribe(topic)

    # Start the MQTT client loop
    client.loop_forever()

# Run MQTT in a background thread
def start_mqtt_in_background():
    mqtt_thread = threading.Thread(target=start_mqtt)
    mqtt_thread.daemon = True
    mqtt_thread.start()

@app.on_event("startup")
def startup_event():
    print("Starting MQTT subscriber...")
    start_mqtt_in_background()
