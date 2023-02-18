class Person:
    def __init__(self, name: str, age: int = 0) -> None:
        self.set_name(name=name)
        self.set_age(age=age)
        self._partner = None
        self._children = []
        self._status = 'Single'

    def procreate(cls, person1, person2):
        baby: Person = Person(f'Child of {person1.name} and {person2.name}')

        person1._children.append(baby)
        person2._children.append(baby)

        return baby

    def get_full_information(self):
        return f'Person {self.name} with age {self.age} and status {self.status} has partner {self.partner} and {self.children}'

    def get_children(self):
        if len(self._children):
            return f'{self.name} has {", ".join(map(str, self._children))} children'
        else:
            return '0 child'

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        if not isinstance(name, str):
            print('Name must be `str` type')
            return

        if name == '':
            print('Name cannot be empty')
            return

        self._name = name

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if not isinstance(age, int):
            print('Age must be `int` type')
            return

        if age < 0:
            print('Age cannot be less than zero')
            return

        self._age = age

    def get_partner(self):
        return self._partner

    def set_partner(self, person):
        self._partner = person

        if person != None:
            self.status = 'Married'
        else:
            self.status = 'Single'

    def set_status_with_partner(self, status, person):
        if self.partner and self.partner != person:
            self.status = 'Traitor'
        else:
            self.partner = person
            self.status = status

    def get_status(self):
        return self._status

    def set_status(self, status):
        if status in self.statuses:
            self._status = status

    def __str__(self) -> str:
        return f'Person {self._name}'

    def __repr__(self) -> str:
        return f'Person {self._name}'

    def __add__(self, person):
        if not self.partner and not person.partner:
            self.partner = person
            person.partner = self

            return

        self.set_status_with_partner('In love', person)
        person.set_status_with_partner('In love', self)

    def __mul__(self, person):
        return Person.procreate(self, person)

    def __sub__(self, person):
        if self.partner == person:
            self.partner = None

        if person.partner == self:
            person.partner = None

    def __del__(self):
        self.status = 'Dead'
        if self.partner:
            self.partner.partner = None

        del self

    age = property(get_age, set_age)
    name = property(get_name, set_name)
    children = property(get_children)
    partner = property(get_partner, set_partner)
    status = property(get_status, set_status)
    procreate = classmethod(procreate)
    statuses = ['Single', 'Married', 'In love', 'Traitor', 'Dead']