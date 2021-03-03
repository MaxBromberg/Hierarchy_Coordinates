import numpy as np
import networkx as nx
import HierarchyCoordinates as hc

# base objects:
a = np.array([
    [0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
])

condensed_network_layers = hc.recursive_leaf_removal(nx.condensation(nx.from_numpy_matrix(a, create_using=nx.DiGraph)), from_top=False)
# G and \tilde{G}_1 in fig 14 (infographic) are he nets of condensed network layers
for net in condensed_network_layers:
    print(nx.to_numpy_array(net))

info_graphic_fwd_graph_entropy = [round(hc.infographic_graph_entropy(net, forward_entropy=True), 3) for net in condensed_network_layers]
info_graphic_bkwd_graph_entropy = [round(hc.infographic_graph_entropy(net), 3) for net in condensed_network_layers]

fwd_graph_entropy = [round(hc.graph_entropy(net, forward_entropy=True), 3) for net in condensed_network_layers]
bkwd_graph_entropy = [round(hc.graph_entropy(net), 3) for net in condensed_network_layers]

print("infrographic graph entropy (from fwd | bkwd ): {0} | {1}".format(info_graphic_fwd_graph_entropy, info_graphic_bkwd_graph_entropy))
print("graph entropy (from fwd | bkwd ): {0} | {1}".format(fwd_graph_entropy, bkwd_graph_entropy))
