import time
import random
import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

def parse_xml(xml_string):
    # parse the whole xml file an dgenerate the distance metrix out of it
    root = ET.fromstring(xml_string)
    vertices = root.findall(".//vertex")
    
    num_vertices = len(vertices)
    distance_matrix = np.zeros((num_vertices, num_vertices))
    
    for i, vertex in enumerate(vertices):
        edges = vertex.findall(".//edge")
        for edge in edges:
            neighbor_index = int(edge.text)
            cost = float(edge.get("cost"))
            distance_matrix[i, neighbor_index] = cost
    
    return distance_matrix

def log_data(iteration, fitness, convergence_curve):
    with open("log.csv", "a") as file:
        file.write(f"{iteration},{fitness}\n")

convergences = {}

def plot_convergence(convergence_curve, population, tournament):
    convergences[f'Population_{population}_Tournament_{tournament}'] = convergence_curve

def draw_chart(data, country):
    # Plotting
    plt.figure(figsize=(10, 6))

    for config, convergence_curve in data.items():
        iterations = range(1, len(convergence_curve) + 1)
        plt.plot(iterations, convergence_curve, label=config)

    plt.title('Convergence Curves for Different Configurations for {}'.format(country))
    plt.xlabel('Iteration')
    plt.ylabel('Fitness')
    plt.legend()
    plt.show()

def initialize_population(size, num_locations):
    # Generate an initial population of random solutions
    population = [np.random.permutation(num_locations) + 1 for _ in range(size)]
    return population

def evaluate_fitness(solution, distance_matrix):
    # Calculate the fitness of a solution based on the provided cost formula
    n = len(solution)
    cost = sum(distance_matrix[solution[i] - 1, solution[(i + 1) % n] - 1] for i in range(n))
    return cost

def tournament_selection(population, tournament_size, distance_matrix):
    # Perform tournament selection to choose a parent
    selected_candidates = random.sample(population, tournament_size)
    fitness_values = [evaluate_fitness(candidate, distance_matrix) for candidate in selected_candidates]
    return selected_candidates[np.argmin(fitness_values)]

def single_point_crossover(parent_a, parent_b):
    # Implement single-point crossover
    crossover_point = random.randint(1, len(parent_a) - 1)
    child_a = np.hstack((parent_a[:crossover_point], parent_b[crossover_point:]))
    child_b = np.hstack((parent_b[:crossover_point], parent_a[crossover_point:]))
    return child_a, child_b

def swap_mutation(solution):
    # Implement swap mutation
    mutation_points = random.sample(range(len(solution)), 2)
    solution[mutation_points[0]], solution[mutation_points[1]] = (
        solution[mutation_points[1]],
        solution[mutation_points[0]],
    )
    return solution

def replace_worst(population, new_solution, distance_matrix):
    # Replace the worst solution in the population with the new solution
    fitness_values = [evaluate_fitness(candidate, distance_matrix) for candidate in population]
    worst_index = np.argmax(fitness_values)
    population[worst_index] = new_solution

def evolutionary_algorithm(distance_matrix, population_size=100, tournament_size=10, max_evaluations=10000):
    population = initialize_population(population_size, len(distance_matrix))
    convergence_curve = []

    evaluations = 0
    start_time = time.time()

    while evaluations < max_evaluations:
        parent_a = tournament_selection(population, tournament_size, distance_matrix)
        parent_b = tournament_selection(population, tournament_size, distance_matrix)

        child_a, child_b = single_point_crossover(parent_a, parent_b)

        child_a = swap_mutation(child_a)
        child_b = swap_mutation(child_b)

        replace_worst(population, child_a, distance_matrix)
        replace_worst(population, child_b, distance_matrix)

        evaluations += 2  # Two new solutions are generated in each iteration

        # Log data for analysis
        best_solution = min(population, key=lambda x: evaluate_fitness(x, distance_matrix))
        best_fitness = evaluate_fitness(best_solution, distance_matrix)
        convergence_curve.append(best_fitness)
        log_data(evaluations, best_fitness, convergence_curve)

    end_time = time.time()

    # Retrieve the best solution found
    best_solution = min(population, key=lambda x: evaluate_fitness(x, distance_matrix))
    best_fitness = evaluate_fitness(best_solution, distance_matrix)

    # Plot the convergence curve
    plot_convergence(convergence_curve, population_size, tournament_size)

    return best_solution, evaluate_fitness(best_solution, distance_matrix)

if __name__ == '__main__':
    with open("burma14.xml", 'r') as burma_file:
        burma_data = burma_file.read()
        
    # Parse XML and get the distance matrix
    D_BURMA = parse_xml(burma_data)

    with open("brazil58.xml", 'r') as brazil_file:
        brazil_data = brazil_file.read()
        
    # Parse XML and get the distance matrix
    D_BRAZIL = parse_xml(brazil_data)

    population_sizes = [50, 100, 200]

    tournament_sizes = [5, 10, 20]

    for population_size in population_sizes:
        for tournament_size in tournament_sizes:
            print('-----------------------------------------------------------------------------------------------------------------------')
            print(f'Population Size: {population_size} \nTournament Size: {tournament_size} \n\n')
            best_solution, best_fitness = evolutionary_algorithm(D_BURMA, population_size=population_size, tournament_size=tournament_size, max_evaluations=10000)
            print("Best Solution for burma:", best_solution)
            print("Best Fitness for burma:", best_fitness)
    
    draw_chart(convergences, "Burma")
    convergences = {}

    for population_size in population_sizes:
        for tournament_size in tournament_sizes:
            print('\n')
            best_solution, best_fitness = evolutionary_algorithm(D_BRAZIL, population_size=population_size, tournament_size=tournament_size, max_evaluations=10000)
            print("Best Solution for brazil:", best_solution)
            print("Best Fitness for brazil:", best_fitness)
            print('-----------------------------------------------------------------------------------------------------------------------\n\n')
    
    
    draw_chart(convergences, "Brazil")
    convergences = {}