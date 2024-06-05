
from collections import namedtuple
import logging

Person = namedtuple("Person", ["name", "age", "age2"])

me = Person("Marcello", 37, 37)
print(me.name)
print(me.index('Marcello'))
print(me.index(37))
print("count Marcello: ", me.count('Marcello'))
print("count 37: ", me.count(37))

try:
    me.name = "Marcello"
except AttributeError as e:
    logging.exception(e)