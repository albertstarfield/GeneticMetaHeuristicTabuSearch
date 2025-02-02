# Genetic Algorithm and Tabu Search: A Comparative Implementation

## Introduction
This project implements and compares two metaheuristic optimization techniques: Genetic Algorithms (GAs) and Tabu Search. Both are used to find approximate solutions for complex problems, but they operate on different principles. This project demonstrates their application to a specific mathematical optimization problem and visualizes their convergence.

## Problem Definition
The goal is to find a combination of four integer values (a, b, c, d), each between 0 and 30 inclusive, that minimizes the absolute difference of the expression `a + 2*b + 3*c + 4*d - 30`. In other words, we are trying to find values that make the expression as close to 30 as possible.

## What is a Genetic Algorithm?
A Genetic Algorithm is an evolutionary algorithm inspired by natural selection. It works by:
- Maintaining a population of potential solutions (chromosomes), each representing a set of four integer values.
- Evaluating the "fitness" of each chromosome based on how close it brings the expression to the target value of 30.
- Selecting pairs of "fitter" chromosomes as parents.
- Generating new chromosomes ("children") through crossover and mutation operations:
   - **Crossover:** Combines genetic information from parents.
   - **Mutation:** Introduces small, random changes in a chromosome.
- Repeating this process over multiple generations, expecting to find better solutions.

### Genetic Algorithm Implementation Details:
- **Encoding:** Each potential solution is represented as a list of four integers `[a, b, c, d]`.
- **Fitness Function:** Calculates the absolute difference `abs(a + 2*b + 3*c + 4*d - 30)`. The aim is to minimize this value.
- **Selection:** Uses a fitness-proportionate selection mechanism to choose parents.
- **Crossover:** Performs one-point crossover to create children.
- **Mutation:** Randomly changes one or more values in a chromosome with a low probability.
- **Convergence Tracking:** Tracks the best fitness value at each generation.
- **Plotting:** Generates a plot showing fitness convergence over generations.

## What is Tabu Search?
Tabu Search is a metaheuristic optimization technique that:
- Uses a "tabu list" to avoid revisiting recently explored solutions, preventing the algorithm from getting stuck in local optima.
- Explores the solution space by considering "neighboring" solutions (solutions with one value changed by 1).
- Makes moves, even if they are not strictly improving, to escape from local optima.

### Tabu Search Implementation Details:
- **Initial Solution:** Starts with an initial solution, in our case, `[20, 15, 25, 30]`.
- **Evaluation:** Same as GA, calculates the absolute difference `abs(a + 2*b + 3*c + 4*d - 30)`.
- **Neighborhood:** Generates neighbors by incrementing or decrementing a single value in the solution list.
- **Tabu List:** Stores visited solutions.  A new neighbor is only accepted if not in the tabu list. The list has a limited size (tabu tenure).
- **Convergence Tracking:** Tracks the best fitness value at each iteration.
- **Plotting:** Generates a plot showing fitness convergence over iterations.

## Implementation Considerations
- Both algorithms are particularly useful for:
  - Complex optimization problems
  - Problems with multiple local optima
  - Cases where exact solutions are computationally expensive to find
- Both are implemented to specifically find values that make the equation `a + 2*b + 3*c + 4*d - 30` equal to 30.
- Plots are generated to visualize the optimization process for each algorithm

## Usage Examples
The `onefile.ipynb` contains the complete implementations of both Genetic Algorithm and Tabu Search. You can run this file directly to see the results and the convergence plots.

## How To Run:
- Ensure that you have Python 3.6 or higher installed along with `numpy` and `matplotlib`.
- Save the content of `onefile.ipynb` into a `.py` file (e.g., `optimization.py`)
- Run the python script through the command line: `python optimization.py`
- The output will include:
    - The best solution found by each algorithm, as a list of four integers (a, b, c, d).
    - The corresponding fitness value for each solution
    - Two plots showing the fitness over iterations/generations for each algorithm

## References
[1] Denny Hermawanto, "Genetic Algorithm for Solving Simple Mathematical Equality Problem" (The core concept for GA is referenced from this paper.)