import re
from data import restaurants, ids

def get_restaurants(restaurants):
    prev = 0
    counter = 0
    rests = {}
    obj = {}
    for k, v in restaurants.items():
        # get index of restaurant
        i = int(re.findall("\d+", k)[0])
        # if we got next restaurant data
        if i != prev:
            # save current restaurant's data
            rests[counter] = dict(zip(obj.keys(), obj.values()))
            # or
            # rest_dict = {}
            # for k, v in obj.items():
            #     rest_dict[k] = v
            # rests[counter] = rest_dict
            obj.clear()
            prev = i
            counter += 1
        obj_key = re.sub("\d+\_", "", k)
        if obj_key in ids:
            obj[obj_key] = v
    rests[counter] = dict(zip(obj.keys(), obj.values()))

    return rests


rests = get_restaurants(restaurants)

for i in range(len(rests)):
    print(f'Restaurant #{i+1}')
    for k, v in rests[i].items():
        print(f'{k}: {v}')