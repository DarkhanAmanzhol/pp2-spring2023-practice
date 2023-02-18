# This task is about to use python generators, modules, datetime
# Let's create 2 .py files: 

import random
from datetime import datetime

random_words = ['liam', 'snake', 'pool', 'ggg', 'hurray', 'yo', 'rock', 'football', 'basket', 'ice_cream', 'bing', 'chilling']
surnames = ['smith', 'black', 'white', 'johnson', 'williams', 'jones', 'millers', 'wilson', 'anderson', 'holmes', 'moore']

def fake_user_generator():
    i = -1
    while True:
        # The generator has a limit of up to 100 data
        i+=1
        if i == 100:
            break

        # Main code
        username = random.choice(random_words) + str(random.randint(0, 1000)) + random.choice(surnames) 
        data = {
            "username": username,
            "age": random.randint(0, 100),
            "gender": random.choice(['female', 'male']),
            "created_at": str(datetime.now().strftime("%x"))
        }

        yield data