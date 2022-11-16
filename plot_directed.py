"""
==============
Directed Graph
==============

Draw a graph with directed edges using a colormap and different node sizes.

Edges have different colors and alphas (opacity). Drawn using matplotlib.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx

testFLights = [[10, 14, 43], [1, 12, 62], [4, 2, 62], [14, 10, 49], [9, 5, 29], [13, 7, 53], [4, 12, 90], [14, 9, 38], [11, 2, 64], [2, 13, 92], [11, 5, 42], [10, 1, 89], [14, 0, 32], [9, 4, 81], [3, 6, 97], [7, 13, 35], [11, 9, 63], [5, 7, 82], [13, 6, 57], [4, 5, 100], [2, 9, 34], [11, 13, 1], [14, 8, 1], [12, 10, 42], [2, 4, 41], [0, 6, 55], [
    5, 12, 1], [13, 3, 67], [3, 13, 36], [3, 12, 73], [7, 5, 72], [5, 6, 100], [7, 6, 52], [4, 7, 43], [6, 3, 67], [3, 1, 66], [8, 12, 30], [8, 3, 42], [9, 3, 57], [12, 6, 31], [2, 7, 10], [14, 4, 91], [2, 3, 29], [8, 9, 29], [2, 11, 65], [3, 8, 49], [6, 14, 22], [4, 6, 38], [13, 0, 78], [1, 10, 97], [8, 14, 40], [7, 9, 3], [14, 6, 4], [4, 8, 75], [1, 6, 56]]

seed = 13648  # Seed random number generators for reproducibility
# G = nx.random_k_out_graph(10, 3, 0.5, seed=seed)
G = nx.DiGraph()
for source, destination, weight in testFLights:
    G.add_edge(str(source), str(destination), weight=weight)

pos = nx.spring_layout(G, seed=seed)

node_sizes = [3 + 10 * i for i in range(len(G))]
M = G.number_of_edges()
edge_colors = range(2, M + 2)
edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
cmap = plt.cm.plasma

nodes = nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color="indigo")
edges = nx.draw_networkx_edges(
    G,
    pos,
    node_size=node_sizes,
    arrowstyle="->",
    arrowsize=10,
    edge_color=edge_colors,
    edge_cmap=cmap,
    width=2,
)
# set alpha value for each edge
# for i in range(M):
#     edges[i].set_alpha(edge_alphas[i])

# pc = mpl.collections.PatchCollection(edges, cmap=cmap)
# pc.set_array(edge_colors)

ax = plt.gca()
ax.set_axis_off()
# plt.colorbar(pc, ax=ax)
plt.show()
