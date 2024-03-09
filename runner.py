from src.tspInstance import tspInstance
from src.simulatedAnnealing import SimulatedAnnealing

tspNonEu = tspInstance()
tspNonEu.reader('C:\\Users\\Conor King\\Documents\\School\\EEC 289Q\\TSP\\TSP\\data\\1000_euclidianDistance.txt')

initialSol = tspNonEu.solutionGen()
initialCost = tspNonEu.solutionCheck(initialSol)
print(initialCost)

sa = SimulatedAnnealing(tspNonEu,cooling_rate=0.995,num_iterations=1000)
best_solution, costs = sa.run()
#print(best_solution)

cost = tspNonEu.solutionCheck(best_solution)
print(cost)
sa.plot_costs(costs)