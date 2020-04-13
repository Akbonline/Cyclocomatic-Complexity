import sys
import build_graph
import time
import McCabe_algo
import Algorithm_2
import paper_algorithm
import Algorithm_3
import networkx as nx
import csv

def time_mccabe(G,outFile):
    start = time.time()
    McCabe_algo.Mccabe_Complexity(G.to_undirected())
    end = time.time()
    return end - start

def time_algo2(G,outFile):
    start = time.time()
    Algorithm_2.Algo_2_Complexity(G)
    end = time.time()
    return end - start

def time_algo3(G,outFile):
    start = time.time()
    Algorithm_3.algo3(G)
    end = time.time()
    return end - start

def time_paper_algo(G,outFile):
    start = time.time()
    paper_algorithm.p_2(G)
    end = time.time()
    return end - start



def main():
    filename = sys.argv[1]
    num_runs = int(sys.argv[2])
    G = build_graph.build_graph(filename)
    out_prefix = filename.split(".")[0]

    mccabe = open(out_prefix + "_mccabe","a")
    algo2 = open(out_prefix + "_algo2", "a")
    algo3 = open(out_prefix + "_algo3", "a")
    paper = open(out_prefix + "_paper", "a")

    total_mccabe = 0
    total_algo2 = 0
    total_algo3 = 0
    total_paper = 0
    for i in range(num_runs):
        total_mccabe += time_mccabe(G,mccabe)
        total_algo2 += time_algo2(G,algo2)
        total_algo3 += time_algo3(G,algo3)
        total_paper += time_paper_algo(G,paper)

    mccabe.write(str(total_mccabe/num_runs))
    algo2.write(str(total_algo2/num_runs))
    algo3.write(str(total_algo3/num_runs))
    paper.write(str(total_paper/num_runs))

    mccabe.close()
    algo2.close()
    algo3.close()
    paper.close()

if __name__ == "__main__":
    main()