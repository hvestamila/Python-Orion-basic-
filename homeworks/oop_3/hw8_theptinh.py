from __future__ import annotations

import time
from typing import Dict, Any
from abc import ABC, abstractmethod
from random import choice, randint
import uuid


class Animal(ABC):

    def __init__(self, name: str, power: int, speed: int):
        self.id = uuid.uuid4()
        self.max_power = power
        self.current_power = power
        self.speed = speed
        self.name = name

    @abstractmethod
    def eat(self, forest: Forest):
        raise NotImplementedError


class Predator(Animal):
    animals = ['Fox', 'Wolf', 'Eagle']

    def eat(self, forest: Forest):
        if self.current_power <= 0:
            forest.remove_animal(self.id)

        chosen_animal = choice(list(forest.animals.values()))
        if chosen_animal.id == self.id:
            return f'{self.name} left without a dinner'
        else:
            if self.speed > chosen_animal.speed and self.current_power > chosen_animal.current_power:
                power_result = self.current_power + self.current_power * 0.5
                if power_result > self.max_power:
                    self.current_power = self.max_power
                else:
                    self.current_power = power_result
                print(f'{self.name} ate')
            else:
                self.current_power = self.current_power - self.max_power * 0.3
                chosen_animal.current_power = chosen_animal.current_power - chosen_animal.max_power * 0.3


class Herbivorous(Animal):
    animals = ['Cow', 'Giraffe', 'Rabbit']

    def eat(self, forest: Forest):
        if self.current_power <= 0:
            forest.remove_animal(self.id)
        else:
            power_result = self.current_power + self.current_power * 0.5
            if power_result > self.max_power:
                self.current_power = self.max_power
            else:
                self.current_power = power_result
            print(f'{self.name} ate')


AnyAnimal: Any[Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        self.animals[animal.id] = animal

    def remove_animal(self, animal_id):
        print(f'--------------\n Removing {self.animals[animal_id].name} \n--------------')
        del self.animals[animal_id]

    def any_predator_left(self):
        return any(isinstance(self.animals[key], Predator) for key in self.animals)


def animal_generator(n, animal_class):
    while n > 0:
        yield animal_class(choice(animal_class.animals), randint(25, 100), randint(25, 100))
        n -= 1


if __name__ == "__main__":

    animals = [next(animal_generator(5, choice([Predator, Herbivorous]))) for i in range(5)]

    my_forest = Forest()
    for animal in [next(animal_generator(5, choice([Predator, Herbivorous]))) for i in range(5)]:
        my_forest.add_animal(animal)

    while True:
        if not my_forest.any_predator_left():
            break
        for key in list(my_forest.animals):
            my_forest.animals[key].eat(my_forest)
        time.sleep(1)
