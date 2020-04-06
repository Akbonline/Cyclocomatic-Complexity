import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# Function calculates Cyclomatic complexity of a graph representing code
# Input: An adjacency matrix
# Output: Integer representing cyclomatic complexity
# Formula = Sum of all out degree - (number of nodes with out degree greater or equal to one) + 1
# Source: https://0-ieeexplore.ieee.org.pacificatclassic.pacific.edu/document/8229931
def paper_algorithm(adjMat):
    combMatr = adjMat * adjMat.transpose()
    print("Adj Matrix * Transpose")
    print(combMatr)
    outDegreeGtOne = []
    sum = 0;
    for i in range(len(combMatr)):
        sum += combMatr.item(i,i)
        if (combMatr.item((i,i)) >= 1):
            outDegreeGtOne.append(combMatr.item((i,i)))
    return (sum - len(outDegreeGtOne) + 1)

def main():
    adjMat = np.matrix('0 1 1 0 0; 0 0 1 0 0; 0 0 0 1 1; 0 0 1 0 0; 0 0 0 0 0')
    print("Original Adj Matric")
    print(adjMat)
    print("Cycolamtic Complexity",paper_algorithm(adjMat))


if __name__ == "__main__":
    main()