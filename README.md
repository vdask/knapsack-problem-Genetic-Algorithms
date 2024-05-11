# knapsack-problem-Genetic-Algorithms
Knapsack Problem Solver using Genetic Algorithm
This project implements a genetic algorithm to solve the knapsack problem, a classic optimization problem in computer science. The knapsack problem involves selecting a subset of items with the maximum combined value while staying within a given weight constraint.

# Overview
The program generates a random set of items with corresponding weights and values. It then uses a genetic algorithm to evolve a population of potential solutions over multiple generations. The algorithm iteratively selects the fittest individuals, performs crossover and mutation operations, and evaluates the fitness of each solution until an optimal or near-optimal solution is found.

# Requirements
Python 3.x
NumPy
Matplotlib


# Parameters
number_range: Range of item indices.
kg: Array of item weights.
price: Array of item values.
pop_number: Population size.
num_gens: Number of generations.
max_kg: Maximum weight allowed in the knapsack.
Results
Upon execution, the program outputs the optimized parameters (selected items) and their corresponding fitness values. Additionally, a plot illustrating the average and maximum fitness values across generations is generated.

# Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for any improvements or bug fixes.

# License
This project is licensed under the MIT License. See the LICENSE file for details.
