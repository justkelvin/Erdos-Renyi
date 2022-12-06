#!/usr/bin/env python3

import matplotlib.pyplot as plt
import networkx as nx

# Set the number of nodes in the network
n = 102

# Set the probability of connecting two nodes by changing this value.
p = 10**-3


# Generate the network
G = nx.erdos_renyi_graph(n, p)

# Compute the chain edges of the network
# Set the default weight for each edge to 1
for u, v in G.edges():
    G.edges[u, v]['weight'] = 1

# Compute the chain edges of the network
chain_edges = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == 1]


# Compute the average distance, aggregation coefficient, maximum degree, and minimum degree
# Find the connected components in the graph
components = nx.connected_components(G)

# Select the largest connected component
largest_component = max(components, key=len)

# Create a subgraph of the largest connected component
subgraph = G.subgraph(largest_component)

# Compute the average shortest path length for the subgraph
avg_dist = nx.average_shortest_path_length(subgraph)

# Compute the clustering coefficient for each node
clustering = nx.clustering(G)

# Compute the average clustering coefficient
avg_clustering = sum(clustering.values()) / len(clustering)

# The aggregation coefficient is the square of the average clustering coefficient
agg_coeff = avg_clustering ** 2
max_deg = max(G.degree, key=lambda x: x[1])
min_deg = min(G.degree, key=lambda x: x[1])

# Print the results
print("Chain edges:", chain_edges)
print("Average distance:", avg_dist)
print("Aggregation coefficient:", agg_coeff)
print("Maximum degree:", max_deg)
print("Minimum degree:", min_deg)

# Plot the network
# Compute the layout of the nodes in the graph
pos = nx.spring_layout(G)

# # Plot the graph using the computed layout
nx.draw(G, pos=pos, with_labels=True)
plt.show()