from src.tspInstance import tspInstance

class Greedy2OptMove:
    def __init__(self, tsp_instance):
        self.tsp_instance = tsp_instance

    def run(self, initial_solution):
        # Copy the initial solution
        solution = initial_solution.copy()

        cyclesVisited = 0

        # Initialize a variable to keep track of improvements
        improvement = True

        # While the solution is improving
        while improvement:
            # Assume no improvement will be found in this iteration
            improvement = False

            # Iterate over pairs of indices (i, j) with i < j
            for i in range(len(solution) - 1):
                for j in range(i + 2, len(solution) + (i != 0)):
                    cyclesVisited += 1
                    
                    # Calculate the change in distance if we reverse the subpath from i to j
                    old_distance = self.tsp_instance.graph[solution[i - 1]][solution[i]] + self.tsp_instance.graph[solution[j - 1]][solution[j % len(solution)]]
                    new_distance = self.tsp_instance.graph[solution[i - 1]][solution[j - 1]] + self.tsp_instance.graph[solution[i]][solution[j % len(solution)]]

                    # If the change in distance is negative, reverse the subpath from i to j
                    if new_distance < old_distance:
                        solution[i:j] = reversed(solution[i:j])
                        improvement = True

        return solution, cyclesVisited