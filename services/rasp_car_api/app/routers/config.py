# Implementation of route to send API
# main/routers/pressure.py
import os 
from fastapi import APIRouter, Depends, HTTPException
from app import schemas

router = APIRouter()

# Edit Dict to modify configs
configuration = {
    # motor : {},
    # sensor : {},
    "mqtt": {
        "broker": os.getenv("MQTT_BROKER", "broker.hivemq.com"),
        "port" :  os.getenv("MQTT_PORT", 1883),
        "topic": os.getenv("MQTT_TOPIC", "defTopic"),
    },
    "sql": os.getenv("SQL_URL", "mysql+pymysql://root:toor123@10.48.229.221:3306/Sensors"),
    
}

@router.get("/config/", response_model=schemas.RaspConfig)
def read_distances():
    return configuration
