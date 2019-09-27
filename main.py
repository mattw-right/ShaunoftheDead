

from random import randint, random
import matplotlib.pyplot as plt

class Zombie:
    """"""

    def __init__(self, speed, infection_rate, closeness):
        """Constructor for Zombie"""
        self.speed = speed
        self.x = randint(0, 200)
        self.y = randint(0, 200)
        self.closeness = closeness
        if random() < infection_rate:
            self.infected = True
        else:
            self.infected = False

    def touching(self, zombie):
        if ((self.x - zombie.x)**2 + (self.y - zombie.y)**2)**0.5 <= self.closeness:
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

    def populate_world(self, population, initial_infection_rate, closeness):
        for person in range(population):
            self.objectList.append(Zombie(2, initial_infection_rate, closeness))

    def update_world(self):
        for person in self.objectList:
            person.move()
            for other_zombie in self.objectList:
                if person.is_infected == False and person.touching(other_zombie):
                    person.infect()


    def get_number_infected(self):
        count = 0
        for person in self.objectList:
            if person.is_infected:
                count += 1
        return count


    def get_number_well(self):
        count = 0
        for person in self.objectList:
            if person.is_infected == False:
                count += 1
        return count


if __name__ == '__main__':
    moves = 1
    population = 500
    my_world = World()
    my_world.populate_world(population, 0.4, 10)
    for i in range(moves):
        my_world.update_world()
        print("Number infected:\t", my_world.get_number_infected())
        print("Number well:\t", my_world.get_number_well())
        plt.bar(['Infected', 'Not'], [int(my_world.get_number_infected()), int(my_world.get_number_well())])
        plt.show()
