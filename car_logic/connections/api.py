import requests
from typing import Dict, Any

class APIController:
    """
    APIController manages interactions with various sensor endpoints via HTTP requests.
    
    Attributes:
        endpoints (dict): A dictionary mapping sensor names to their respective API URLs.
    """

    def __init__(self, baseUrl: str) -> None:
        """
        Initializes the APIController with the base URL and constructs API endpoints.

        Args:
            baseUrl (str): The base URL for the API.
        """
        self.endpoints = {
            "lightSensor": f"http://{baseUrl}/photoresistor",
            "accelerometer": f"http://{baseUrl}/accelerometer",
            "environmentSensor": f"http://{baseUrl}/pressure",
            "distanceSensor": f"http://{baseUrl}/distance",
            "config": f"http://{baseUrl}/config"
        }
    
    def sendData(self, data: dict, sensor: str) -> requests.Response:
        """
        Sends data to a specified sensor endpoint using a POST request.

        Args:
            data (dict): The data to send in JSON format.
            sensor (str): The sensor endpoint to which data should be sent.

        Returns:
            requests.Response: The response object from the POST request.

        Raises:
            requests.exceptions.RequestException: If the sensor is invalid or an error occurs during the request.
        """
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
            print(f"Error sending data to endpoint for {sensor}: {e}")

    def getData(self, sensor: str) -> Dict[str, Any]:
        """
        Retrieves data from a specified sensor endpoint using a GET request.

        Args:
            sensor (str): The sensor endpoint from which data should be retrieved.

        Returns:
            Dict[str, Any]: The JSON data retrieved from the API or an error message.

        Raises:
            requests.exceptions.RequestException: If the sensor is invalid or an error occurs during the request.
        """
        try:
            if sensor not in self.endpoints:
                raise requests.exceptions.RequestException(f"Not a valid sensor, check documentation. sensor: {sensor}")

            response = requests.get(self.endpoints[sensor])
            if response.status_code == 200:
                print(f"Data retrieved from {self.endpoints[sensor]} successfully.")
                return response.json()
            else:
                print(f"Failed to retrieve data from {self.endpoints[sensor]}. Status code: {response.status_code}")
                return {"error": f"Failed to retrieve data, status code: {response.status_code}"}
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving data from {self.endpoints[sensor]}: {e}")
            return {"error": str(e)}
