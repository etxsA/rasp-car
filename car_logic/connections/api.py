import requests
from typing import Dict

class APIController:

    def __init__(self, baseUrl) -> None:
        # Construct each apiEndpoints based on Base Url
        self.endpoints = {
        "lightSensor": f"http://{baseUrl}/photoresistor",
        "accelerometer": f"http://{baseUrl}/accelerometer",
        "environmentSensor": f"http://{baseUrl}/pressure",
        "distanceSensor": f"http://{baseUrl}/distance",
        "config": f"http://{baseUrl}/config"
    }
    
    def sendData(self, data: dict, sensor: str) -> requests.Response:
        try:

            if sensor not in self.endpoints.keys():
                raise requests.exceptions.RequestException(f"Not a valid sensor, check documentation. sensor: {sensor}")

            response = requests.post(self.endpoints[sensor], json=data)
            if response.status_code == 200:
                print(f"Data sent to {self.endpoints[sensor]} successfully.")
                return response
            else:
                print(f"Failed to send data to {self.endpoints[sensor]}. Status code: {response.status_code}")
                return response
        except requests.exceptions.RequestException as e:
            print(f"Error sending data to {self.endpoints[sensor]}: {e}")


