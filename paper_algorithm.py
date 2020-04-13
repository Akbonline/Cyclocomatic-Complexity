import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# Function calculates Cyclomatic complexity of a graph representing code
# Input: An adjacency matrix
# Output: Integer representing cyclomatic complexity
# Formula = Sum of all out degree - (number of nodes with out degree greater or equal to one)
# Source: https://0-ieeexplore.ieee.org.pacificatclassic.pacific.edu/document/8229931
def paper_algorithm(adjMat):
    combMatr = np.dot(adjMat, adjMat.transpose())
    outDegreeGtOne = []
    sum = 0;
    for i in range(len(combMatr)):
        sum += combMatr.item(i,i)
        if (combMatr.item((i,i)) >= 1):
            outDegreeGtOne.append(combMatr.item((i,i)))

    return (sum - len(outDegreeGtOne))

# Function calculates Cyclomatic complexity of a graph representing code
# Input: A network X graph
# Output: Integer representing cyclomatic complexity
# Formula = Sum of all out degree - (number of nodes with out degree greater or equal to one)
# Source: https://0-ieeexplore.ieee.org.pacificatclassic.pacific.edu/document/8229931
def p_2(G):
    sum = 0;
    outDegreeGtOne = []
    for n in G:
        od = G.out_degree(n)
        sum += od
        if od >= 1:
            outDegreeGtOne.append(n)

    return sum - len(outDegreeGtOne)

def main():
    adjMat = np.matrix('0 1 1 0 0; 0 0 1 0 0; 0 0 0 1 1; 0 0 1 0 0; 0 0 0 0 0')
    print("Original Adj Matric")
    print(adjMat)
    print("Cycolamtic Complexity",paper_algorithm(adjMat))


if __name__ == "__main__":
    main()