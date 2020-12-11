#!/bin/bash

docker build -t rubyan/producer:1.2 -f Dockerfile.producer .
docker build -t rubyan/consumer:1.2 -f Dockerfile.consumer .
