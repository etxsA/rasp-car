import time
import json
import requests
import paho.mqtt.client as mqtt
from datetime import datetime

# Dirección IP y puerto de la API
API_IP = "192.168.1.100"
BASE_URL = f"http://{API_IP}"

def post_data(endpoint, data):
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print(f"POST exitoso a {endpoint}: {response.json()}")
        else:
            print(f"Error en POST a {endpoint}: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")

def on_message(client, userdata, message):
    payload = json.loads(message.payload.decode())
    timestamp = datetime.utcnow().isoformat()
    
    if message.topic == "TestTECIoT/sensor1":
        # /photoresistor/ endpoint
        data = {
            "voltage": payload.get("voltage", 0),
            "lightLevel": payload.get("lightLevel", 0),
            "timestamp": timestamp
        }
        post_data("/photoresistor/", data)

    elif message.topic == "TestTECIoT/sensor2":
        # /accelerometer/ endpoint
        data = {
            "x": payload.get("x", 0),
            "y": payload.get("y", 0),
            "z": payload.get("z", 0),
            "events": payload.get("events", "none"),
            "timestamp": timestamp
        }
        post_data("/accelerometer/", data)

    elif message.topic == "TestTECIoT/adc":
        # /distance/ endpoint
        data = {
            "distance": payload.get("distance", 0),
            "timestamp": timestamp
        }
        post_data("/distance/", data)

    elif message.topic == "TestTECIoT/pressure":
        # /pressure/ endpoint
        data = {
            "temperature": payload.get("temperature", 0),
            "pressure": payload.get("pressure", 0),
            "altitude": payload.get("altitude", 0),
            "timestamp": timestamp
        }
        post_data("/pressure/", data)
    
    print(f"Mensaje recibido en el topic {message.topic}: {payload}")

# Establecer conexión
mqttc = mqtt.Client()
mqttc.on_message = on_message

# Conectar al broker
mqttc.connect("broker.hivemq.com", 1883)

# Suscribirse a los topics
mqttc.subscribe("TestTECIoT/1")
mqttc.subscribe("TestTECIoT/sensor1")
mqttc.subscribe("TestTECIoT/sensor2")
mqttc.subscribe("TestTECIoT/adc")
mqttc.subscribe("TestTECIoT/pressure")

# Iniciar el bucle para esperar y recibir mensajes
mqttc.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Desconectando...")

# Detener el bucle y desconectar
mqttc.loop_stop()
mqttc.disconnect()
