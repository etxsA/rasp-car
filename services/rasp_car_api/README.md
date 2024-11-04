# rasp_car_api
> [!NOTE]
> The API can run in any system

A simple fastapi implementation serving as bridge between our car and the database server. 

## Table of Contents

- [Code Requirements](#code-requirements)
- [Environment Variables](app/README.md#environment-variables)
- [Database Models](#database-models)
- [API Endpoints](#api-endpoints)
  - [Photoresistor Endpoints](#photoresistor-endpoints)
  - [Accelerometer Endpoints](#accelerometer-endpoints)
  - [Distance Endpoints](#distance-endpoints)
  - [Pressure Endpoints](#pressure-endpoints)

---

## Code Requirements 
To execute any of the code , ensure you are running on a python virtual environment (venv). If no, create one and use it from the termimal: 
```bash
python3 -m venv rasp_car_api
source rasp-car/bin/activate
```

If you need to get out of the venv, just use __deactivate__
```bash
deactivate
```

Ensuring you are in a venv, install the requirements using: 
```bash
pip3 install -r requirements.txt
```

## Running the API

To run the API simply use uvicorn as follows: 

```bash
uvicorn app.main:app --reload
```
