## Environment Variables
There is the use of environment varibles for the Database Server URL, in case it's not defined, default will be used. 
> [!TIP]
> Create an .env file, the variable should be named DATABASE_URL

## File Structure
- **`📂 app/`**: Folder containing the FastAPI application code.
  - **`📄 main.py`**: Entry point
  - **`📄 database.py`**: Database connection and setup using SQLAlchemy.
  - **`📄 models.py`**: SQLAlchemy models that define database tables.
  - **`📄 schemas.py`**: Pydantic schemas for validating request and response data.
  - **`📄 crud.py`**: CRUD controlleres definition


## CRUD Operations
There is a part, where all the available operations are defined, in accordance with the models create from the schemas. 

The operations where created as follows: 
- Create Functions (create_*): Accepts a Pydantic schema (schemas.*Create) to create a new record. Sets the timestamp to the current time if not provided.

- Read Functions (get_* and get_*s): Retrieve single records by id or multiple records with pagination (skip and limit).

- Delete Functions (delete_*): Deletes a record by id and commits the transaction.

There was no adition of update functions, because there is no need to update the entries of the database. 

## API Endpoints

... 

