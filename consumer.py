#!/usr/bin/env python3

import redis
import time
import random
r = redis.Redis(host='redis', port=6379, db=0)
random.seed()

while(True):
    try:
        word = r.lpop('queue')
        print(f"got {word} from queue")

        if (random.random() > 0.9):
            pass
            # print("*** CRASHED ***")
            # quit()
        
        time.sleep(10)
    except redis.exceptions.ConnectionError:
        print("Could not connect to Redis, retrying...")
        time.sleep(1)
    


