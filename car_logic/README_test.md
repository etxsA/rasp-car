# Sensor and Motor Controller with API and MQTT Integration

This Python script is designed to control various types of hardware (motors and sensors) and facilitate data communication with external systems using API, MQTT, and direct SQL database connections. It provides a menu-driven interface to interact with hardware and to send sensor data to various platforms.

## Features

The application includes the following functionalities:

1. **Main Menu**: 
   - Allows selection between motor control, sensor data reading, and data transmission using different protocols (API, MQTT, SQL).

2. **Motor Control**:
   - Provides options to control motor movements, including moving forward, backward, turning, and spinning in place.

3. **Sensor Control**:
   - Allows reading data from various sensors such as Light, Accelerometer, Environmental, and Distance sensors. 
   - Displays individual sensor data or reads all sensor data at once.

4. **Data Transmission via API**:
   - Sends sensor data to a specified API endpoint. Each sensor type (Light, Accelerometer, Environmental, Distance) has dedicated options to transmit data.
   - Supports bulk transmission of all sensor data to the API.

5. **Data Transmission via MQTT**:
   - Sends sensor data to an MQTT broker.
   - Allows sending data for individual sensors or all sensors at once to predefined MQTT topics.

6. **Direct Database Transmission**:
   - Sends sensor data directly to a database using SQL.
   - Provides individual transmission options for Light, Accelerometer, Environmental, and Distance data.

## Usage

### Running the Script

The script accepts the following command-line arguments:

- `baseUrl` (required): The base URL for the API server.
- `mqttBroker` (optional): The address of the MQTT broker.
- `mqttPort` (optional): The port of the MQTT broker.
- `mqttTopic` (optional): The base topic for MQTT.
- `dbURL` (optional): URL of the database for a direct SQL connection.

```bash
python main.py <baseUrl> <mqttBroker> <mqttPort> <mqttTopic> <dbURL>
