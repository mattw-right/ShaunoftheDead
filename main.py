

from random import randint, random


class Zombie:
    """"""

    def __init__(self, speed, infection_rate):
        """Constructor for Zombie"""
        self.speed = speed
        self.x = randint(0, 200)
        self.y = randint(0, 200)
        if random() < infection_rate:
            self.infected = True
        else:
            self.infected = False

    def touching(self, zombie):
        if self.x == zombie.x and self.y == zombie.y:
            return True

    def move(self):
        self.x = self.x + self.speed
        self.y = self.y + self.speed

    def infect(self):
        if not self.infected:
            self.infected = True

    @property
    def is_infected(self):
        return self.infected


class World():
    """"""

    def __init__(self):
        self.objectList = []

    def populate_world(self, population, initial_infection_rate):
        for person in range(population):
            self.objectList.append(Zombie(2, initial_infection_rate))

    def update_world(self):
        for person in self.objectList:
            person.move()
            for other_zombie in self.objectList:
                if person.is_infected and person.touching(other_zombie):
                    person.infect()


    def get_number_infected(self):
        return "None"


    def get_number_well(self):
        return "None"


if __name__ == '__main__':
    moves = 10000
    my_world = World()
    my_world.populate_world(500, 0.4)
    for i in range(moves):
        my_world.update_world()
        print("Number infected:\t", my_world.get_number_infected())
        print("Number well:\t", my_world.get_number_well())
