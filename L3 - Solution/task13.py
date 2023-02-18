class WeatherCondition:
    def __init__(self, temperature):
        self.temperature = temperature

    def __str__(self):
        raise NotImplementedError("__str__ not implemented")

    def what_to_wear(self):
        raise NotImplementedError("what_to_wear not implemented")

class Sunny(WeatherCondition):
    def __str__(self):
        return "sunny"

    def what_to_wear(self):
        if self.temperature >= 15:
            return "Wear shorts and a t-shirt."
        return "Wear long pants and a sweater."

class Cloudy(WeatherCondition):
    def __str__(self):
        return "cloudy"

    def what_to_wear(self):
        if self.temperature >= 0:
            return "Wear a jacket."
        return "Wear a heavy coat."

class Rainy(WeatherCondition):
    def __str__(self):
        return "rainy"

    def what_to_wear(self):
        return "Wear a raincoat."

average_temp = lambda conditions: sum(c.temperature for c in conditions) / len(conditions)

average_temp_by_condition = lambda conditions, condition: average_temp(list(filter(lambda c: type(c) == condition, conditions)))

filter_conditions = lambda conditions, condition: list(filter(lambda c: type(c) == condition, conditions))

conditions = [    Sunny(20),    Cloudy(1),    Rainy(10),    Sunny(14),    Cloudy(-20),    Rainy(5),]

# Compute the average temperature of all conditions
avg_temp = average_temp(conditions)
print("Average temperature of all conditions:", avg_temp)

# Compute the average temperature of sunny conditions
avg_temp_sunny = average_temp_by_condition(conditions, Sunny)
print("Average temperature of sunny conditions:", avg_temp_sunny)

# Filter sunny conditions
sunny_conditions = filter_conditions(conditions, Sunny)
print("Sunny conditions:")
for c in sunny_conditions:
    print(c.what_to_wear())

