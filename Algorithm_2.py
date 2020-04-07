import networkx as nx


# Function calculates cyclomatic complexity of a graph representing code using algorithm 2
# Input:  A NetworkX graph
# Output:  An integer representing the cyclomatic complexity
# The formula:
#       CC = PN + 1
#   CC - cyclomatic complexity
#   PN - predicate node (parent node)
# Source:  https://0-ieeexplore.ieee.org.pacificatclassic.pacific.edu/document/1702388

def Algo_2_Complexity(graph):
    pn = 0

    for n in graph:
        if graph.out_degree(n) == 2:
            pn = pn + 1
    return pn


if __name__ == '__main__':
    G = nx.DiGraph()

    G.add_node(1)
    G.add_node(2)
    G.add_node(3)

    G.add_edge(1, 2)
    G.add_edge(1, 3)

    G.add_node(4)
    G.add_node(5)

    G.add_edge(3, 4)
    G.add_edge(3, 5)

    G.add_node(6)

    G.add_edge(2, 6)

    pn = Algo_2_Complexity(G)

    cc = pn + 1

    print("Algorithm 2 yields the CC of:", cc)
