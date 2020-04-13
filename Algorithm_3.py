import networkx as nx

def algo3(G):
    count = 0
    for n in G:
        if G.out_degree(n) > 1:
            count += 1
    return count
