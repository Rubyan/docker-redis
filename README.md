# docker-redis
A message queue microservice with Redis and Python

## redis
The redis message queue that clients can connect to. Data is persisted in ./data

## producer
a python producer that writes a random word from the list ['space', 'tesla', 'cat', 'pi', 'minecraft', 'quake', 'mac', 'redis']to the queue and sleeps for 0-5 seconds

## consumer
a python consumer that reads from the queue and sleeps for 10 seconds. There is a 0.05 change that the consumer crashes

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
