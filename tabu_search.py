import random
import numpy as np

class TabuSearch:
    def __init__(self, tabu_tenure=10):
        self.tabu_list = []
        self.tabu_tenure = tabu_tenure
        
    def create_initial_solution(self):
        # Start with values that are likely to give a good solution
        return [20, 15, 25, 30]
    
    def evaluate_solution(self, solution):
        a, b, c, d = solution
        return abs(a + 2*b + 3*c + 4*d - 30)
    
    def get_neighbors(self, current_solution):
        neighbors = []
        
        for i in range(len(current_solution)):
            new_value = (current_solution[i] + 1) % 31
            neighbors.append(current_solution[:i] + [new_value] + current_solution[i+1:])
            
            new_value = (current_solution[i] - 1) % 31
            neighbors.append(current_solution[:i] + [new_value] + current_solution[i+1:])
            
        return neighbors
    
    def run(self, max_iterations=100):
        current_solution = self.create_initial_solution()
        best_solution = current_solution
        
        for iteration in range(max_iterations):
            neighbors = self.get_neighbors(current_solution)
            
            best_neighbor = None
            best_neighbor_value = float('inf')
            
            for neighbor in neighbors:
                if neighbor not in self.tabu_list:
                    value = self.evaluate_solution(neighbor)
                    if value < best_neighbor_value:
                        best_neighbor = neighbor
                        best_neighbor_value = value
            
            if best_neighbor is not None:
                current_solution = best_neighbor
                self.tabu_list.append(current_solution)
                
                if len(self.tabu_list) > self.tabu_tenure:
                    self.tabu_list.pop(0)
            
            current_value = self.evaluate_solution(current_solution)
            if current_value < self.evaluate_solution(best_solution):
                best_solution = current_solution.copy()
        
        return best_solution, self.evaluate_solution(best_solution)

if __name__ == "__main__":
    ts = TabuSearch()
    best_solution, fitness = ts.run()

    print(f"Best solution found: {best_solution}")
    print(f"Fitness value: {fitness}")