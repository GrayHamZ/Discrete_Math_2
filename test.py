import matplotlib.pyplot as plt
import networkx as nx

# Define the graph
G = nx.Graph()
G.add_nodes_from(["A", "B", "C", "D", "E", "F", "G"])
edgelist = [("A", "C", 10), ("A", "I", 5), ("C", "B", 20), ("C", "E", 15),("C", "D", 30), 
            ("B", "E", 25), ("I", "E", 40), ("E", "F", 35),("F", "G", 50), ("G", "E", 45)]
G.add_weighted_edges_from(edgelist)
minimum_spning_tree = nx.minimum_spanning_tree(G) # Implement Kruskal's algorithm by getting minimum spanning tree

# Draw the graph and minimum spanning tree
plt.figure(figsize=(10, 8))
pos = nx.planar_layout(G)
nx.draw(
    G, pos, edge_color='black', width=1, linewidths=1,
    node_size=500, node_color='pink', alpha=0.9,
    with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
nx.draw_networkx_edges(minimum_spning_tree, pos=pos, edge_color='pink', width=2)

plt.show()