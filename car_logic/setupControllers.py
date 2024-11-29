from typing import Tuple 
from .sensors import SensorController
from .motors.movements import MovementController
from .connections import MqttController, APIController, DBController


def setupControllers(baseUrl: str, 
                    mqttBroker: str=None, mqttPort: str=None, mqttTopic: str=None, dbURL: str = None) -> \
                Tuple[MovementController, SensorController, APIController, MqttController, DBController]:
    """Function to setup all controllers, to provide a configuration modify the thing the api returns
    when getting /config, the data of this endpoint is used to manage the configuration of the controllers
    baseUrl is mandatory any other Args are treated as optional

    Args:
        baseUrl (str): Url of the api
        mqttBroker (str, optional): Url of the mqtt broker. Defaults to None.
        mqttPort (str, optional): Port of the mqtt broker. Defaults to None.
        mqttTopic (str, optional): Topic for mqtt publish. Defaults to None.
        dbURL   (str, optional): dbURL to connect to. 

    Raises:
        ConnectionError: When the provided info by API is no enough

    Returns:
        List[MovementController, SensorController, APIController, MqttController]: List of Instances of each controller. 
    """
    apiC = APIController(baseUrl)
    
    config: dict = apiC.getData("config")
    


    motor = MovementController()
    sensors = SensorController()
    def printer(payload):
            print("mqtt: " + payload)

    # Check if the arguments where provided
    if not mqttBroker or not mqttPort or not mqttTopic:
        print(f"Using mqtt config provided by API <- No mqtt config provied in cli")
        mqttConfig = config.get("mqtt", {})
        mqttBroker = mqttConfig.get("broker")
        mqttPort = mqttConfig.get("port")
        mqttTopic = mqttConfig.get("topic")

        # Never Trust API, if not provided fail
        if mqttBroker and mqttPort and mqttTopic:
            mqttC = MqttController(mqttBroker, mqttPort, mqttTopic, printer)
        else: 
            raise ConnectionError("Error fetching config from API, may be broken")
    else: 
        mqttC = MqttController(mqttBroker, mqttPort, mqttTopic, printer)

    # URL Direct Conection
    if not dbURL:
        print(f"Using dbURL provided by API <- No DB config URL provided")
        dbURL = config.get("sql", "")
        if dbURL != "":
            dbC = DBController(dbURL)
        else:
            raise ConnectionError("Error fetching config from API, may be broken for dB")
    else:
        dbC = DBController(dbURL)



    return [motor, sensors, apiC, mqttC, dbC]
