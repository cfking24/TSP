from src.greedy import GreedyAlgorithm
from src.tspInstance import tspInstance
from src.greedyEuclid import GreedyEuclid

tsp = tspInstance()
tsp.reader('C:\\Users\\Conor King\\Documents\\School\\EEC 289Q\\TSP\\TSP\\data\\1000_euclidianDistance.txt') 

# Define the number of clusters for the GreedyEuclid algorithm
n_clusters = 10  # Adjust this value based on your specific use case

# Create a GreedyEuclid object
greedy_euclid = GreedyEuclid(tsp, n_clusters)

# Run the GreedyEuclid algorithm
cluster_solutions = greedy_euclid.run()

# Link the clusters together
cluster_order = greedy_euclid.link_clusters()

# Get the overall solution
overall_solution = greedy_euclid.get_overall_solution(cluster_order)

# Print the overall solution
print(overall_solution)

# Check the total distance of the overall solution
total_distance = tsp.solutionCheck(overall_solution)
print(f'Total distance: {total_distance}')