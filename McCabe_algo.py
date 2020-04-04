import networkx as nx

# Function calculates Cyclomatic Complexity of a graph representing code
# Input:  A NetworkX graph
# Output:  AN integer
# The formula:
#       # of edges + # of nodes + 2 * # of connected components in the graph
# Source:  https://0-ieeexplore.ieee.org.pacificatclassic.pacific.edu/document/1702388
def Mccabe_Complexity(graph):
    return graph.number_of_edges() - graph.number_of_nodes() + 2 * nx.number_connected_components(graph)

if __name__ == '__main__':
    G = nx.Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_edge(1,2)
    print(Mccabe_Complexity(G))
    