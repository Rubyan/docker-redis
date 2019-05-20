# docker-redis
A message queue microservice with Redis and Python

## redis
The redis message queue that clients can connect to. Data is persisted in ./data

## producer
a python producer that writes to the queue

## consumer
a python consumer that reads from the queue

## observer
a python observer that counts the number of items in the list

# Building and testing
```
docker-compose up -d --build && docker-compose logs -f
docker-compose down
```
# Running as stack and increasing workers
```
./deploy
docker service scale redis-consumer=10

docker service ls

docker service logs -f redis_producer

docker ps

docker stack rm redis
```
