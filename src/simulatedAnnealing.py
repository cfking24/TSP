import numpy as np
import time
import matplotlib.pyplot as plt

class SimulatedAnnealing:
    def __init__(self, tsp_instance, initial_temperature=1000, cooling_rate=0.995, num_iterations=1000):
        self.tsp_instance = tsp_instance
        self.temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.num_iterations = num_iterations
        self.current_solution = None
        self.best_solution = None

    def generate_new_solution(self):
        # Generate a new solution by swapping two cities in the current solution
        new_solution = self.current_solution.copy()
        i, j = np.random.randint(0, len(new_solution), 2)
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        return new_solution

    def evaluate_solution(self, solution):
        return self.tsp_instance.solutionCheck(solution)

    def run(self, initial_solution=None, time_limit=None):
        # If an initial solution is provided, use it; otherwise, generate a random solution
        self.current_solution = initial_solution if initial_solution is not None else self.tsp_instance.solutionGen()
        self.best_solution = self.current_solution

        # Initialize a list to store the cost at each iteration
        costs = []

        start_time = time.time()

        for _ in range(self.num_iterations):
            # Check if the time limit has been reached
            if time_limit is not None and time.time() - start_time > time_limit:
                print("Time limit reached.")
                break

            new_solution = self.generate_new_solution()
            old_cost = self.evaluate_solution(self.current_solution)
            new_cost = self.evaluate_solution(new_solution)
            if new_cost < old_cost or np.random.rand() < np.exp((old_cost - new_cost) / self.temperature):
                self.current_solution = new_solution
                if new_cost < self.evaluate_solution(self.best_solution):
                    self.best_solution = new_solution

            # Save the cost of the current solution
            costs.append(self.evaluate_solution(self.current_solution))

            self.temperature *= self.cooling_rate

        return self.best_solution, costs

    def plot_costs(self, costs):
        plt.figure()
        plt.plot(costs)
        plt.title('Costs over time')
        plt.xlabel('Iteration')
        plt.ylabel('Cost')
        plt.show()
