
from functools import partial
import random
from typing import Callable

type NameGetter = Callable[[], str]

def _greet(get_name: NameGetter, greeting="Hello"):
    return f"{greeting} {get_name()}"

def get_weather():
    return random.choice(["Sunny", "Rainy", "Cloudy", "Windy"])
greet_weather: Callable[[], str] = partial(_greet, get_name=get_weather, greeting="Good Morning, today it's")

if __name__ == "__main__":
    def get_name():
        return "John"

    print(_greet(get_name))
    
    print(greet_weather())