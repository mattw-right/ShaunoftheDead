from Zombie import Zombie
from Doctor import Doctor
import numpy as np
import matplotlib.pyplot as plt

class World():
    """"""

    def __init__(self, population, initial_infection_rate, closeness, dimensions, speed, frequency, turns, no_doctors, length_of_immunity):
        self.objectList = []
        self.doctorsList = []
        self.population = population
        self.initial_infection_rate = initial_infection_rate
        self.length_of_immunity = length_of_immunity
        self.closeness = closeness
        self.dimensions = dimensions
        self.speed = speed
        self.frequency = frequency
        self.turns = turns
        self.no_doctors = no_doctors

    def populate_world(self, population, initial_infection_rate, closeness):
        for person in range(population):
            self.objectList.append(Zombie(self.speed, initial_infection_rate, closeness, self.dimensions, self.length_of_immunity))
        for doctor in range(self.no_doctors):
            self.doctorsList.append(Doctor(self.speed, closeness, self.dimensions))

    def update_world(self, turn):
        for person in self.objectList:
            person.move()
            for other_zombie in self.objectList:
                if person.is_infected and person.touching(other_zombie):
                    other_zombie.infect(turn)
        for doctor in self.doctorsList:
            doctor.move()
            for other_zombie in self.objectList:
                if doctor.touching(other_zombie):
                    other_zombie.heal(turn)


    def create_coord_list(self):
        infected = np.zeros(shape=(len(self.objectList), 2))
        healthy = np.zeros(shape=(len(self.objectList), 2))
        doctors = np.zeros(shape=(len(self.doctorsList), 2))
        for i, j in enumerate(self.objectList):
            if j.is_infected:
                infected[i, 0] = j.x
                infected[i, 1] = j.y
            else:
                healthy[i, 0] = j.x
                healthy[i, 1] = j.y
        for i, j in enumerate(self.doctorsList):
            doctors[i, 0] = j.x
            doctors[i, 1] = j.y




        return infected, healthy, doctors

    def plot(self, infected, healthy, doctors, no):
        plt.scatter(infected[:, 0], infected[:, 1], facecolor='red')
        plt.scatter(healthy[:, 0], healthy[:, 1], facecolor='blue')
        plt.scatter(doctors[:, 0], doctors[:, 1], facecolor='green')
        plt.axis('off')
        plt.savefig('snapshots/{}.png'.format(no))
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

    def train_doctor(self):
        self.doctorsList.append(Doctor(self.speed, self.closeness, self.dimensions))

