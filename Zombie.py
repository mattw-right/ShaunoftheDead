from random import random, randint

class Zombie:
    """"""

    def __init__(self, speed, infection_rate, closeness, dimensions, length_of_immunity):
        """Constructor for Zombie"""
        self.speed = speed
        self.dimensions = dimensions
        self.length_of_immunity = length_of_immunity
        self.x = randint(0, self.dimensions)
        self.y = randint(0, self.dimensions)
        self.turn_healed = 0
        self.closeness = closeness
        if random() < infection_rate:
            self.infected = True
        else:
            self.infected = False

    def touching(self, zombie):
        if ((self.x - zombie.x)**2 + (self.y - zombie.y)**2)**0.5 <= self.closeness:
            return True
        else:
            return False

    def move(self):
        if self.x > self.dimensions or self.y > self.dimensions or self.x < 0 or self.y < 0:
            self.speed = -1*self.speed
        self.small_offset = -1*random()
        self.x = self.x + 2*(self.speed*(random()-1)+self.small_offset)
        self.y = self.y + 2*(self.speed*(random()-1)+self.small_offset)

    def infect(self, count):
        if not self.infected and count-self.turn_healed > self.length_of_immunity:
            self.infected = True

    @property
    def is_infected(self):
        return self.infected

    def heal(self, turn_healed):
        if self.infected:
            self.infected = False
            self.turn_healed = turn_healed
