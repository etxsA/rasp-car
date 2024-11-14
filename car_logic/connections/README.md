# Rasp-Car

## General Description

Rasp-Car is a software project designed to control an automated vehicle using a Raspberry Pi. This project includes modules for API communication, database handling, data schema definitions, and MQTT communication, facilitating integration and extensibility.

## Project Structure

1. **`__init__.py`**  
   - **Description**: Required for Python to recognize the directory as a package. Allows for the initialization of global variables and configurations.

2. **`api.py`**  
   - **Description**: Manages communication with external APIs. Contains functions and classes for making HTTP requests and processing responses, ensuring smooth integration with external services.

3. **`db.py`**  
   - **Description**: Project's database handler. Defines functions to connect to and manipulate data within the database, covering CRUD operations (create, read, update, and delete).

4. **`schemas.py`**  
   - **Description**: Contains the data schemas used in the project. Defines the structure of data entities, ensuring validation and consistency of information exchanged between modules and APIs.

5. **`mqtt.py`**  
   - **Description**: Manages MQTT communication. Provides functions for publishing and subscribing to messages, facilitating real-time communication between the vehicle and other connected devices.

6. **`models.py`**  
   - **Description**: Defines the data models used in the project. These models represent the entities and relationships in the database, facilitating structured data manipulation.

## Installation and Execution

1. **Clone the repository:**
   ```bash
   git clone <repository-URL>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the project:**
   ```bash
   python main.py
   ```

## Requirements

- **Python 3.x**
- **Required modules** (listed in `requirements.txt`)

## Usage and Features

- **api.py**: Executes functions for communication with external services to gather data.
- **db.py**: Manages data storage and performs database operations.
- **schemas.py**: Validates data, ensuring integrity in data exchange.
- **mqtt.py**: Facilitates real-time communication via the MQTT protocol, enabling data transmission between devices.
- **models.py**: Defines data models and relationships, structuring data storage and manipulation.
