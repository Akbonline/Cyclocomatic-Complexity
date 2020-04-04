import networkx as nx

def Mccabe_Complexity(graph):
    return graph.number_of_edges() - graph.number_of_nodes() + 2 * nx.number_connected_components(graph)

if __name__ == '__main__':
    G = nx.Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_edge(1,2)
    print(Mccabe_Complexity(G))
    