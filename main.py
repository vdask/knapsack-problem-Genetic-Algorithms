import numpy as np
import random as rd
from random import randint
import matplotlib.pyplot as plt


#random initializing the list of items
number_range = np.arange(1, 11) #chromosomes length
kg = np.random.randint(1, 10, size = 10) # random arary for kilograms
price = np.random.randint(1, 750, size = 10) # random array for prices
max_kg = 300
print('Items Weights Prices')
for i in range(number_range.shape[0]):
    print('  {0}      {1}       {2}'.format(number_range[i], kg[i], price[i]))

 #Population size and initial population
pop_number = 10
pop_size = (pop_number, number_range.shape[0])
# print('Population size = {}'.format(pop_size))
initial_pop = np.random.randint(2, size = pop_size)
initial_pop = initial_pop.astype(int)
num_gens = 800
# print('Initial population: \n{}'.format(initial_pop))

#fitness function
def fitness_function(kg, price, pop, threshold):
    fitness = np.empty(pop.shape[0])
    for i in range(pop.shape[0]):
        sum1 = np.sum(pop[i] * price)
        sum2 = np.sum(pop[i] * kg)
        if sum2 <= threshold:
            fitness[i] = sum1
        else :
            fitness[i] = 0
    return fitness.astype(int)

#Selecting the fittest individuals for crossover
def selection_function(fitness, num_parents, pop): #num_parents (half population)
    fitness = list(fitness)
    parents = np.empty((num_parents, pop.shape[1]))
    for i in range(num_parents):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        #print("this is max_fitness_position", max_fitness_idx)
        parents[i,:] = pop[max_fitness_idx[0][0], :] #thesi pou vrethike optimum solution apo population matrix append to parents
        fitness[max_fitness_idx[0][0]] = -9999
    return parents

#Crossover function
def crossover_function(parents, num_offsprings):
    offsprings = np.empty((num_offsprings, parents.shape[1]))
    crossover_point = int(parents.shape[1]/2) #one point crossover
    crossover_rate = 0.9

    for i in range(num_offsprings):
        parent1_index = i%parents.shape[0]
        parent2_index = (i+1)%parents.shape[0]

        x = rd.random()
        if x > crossover_rate:

            parent1_index = i%parents.shape[0]
            parent2_index = (i+1)%parents.shape[0]
            offsprings[i,0:crossover_point] = parents[parent1_index,0:crossover_point]
            offsprings[i,crossover_point:] = parents[parent2_index,crossover_point:]
        else:
            parent1_index = i % parents.shape[0]
            parent2_index = (i+1)%parents.shape[0]
    return offsprings


#Mutation function
def mutation_function(offsprings):
    mutants = np.empty(offsprings.shape)
    mutation_rate = 0.09
    for i in range(mutants.shape[0]):
        rnd = rd.random()
        mutants[i,:] = offsprings[i,:]
        if rnd > mutation_rate:
            continue
        int_rnd = randint(0,offsprings.shape[1]-1)
        if mutants[i,int_rnd] == 0 :
            mutants[i,int_rnd] = 1
        else :
            mutants[i,int_rnd] = 0
    return mutants

#Optimization funtion
def optimize_function(kg, price, pop, pop_size, num_gens, threshold):
    parameters, fitness_history = [], []
    num_parents = int(pop_size[0]/2)
    num_offsprings = pop_size[0] - num_parents
    for i in range(num_gens):
        fitness = fitness_function(kg, price, pop, threshold)
        fitness_history.append(fitness)
        parents = selection_function(fitness, num_parents, pop)
        offsprings = crossover_function(parents, num_offsprings)
        mutants = mutation_function(offsprings)
        pop[0:parents.shape[0], :] = parents
        pop[parents.shape[0]:, :] = mutants

    print('Last generation: \n{}\n'.format(pop))
    fitness_last_gen = fitness_function(kg,price, pop, threshold)
    print('Fitness of the last generation: \n{}\n'.format(fitness_last_gen))
    max_fitness = np.where(fitness_last_gen == np.max(fitness_last_gen))
    parameters.append(pop[max_fitness[0][0], :])
    return parameters, fitness_history


parameters, fitness_history = optimize_function(kg, price, initial_pop, pop_size, num_gens, max_kg)
print('Οptimized parameters:\n{}'.format(parameters))
selected_items = number_range * parameters
print('\n Selected items')
for i in range(selected_items.shape[1]):
  if selected_items[0][i] != 0:
     print('{}'.format(selected_items[0][i]))

fitness_mo = [np.mean(fitness) for fitness in fitness_history]
fitness_max = [np.max(fitness) for fitness in fitness_history]
plt.plot(list(range(num_gens)), fitness_mo, color = "cyan")
plt.plot(list(range(num_gens)), fitness_max, color = "red")
plt.legend()
plt.xlabel('generations')
plt.ylabel('fitness')
plt.show()
#print(np.asarray(fitness_history).shape)