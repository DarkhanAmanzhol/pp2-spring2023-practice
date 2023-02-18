class Person:

    count_of_object = 0

    def __init__(self, name, family_name, age, occupation, nationality):
        self.name = name
        self.family_name = family_name
        self.age = age
        self.occupation = occupation
        self.nationality = nationality
        Person.count_of_object += 1

    def get_name(self):
        return ("{name} {family_name}".format(name = self.name, family_name = self.family_name))

    def get_nationality(self):
        return self.nationality

    def get_age(self):
        return self.age

    def get_occupation(self):
        return self.occupation

    def year_born(self, cur_year):
        return cur_year - self.age

    def get_gender(self, gender):
        self.gender = gender
        return gender