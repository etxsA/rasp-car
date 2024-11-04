# Services
The project uses 2 main services a MySQL Database for storing the sensor data, in this case we include a docker definition, so it can be used for testing. 

The second service is the fastapi, an implementation in python that serves as a bridge between our car, the database, and our main aplication

## Folder Structure
- **`📂 services/`**: Container for all services
  -  [**`📂 rasp_car_api/`**:](/services//rasp_car_api/app)
  Implementation of a fastapi, using sqlalchemy to interact with the MySQL Database. Simple rest api. 
  - [**`📂 mysql/`**:](/services/mysql/)
      Database Scheme, and instructions to replicate it, also it's included a docker file to test it locally. 

