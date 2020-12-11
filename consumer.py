#!/usr/bin/env python3

import redis
import time
import random
import os

host = os.environ.get('host', 'redis')
print(f"Using host {host}")

r = redis.Redis(host=host, port=6379, db=0)

print("Consumer is starting ...")

random.seed()

while(True):
    try:
        word = r.lpop('queue')
        print(f"got {word} from queue")

        if (random.random() > 0.95):
            pass
            print("*** CRASHED ***")
            quit()
        
        time.sleep(10)
    except redis.exceptions.ConnectionError:
        print("Could not connect to Redis, retrying...")
        time.sleep(1)
    


