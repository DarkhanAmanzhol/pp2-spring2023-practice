#  Generator task
from generators import fake_user_generator

class User:
    def __init__(self, username, age, gender, created_at):
        self.username = username
        self.age = age
        self.gender = gender
        self.created_at = created_at
    
    def age_group(self):
        if self.age <= 12:
            return 'Child'
        elif self.age <= 17:
            return 'Adolescent'
        elif self.age <= 65:
            return 'Adult'
        else:
            return 'Old adult'


user_generator = fake_user_generator()

# Printing area
for _ in range(10):
    # Calls next yield value from the function
    new_user = next(user_generator)

    print('User:', new_user)
    user = User(new_user['username'], new_user['age'], new_user['gender'], new_user['created_at'])
    print(f'{user.username} age group is', user.age_group(), "\n")