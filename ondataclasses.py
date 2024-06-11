from dataclasses import dataclass
import datetime

def computeBorn(age):
    current_year = datetime.datetime.now().year
    return current_year - age

@dataclass()
class Person:
    name: str
    city: str
    born: int = 0

    def __post_init__(self):
        self.born = computeBorn(self.born)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self.born = computeBorn(value)
        self._age = value

me = Person("John", "New York", 30)
print(me)
print(me.name)
sosia = Person("John", "New York", 30)
print(me == sosia)

me.age = 37
print(me)