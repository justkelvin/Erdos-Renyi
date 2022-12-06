# consider the erdos-renyi network model, write a program where 102 nodes are randomly connected with probability of p = 10-5. 103, 2x103 and other nodes, two 10-4,10-2 and so on.
# 1. Calculate the average distance, aggregation coefficient, maximum degree and minimum degree of the network.

import networkx as nx
import matplotlib.pyplot as plt
 
# Create the Erdos-Renyi network
G = nx.erdos_renyi_graph(102, 0.00001)
 
# Find the connected components in the graph
components = nx.connected_components(G)

# calculate the chain edges of the network
# chain_edges = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == 1]
for u, v in G.edges():
    G.edges[u, v]['weight'] = 1

# Compute the chain edges of the network
chain_edges = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == 1]

# Select the largest connected component
largest_component = max(components, key=len)

# Create a subgraph of the largest connected component
subgraph = G.subgraph(largest_component)

# Compute the average shortest path length for the subgraph
avg_dist = nx.average_shortest_path_length(subgraph)
 
# Calculate the aggregation coefficient
# agg_coeff = nx.aggregation_coefficient(G)
# Compute the clustering coefficient for each node
clustering = nx.clustering(G)

# Compute the average clustering coefficient
avg_clustering = sum(clustering.values()) / len(clustering)

# The aggregation coefficient is the square of the average clustering coefficient
agg_coeff = avg_clustering ** 2
 
# Calculate the maximum degree
max_degree = max(dict(G.degree).values())
 
# Calculate the minimum degree
min_degree = min(dict(G.degree).values())
# Print the results
print('Chain edges:', chain_edges)
print('Average distance:', avg_dist)
print('Aggregation coefficient:', agg_coeff)
print('Maximum degree:', max_degree)
print('Minimum degree:', min_degree)
 
# Plot the network
nx.draw(G, with_labels=True)
plt.show()
