import random
import numpy as np

class GeneticAlgorithm:
    def __init__(self, population_size=6, generations=50):
        self.population_size = population_size
        self.generations = generations
        
    def create_initial_population(self):
        return [random.sample(range(0, 31), 4) for _ in range(self.population_size)]
    
    def fitness_function(self, chromosome):
        a, b, c, d = chromosome
        return abs(a + 2*b + 3*c + 4*d - 30)
    
    def select_parents(self, population):
        total_fitness = sum(self.fitness_function(chromosome) for chromosome in population)
        selected = []
        
        for _ in range(2):
            r = random.uniform(0, total_fitness)
            current_sum = 0
            
            for i, (chromosome, fitness) in enumerate(zip(population, 
                [self.fitness_function(chromosome) for chromosome in population])):
                current_sum += fitness
                
                if current_sum > r:
                    selected.append(i)
                    break
                    
        return [population[i] for i in selected]
    
    def crossover(self, parent1, parent2):
        cut_point = random.randint(0, len(parent1)-1)
        child1 = parent1[:cut_point] + parent2[cut_point:]
        child2 = parent2[:cut_point] + parent1[cut_point:]
        return [child1, child2]
    
    def mutate(self, chromosome):
        for i in range(len(chromosome)):
            if random.random() < 0.1:
                chromosome[i] = random.randint(0, 30)
        return chromosome
    
    def run(self):
        population = self.create_initial_population()
        
        for generation in range(self.generations):
            new_population = []
            
            parents = self.select_parents(population)
            children = []
            
            for i in range(0, len(parents), 2):
                if i+1 < len(parents):
                    child1, child2 = self.crossover(parents[i], parents[i+1])
                    new_population.extend([child1, child2])
                    
            population = [self.mutate(chromosome) for chromosome in new_population]
            
        return max(population, key=self.fitness_function)

if __name__ == "__main__":
    ga = GeneticAlgorithm()
    best_solution = ga.run()
    
    print(f"Best solution found: {best_solution}")
    print(f"Fitness value: {ga.fitness_function(best_solution)}")