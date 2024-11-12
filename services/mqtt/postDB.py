import time
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Mensaje recibido en el topic {message.topic}: {message.payload.decode()}")

# Establecer conexión
mqttc = mqtt.Client()
mqttc.on_message = on_message  # Asignar la función de callback para recibir mensajes

# Definir broker y puerto de conexión
mqttc.connect("broker.hivemq.com", 1883)

# Suscribirse al topic para recibir mensajes
mqttc.subscribe("Sensores")

# Iniciar el bucle para esperar y recibir mensajes
mqttc.loop_start()

try:
    # Mantener el script en ejecución para recibir mensajes continuamente
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Desconectando...")

# Detener el bucle y desconectar
mqttc.loop_stop()
mqttc.disconnect()
