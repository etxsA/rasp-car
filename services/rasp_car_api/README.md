# rasp_car_api
> [!NOTE]
> The API can run in any system

A simple fastapi implementation serving as bridge between our car and the database server. 
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

## Environment Variables
There is the use of environment varibles for the Database Server URL, in case it's not defined, default will be used. 
> [!TIP]
> Create an .env file, the variable should be named DATABASE_URL


## File Structure



