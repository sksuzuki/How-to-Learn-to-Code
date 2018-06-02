import random
import sys

BOARD = 20


class Food:

    def __init__(self):
        self.x = ...
        self.y = ...
        self.mass = ...

    def degrade(self):
        ...


class Virus:

    def __init__(self, x=..., y=...):
        self.x = ...
        self.y = ...
        self.mass = ...

    def defense(self):
        return ...

    def move(self):
        ...

    def check_eating(self, ...):
        ...
        return ...

    def check_dividing(self):
        ...
        return ...

class Macrophage:

    def __init__(self):
        self.x = ...
        self.y = ...
        self.history = ...
        self.attack = ...

    def try_kill(self, ...):
        ...
        return ...

    def check_killing(self, ...):
        ...
        return ...

    def move_straight(self, ...):
        ...
        return ...

    def move_random(self, ...):
        ...
        return ...

    def move_and_kill(self, ...):
        ...
        return ...


class Simulation:

    def __init__(self, ..., ..., ...):
        self.food_ls = ...
        self.virus_ls = ...
        self.mac_ls = ...

    def update_viruses(self):
        ...

    def update_macs(self):
        ...

    def update_food(self):
        ...

    def run(self):
        ...

        return ..., ...


if __name__ == '__main__':
    ...
    results = f'({mean100}, {mean200})'
    print(results)
    with open('results/6.txt', 'w') as outfile:
        outfile.write(results)