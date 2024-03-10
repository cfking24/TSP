class GreedyAlgorithm:
    def __init__(self, tsp_instance):
        self.tsp_instance = tsp_instance
        self.current_solution = None
        self.best_solution = None

    def run(self, mode=0):
        if mode == 0:
            # If mode is 0, run the algorithm as normal
            self.current_solution = self.run_from_node(0)
        elif mode == 1:
            # If mode is 1, try each node as the starting node
            best_distance = float('inf')
            for initial_node in range(len(self.tsp_instance.graph)):
                solution = self.run_from_node(initial_node)
                distance = self.tsp_instance.solutionCheck(solution)
                if distance < best_distance:
                    best_distance = distance
                    self.current_solution = solution

        self.best_solution = self.current_solution
        return self.best_solution

    def run_from_node(self, initial_node):
        # Start from the initial node
        solution = [initial_node]
        remaining_nodes = set(range(len(self.tsp_instance.graph))) - set(solution)

        while remaining_nodes:
            last_node = solution[-1]
            next_node = min(remaining_nodes, key=lambda node: self.tsp_instance.graph[last_node][node])
            solution.append(next_node)
            remaining_nodes.remove(next_node)

        return solution

