import matplotlib.pyplot as plt
import networkx as nx

nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
edges = [(1, 2, 55), (1, 7, 106), (2, 3, 79), (2, 7, 104), (3, 4, 112), (3, 5, 98), (3, 8, 110), (4, 6, 58), (5, 6, 139), (5, 9, 131), 
         (5, 12, 126), (6, 12, 69), (6, 13, 140), (6, 20, 135), (7, 17, 97), (7, 10, 101), (7, 8, 85), (8, 9, 83), (8, 11, 70), (8, 14, 141), 
         (9, 12, 136), (10, 11, 105), (11, 16, 106), (11, 17, 99), (12, 13, 109), (12, 14, 140), (13, 15, 141), (13, 20, 138), (14, 15, 122), 
         (14, 16, 128), (15, 20, 102), (16, 19, 141), (16, 20, 139), (16, 18, 136), (17, 18, 74), (18, 19, 93)]

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

mst = nx.minimum_spanning_tree(G)

pos = nx.spring_layout(G)

# Define node colors
node_colors = ['green'] * len(nodes)

# Define edge colors
edge_colors = ['red' if edge in mst.edges else 'black' for edge in G.edges]

nx.draw(G, pos, with_labels=True, node_color=node_colors)
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2)
nx.draw_networkx_edge_labels(G, pos, edge_labels={edge[:2]: edge[2] for edge in edges})

plt.show()
