from sklearn.cluster import KMeans
from src.tspInstance import tspInstance
from src.greedy import GreedyAlgorithm
import numpy as np

class GreedyEuclid:
    def __init__(self, tsp_instance, n_clusters):
        self.tsp_instance = tsp_instance
        self.n_clusters = n_clusters
        self.cluster_solutions = []

    def cluster_nodes(self):
        # Ensure the distance matrix is a numpy array
        if not isinstance(self.tsp_instance.graph, np.ndarray):
            self.tsp_instance.graph = np.array(self.tsp_instance.graph)

        # Create a KMeans object
        kmeans = KMeans(n_clusters=self.n_clusters)

        # Fit the KMeans object to the data
        kmeans.fit(self.tsp_instance.graph)

        # Get the cluster assignments for each node
        labels = kmeans.labels_

        return labels

    def run(self):
        # Cluster the nodes
        cluster_labels = self.cluster_nodes()

        # For each cluster, run the greedy algorithm
        for i in range(self.n_clusters):
            # Create a subgraph for this cluster
            cluster_nodes = np.where(cluster_labels == i)[0]
            subgraph = self.tsp_instance.graph[np.ix_(cluster_nodes, cluster_nodes)]

            # Create a new TSP instance for this cluster
            cluster_tsp = tspInstance()
            cluster_tsp.graph = subgraph

            # Run the greedy algorithm on this cluster
            greedy = GreedyAlgorithm(cluster_tsp)
            cluster_solution = greedy.run()

            # Append the solution of this cluster
            self.cluster_solutions.append(cluster_solution)

        # Link the clusters together
        # This part is left as an exercise

        return self.cluster_solutions
    
    def link_clusters(self):
        # Create a "reduced" distance matrix where each node represents a cluster
        reduced_graph = np.zeros((self.n_clusters, self.n_clusters))
        for i in range(self.n_clusters):
            for j in range(i+1, self.n_clusters):
                # Find the minimum distance between cluster i and cluster j
                min_distance = np.min(self.tsp_instance.graph[np.ix_(self.cluster_solutions[i], self.cluster_solutions[j])])
                reduced_graph[i][j] = min_distance
                reduced_graph[j][i] = min_distance  # Assuming the graph is undirected

        # Create a new TSP instance for the reduced graph
        reduced_tsp = tspInstance()
        reduced_tsp.graph = reduced_graph

        # Solve the reduced TSP instance using the greedy algorithm
        greedy = GreedyAlgorithm(reduced_tsp)
        cluster_order = greedy.run(mode=1)

        # The cluster_order now gives an order in which to visit the clusters
        return cluster_order
    
    def get_overall_solution(self, cluster_order):
        # Initialize an empty list to hold the overall solution
        overall_solution = []

        # Iterate over the cluster_order
        for cluster_index in cluster_order:
            # Get the solution for this cluster
            cluster_solution = self.cluster_solutions[cluster_index]

            # Append the nodes in this cluster to the overall solution
            overall_solution.extend(cluster_solution)

        return overall_solution