from random import random, randint

class Doctor:

    def __init__(self, speed, closeness, dimensions):
        """Constructor for Zombie"""
        self.speed = speed
        self.dimensions = dimensions
        self.x = randint(0, dimensions)
        self.y = randint(0, dimensions)
        self.closeness = closeness

    def touching(self, zombie):
        if ((self.x - zombie.x) ** 2 + (self.y - zombie.y) ** 2) ** 0.5 <= self.closeness:
            return True
        else:
            return False

    def move(self):
        if self.x > self.dimensions or self.y > self.dimensions or self.x < 0 or self.y < 0:
            self.speed = -1 * self.speed
        self.x = self.x + self.speed * (random() - 1)
        self.y = self.y + self.speed * (random() - 1) * (random() - 1)

    def infect(self):
        if not self.infected:
            self.infected = True
