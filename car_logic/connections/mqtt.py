import paho.mqtt.client as mqtt
import json

class MqttController: 

    """ Wrapper class for the mqtt client to ensure
        it only works with the sensors and the data of the
        current context. 
    """

    def __init__(self, broker: str, port: int, baseTopic: str, on_message_fun) -> None:
        """Construct a simple mqqt client to publish messages to a broker

        Args:
            broker (str): url of the broker
            port (int): port of the broker
            baseTopic (str): The base topic from which topics for each sensor will be constructed
        """

        self.baseTopic = baseTopic
        # Construct Topics dict
        self.topics = {
            "lightSensor": f"{baseTopic}/photoresistor",
            "accelerometer": f"{baseTopic}/accelerometer",
            "environmentSensor": f"{baseTopic}/pressure",
            "distanceSensor": f"{baseTopic}/distance"
        }
        # Setup MQTT client
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.on_message_fun = on_message_fun
        self.client.on_message = self.on_message_fun
        self.client.connect(broker, port, 100)
        self.client.subscribe(f"equipo3/control")
        print(f"Subscribed to MQTT topic: {self.baseTopic}/control")
        on_message_fun("Test, PAYLOAD INSERTION")
        self.client.loop_start()  # Start the loop to process network traffic
    
    def sendData(self, data: str, sensor: str):
        """Publish data of a specific sensor to the broker

        Args:
            data (str): Data to publish 
            topic (str): Specific sensor

        Returns:
            _type_: Result of the publish
        """

        # Check if sensor is valid 
        if sensor not in self.topics.keys():
            print(f"Tried to send data to an unvalid sensor: {sensor}")
            return {"error": "Sensor non existant"}
        
        # Try publishing
        result = self.client.publish(self.topics[sensor], payload=str(data)) # Before Publishing it serialize it to a json format

        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            print(f"Data sent to MQTT topic {self.topics[sensor]} successfully.")
            return result
        else:
            print(f"Failed to send data to MQTT topic {self.topics[sensor]}")
            return result
        
    def on_message(self, client, userdata, msg):
            payload = msg.payload.decode("utf-8")
            print(f"Received message: {payload}")

            self.on_message_fun(payload)

    def __del__(self):
        """Stop mqtt instance and disconnect
        """
        self.client.loop_stop() 
        self.client.disconnect()  # Disconnect the MQTT client
