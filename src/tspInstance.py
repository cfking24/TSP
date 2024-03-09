import numpy as np

class tspInstance:
    def __init__(self):
        self.graph = None
        self.best_solution = None

    def reader(self, file_path):
        with open(file_path, 'r') as file:
            num_nodes = int(next(file).strip())
            self.graph = np.zeros((num_nodes, num_nodes))
            next(file)  # Skip the column headings
            for line in file:
                node1, node2, distance = line.split()
                node1 = int(node1) - 1
                node2 = int(node2) - 1
                distance = float(distance)
                self.graph[node1][node2] = distance
                self.graph[node2][node1] = distance  # Assuming the graph is undirected

    def solutionGen(self):
        if self.graph is None:
            print("Error: Graph not initialized.")
            return None

        # Generate a random permutation of the nodes
        solution = np.random.permutation(self.graph.shape[0])
        return solution

    def solutionCheck(self, solution):
        if self.graph is None:
            print("Error: Graph not initialized.")
            return None

        # Calculate the total distance of the solution
        total_distance = 0
        for i in range(len(solution) - 1):
            total_distance += self.graph[solution[i]][solution[i + 1]]
        total_distance += self.graph[solution[-1]][solution[0]]  # Add the distance from the last node to the first node

        return total_distance

    def bestSolution(self, solution):
        # Check if the solution is better than the current best solution
        current_best = self.solutionCheck(self.best_solution) if self.best_solution is not None else float('inf')
        solution_distance = self.solutionCheck(solution)

        if solution_distance < current_best:
            self.best_solution = solution
            return True

        return False