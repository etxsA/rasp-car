# Services
The project uses 2 main services a MySQL Database for storing the sensor data, in this case we include a docker definition, so it can be used for testing. 

The second service is the fastapi, an implementation in python that serves as a bridge between our car, the database, and our main aplication

## Folder Structure
- **`📂 services/`**: Container for all services
  -  [**`📂 rasp_car_api/`**:](/services//rasp_car_api/app)
  Implementation of a fastapi, using sqlalchemy to interact with the MySQL Database. Simple rest api. 
  - [**`📂 mysql/`**:](/services/mysql/)
      Database Scheme, and instructions to replicate it, also it's included a docker file to test it locally.
  - [**`📂 rasp_car_api/`**:](/services/rasp_car_api/)
      Contains a simple FastAPI implementation that acts as a bridge between a car and a database server. It provides various API endpoints to interact with car data.
  - [**`📂 rasp_car_app/`**:](/services/rasp_car_app/)
      Typescript-based app which displays sensor readings in a visual way.

