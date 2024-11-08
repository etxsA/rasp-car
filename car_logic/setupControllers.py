from typing import Tuple 
from .sensors import SensorController
from .motors.movements import MovementController
from .connections import MqttController, APIController


def setupControllers(baseUrl: str, 
                    mqttBroker: str=None, mqttPort: str=None, mqttTopic: str=None) -> \
                Tuple[MovementController, SensorController, APIController, MqttController]:
    """Function to setup all controllers, to provide a configuration modify the thing the api returns
    when getting /config, the data of this endpoint is used to manage the configuration of the controllers
    baseUrl is mandatory any other Args are treated as optional

    Args:
        baseUrl (str): Url of the api
        mqttBroker (str, optional): Url of the mqtt broker. Defaults to None.
        mqttPort (str, optional): Port of the mqtt broker. Defaults to None.
        mqttTopic (str, optional): Topic for mqtt publish. Defaults to None.

    Raises:
        ConnectionError: When the provided info by API is no enough

    Returns:
        List[MovementController, SensorController, APIController, MqttController]: List of Instances of each controller. 
    """
    apiC = APIController(baseUrl)
    
    config: dict = apiC.getData("config")
    
    motor = MovementController()
    sensors = SensorController()

    # Check if the arguments where provided
    if not mqttBroker or not mqttPort or not mqttTopic:
        print(f"Using mqtt config provided by API <- No mqtt config provied in cli")
        mqttConfig = config.get("mqtt", {})
        mqttBroker = mqttConfig.get("broker")
        mqttPort = mqttConfig.get("port")
        mqttTopic = mqttConfig.get("topic")

        # Never Trust API, if not provided fail
        if mqttBroker and mqttPort and mqttTopic:
            mqttC = MqttController(mqttBroker, mqttPort, mqttTopic)
        else: 
            raise ConnectionError("Error fetching config from API, may be broken")
    else: 
        mqttC = MqttController(mqttBroker, mqttPort, mqttTopic)

    return [motor, sensors, apiC, mqttC]
