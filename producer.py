#!/usr/bin/env python3
# https://redis-py.readthedocs.io/en/latest/

import redis
import random
import time
import os

host = os.environ.get('host', 'redis')
print(f"Using host {host}")

r = redis.Redis(host=host, port=6379, db=0)

words = ['space', 'tesla', 'cat', 'pi', 'minecraft', 'quake', 'mac', 'redis']
print("Producer starting...")

while(True):
    try:
        word = random.choice(words)
        res = r.rpush('queue', word)

        print(f"added {word} to queue: {res}")

        t = random.randint(0, 5)
        time.sleep(t)
    except redis.exceptions.ConnectionError:
        print("Could not connect to Redis, retrying...")
        time.sleep(1)
