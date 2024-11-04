# Database 
This a simple dockerfile, where you can build a docker image for testing in a docker container. 

## Schema
The database schema is present in the [database.sql](./database.sql), it's the file from which the database in the docker will be initialized.

If you want to replecate the database in another environment just use the CREATE TABLE statements provided. 

## How to build it and use it. 
> ![NOTE]
> This docker container, should only be used for testing and developing, never in production environments.


> ![TIP]
> Before bulding, modify it as you wish ensure credentials ared specified in the other services of the project. 

__Building__ \
To build the image ensure the configuration as you want it, specially the credentials, after that run: 
```bash
docker build -t mysql_raspcar_image .
```
__Running it__ \
Now that you have an image just run a contair from it: 
```bash
docker run -d -p 3306:3306 --name mysql_raspcar_container mysql_raspcar_image
```
> ![NOTE]
> -d: for runnint in detached mode
> -p: maps port 3306 from the container to localhost, so it can be accesed from outside.

## Managing the container and image

Here is a compilation of commands to manage the docker container and the image in your system. 

- _Connect to MySQL in the Container as root_
```bash
docker exec -it mysql_raspcar_container mysql -u root -p
```
- _View logs_
```bash
docker logs 
```
- _Stop the container_
```bash
docker stop mysql_raspcar_container
```
- _Start container if stopped_
```bash
docker start mysql_raspcar_container
```
- _Delete container_
```bash
docker rm -f mysql_raspcar_container
```
- _Delete image_
```bash
docker rmi mysql_raspcar_image
```
