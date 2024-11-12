# Implementation of MQTT server to be runned when the api starts
# Concurrently insert to the database.
from contextlib import asynccontextmanager
from fastapi import FastAPI
import json
import paho.mqtt.client as mqtt

from app.database import get_db
from app import schemas
from app import crud
from app.routers import config

# MQTT configuration
MQTT = config.configuration.get("mqtt")
mqttBroker = MQTT.get("broker")
mqttPort = MQTT.get("port")
baseTopic = MQTT.get("topic")

# Define the topics for each sensor
sensorTopics = {
    "lightSensor": f"{baseTopic}/photoresistor",
    "accelerometer": f"{baseTopic}/accelerometer",
    "environmentSensor": f"{baseTopic}/pressure",
    "distanceSensor": f"{baseTopic}/distance",
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

    topic = message.topic
    # Route the message to the appropriate CRUD function based on topic
    if topic == sensorTopics["lightSensor"]:
        photoresistor_data = schemas.PhotoresistorCreate(**data)
        crud.create_photoresistor(db, photoresistor_data)
        print(f"MQTT:\t  OK Insertion {topic}")  

    elif topic == sensorTopics["accelerometer"]:
        accelerometer_data = schemas.AccelerometerCreate(**data)
        crud.create_accelerometer(db, accelerometer_data)
        print(f"MQTT:\t  OK Insertion {topic}")  

    elif topic == sensorTopics["environmentSensor"]:
        pressure_data = schemas.PressureCreate(**data)
        crud.create_pressure(db, pressure_data)
        print(f"MQTT:\t  OK Insertion {topic}")  

    elif topic == sensorTopics["distanceSensor"]:
        distance_data = schemas.DistanceCreate(**data)
        crud.create_distance(db, distance_data)
        print(f"MQTT:\t  OK Insertion {topic}")  

    else:
        print("Unknown topic:", topic)
    # Close the database session
    db.close()


# Lifespan context manager to start and stop MQTT
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start MQTT client
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(mqttBroker, mqttPort, 60)

    # Subscribe to sensor topics
    for topic in sensorTopics.values():
        client.subscribe(topic)

    # Start MQTT loop in a separate thread
    client.loop_start()
    print(f"MQTT:\t  MQTT client started listening in main topic: {baseTopic}")
    print(f"MQTT:\t  Using broker: {mqttBroker}:{mqttPort}")

    try:
        yield
    finally:
        # Stop MQTT client on shutdown
        client.loop_stop()
        client.disconnect()
        print(f"MQTT:\t  MQTT client stopped")
