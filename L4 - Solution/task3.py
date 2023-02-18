from datetime import datetime
# Sample users contain dictionaries in an array
from sample_inputs import users

def person_age(birthdate_obj):
    birthdate = datetime.strptime(birthdate_obj, '%Y-%m-%d')

    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def ab_groups(data, max_age):
    # filtered_data = (person for person in data if age(parse_datetime(person['birthdate'])) <= max_age)
    filtered_data = []
    for person in data:
        if person_age(person['birthdate']) <= max_age:
            filtered_data.append(person)



    sorted_data = sorted(filtered_data, key=lambda x: x['height'])
    group_a, group_b = [], []
    for i in range(len(sorted_data)):
        (group_a if i % 2 == 0 else group_b).append(sorted_data[i])
    return group_a, group_b


def average_height(data):
    # total_height = sum(person['height'] for person in data)
    total_height = 0
    for person in data:
        total_height += person['height']

    avg_height = total_height / len(data)
    return avg_height


max_age = 40
groups = ab_groups(users, max_age)

group_a, group_b = groups

a_av_h = average_height(group_a)
b_av_h = average_height(group_b)

print(len(group_a), len(group_b))
print(a_av_h, b_av_h)