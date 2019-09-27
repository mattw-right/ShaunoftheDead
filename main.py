

from random import randint, random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

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
        else:
            return False

    def move(self):
        if self.x > 200 or self.y > 200 or self.x < 0 or self.y < 0:
            self.speed = -1*self.speed
        self.x = self.x + self.speed
        self.y = self.y + self.speed
        self.speed = 2*random()-2

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
                if person.is_infected and person.touching(other_zombie):
                    other_zombie.infect()

    def create_coord_list(self):
        infected = np.zeros(shape=(len(self.objectList), 2))
        healthy = np.zeros(shape=(len(self.objectList), 2))
        for i, j in enumerate(self.objectList):
            if j.is_infected:
                infected[i, 0] = j.x
                infected[i, 1] = j.y
            else:
                healthy[i, 0] = j.x
                healthy[i, 1] = j.y
        return infected, healthy

    def plot(self, infected, healthy):
        plt.scatter(infected[:, 0], infected[:, 1], facecolor='red')
        plt.scatter(healthy[:, 0], healthy[:, 1], facecolor='blue')
        plt.show()



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
    population = 100
    initial_infection_rate = 0.1
    closeness = 25
    my_world = World()
    my_world.populate_world(population, initial_infection_rate, closeness)
    infectedCount = []
    healthyCount = []
    count = 0
    while True:
        my_world.update_world()
        print("{}. Number infected: {}".format(count, my_world.get_number_infected()))
        print("{}. Number well: {}".format(count, my_world.get_number_well()))

        if count % 15 == 0:
            plt.bar(['Infected', 'Not'], [int(my_world.get_number_infected()), int(my_world.get_number_well())])
            infected, healthy = my_world.create_coord_list()
            my_world.plot(infected, healthy)


        infected, healthy = my_world.create_coord_list()
        my_world.plot(infected, healthy)

        infectedCount.append(my_world.get_number_infected())
        healthyCount.append(my_world.get_number_well())

        if my_world.get_number_well() == 0:
            break
        count+= 1

    input('Press enter to see graph over time... ')
    print(healthyCount)
    plt.plot(range(count+1), infectedCount)
    plt.show()
