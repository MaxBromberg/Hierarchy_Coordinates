import numpy as np
import networkx as nx
import HierarchyCoordinates as hc

a = np.array([
    [0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
])

print('(a) Treeness: {0} | Feedforwardness: {1}  | Orderability: {2}'.format(*np.round(hc.hierarchy_coordinates(a), 2)))

G = nx.condensation(nx.from_numpy_matrix(a, create_using=nx.DiGraph))
pruned_to_ground = hc.recursive_leaf_removal(G, from_top=True)
pruned_from_ground = hc.recursive_leaf_removal(G, from_top=False)
print("Pruned from top:")
for pruned_tree in pruned_to_ground:
    print(nx.to_numpy_array(pruned_tree))
print("Pruned from bottom:")
for pruned_tree in pruned_from_ground:
    print(nx.to_numpy_array(pruned_tree))
