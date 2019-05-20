#!/usr/bin/env python3

import redis
import time

r = redis.Redis(host='redis', port=6379, db=0)
print("Observer starting...")

while(True):
    
    try:
        length = r.llen('queue')
        print(f"The queue contains {length} items")
        time.sleep(1)
    except redis.exceptions.ConnectionError:
        print("Could not connect to Redis, retrying...")
        time.sleep(1)

    


