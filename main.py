

import matplotlib.pyplot as plt
from PIL import Image
from World import World

population = 200
initial_infection_rate = 0.01
closeness = 20
dimensions = 1000
speed = 10
frequency = 15
turns = 1000
no_doctors = 5
train_new_doctor_frequency = 100
length_of_immunity = 10

if __name__ == '__main__':
    my_world = World(population, initial_infection_rate, closeness, dimensions, speed, frequency, turns, no_doctors, length_of_immunity)
    my_world.populate_world(population, initial_infection_rate, closeness)
    infectedCount = []
    healthyCount = []
    count = 0
    for count in range(turns):
        my_world.update_world(count)

        if count % frequency == 0:
            #plt.bar(['Infected', 'Not'], [int(my_world.get_number_infected()), int(my_world.get_number_well())])
            print(count)
            print("{}. Number infected: {}".format(count, my_world.get_number_infected()))
            print("{}. Number well: {}".format(count, my_world.get_number_well()))

        if count % train_new_doctor_frequency == 0:
            my_world.train_doctor()

        infected, healthy, doctors = my_world.create_coord_list()
        my_world.plot(infected[2:], healthy[2:], doctors, count)
        plt.show()


        infectedCount.append(my_world.get_number_infected())
        healthyCount.append(my_world.get_number_well())

        if my_world.get_number_well() == 0:
            print('Finished...')
            break
        count+= 1

    print(healthyCount)
    plt.plot(range(count), infectedCount)
    plt.show()

    frames = []
    for i in range(count):
        new_frame = Image.open('snapshots/{}.png'.format(i))
        frames.append(new_frame)


    frames[0].save('output.gif', format='GIF',
                   append_images=frames[:],
                   save_all=True,
                   duration=30, loop=1)
