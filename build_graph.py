import networkx as nx

def build_graph(filename):
    G = nx.DiGraph()
    G.add_node("Start")
    G.add_node("Exit")  # Adding an Exit state
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    stack = []
    start = 1
    count = 0
    nobp = 0
    # Strips the newline character
    #print("Start")
    for line in Lines:
        count += 1  # Counting each line
        G.add_node("State " + str(count))  # Adding a new state
        if start:
            G.add_edge("Start", "State " + str(count))
            start = 0
        #print("State " + str(count) + ":"),
        for i in line.strip():
            #print(i),
            if (i == "{"):
                nobp += 1
                stack.append("State " + str(count))
                G.add_edge("State " + str(count), "State " + str(count + 1), edge_labels="True")
                continue
            if (i == "}"):
                temp = stack.pop()
                G.add_edge(temp, "State " + str(count + 1), edge_labels="False")
                G.add_edge("State " + str(count), temp, edge_labels="Loopback")
                continue
            G.add_edge("State " + str(count), "State " + str(count + 1))

        #print("")
        # print("Line{}: {}".format(count, line.strip()))
    #print("Exit")
    G.add_edge("State " + str(count), "Exit")
    return G;