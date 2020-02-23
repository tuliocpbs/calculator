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

`$ docker-compose up -d rabbitmq postgres adminer elasticsearch kibana apm`

> Wait for all dependencies be up

`$ docker-compose up -d web consumer`

### How to interact with the Application

###### Access `API Swagger Endpoint` : <http://localhost:5000/docs>

> To user any requests insert the Api-Key value on Authorize field

| Credentials | Value|
|------------|-------|
|Api-Key |secret-api-key |

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

> Use this interface to visualize the final result on the database

| Credentials | Value|
|------------|-------|
|System |PostgreSQL |
|Password |postgres |
|User |user |
|Password |password |
|Database |calculator |
