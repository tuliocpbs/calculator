# Calculator

### Infrastructure

![Calculator Infrastructure Architecture](https://github.com/tuliocpbs/calculator/blob/master/images/calculator_infrastructure.png)

### Requirements to run this project

##### Docker - [Link for instrucitons](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

##### Docker Compose - [Link for instructions](https://docs.docker.com/compose/install/)

### How to Run

###### Execute the commands bellow in sequence:

`$ git clone https://github.com/tuliocpbs/calculator.git`

`$ cd calculator`

`$ docker-compose up -d`

### How to interact with the Application

###### Access `API Swagger Endpoint` : <http://localhost:5000/api/docs/>

### Monitoring with Elastic APM

> Wait for Kibana be up

###### Access `APM app on Kibana ` : <http://localhost:5601/app/apm>

### How to interact with RabbitMQ

###### Access `RabbitMQ Management Endpoint` : <http://localhost:15672>

| Credentials | Value|
|------------|-------|
|User |user |
|Password |password |

### How to interact with PostgreSQL

###### Access `Adminer Endpoint` : <http://localhost:8080>

| Credentials | Value|
|------------|-------|
|System |PostgreSQL |
|Password |postgres |
|User |user |
|Password |password |
|Database |calculator |
