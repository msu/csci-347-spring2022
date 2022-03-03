# Test case graphs for Project 2: CSCI 347

g0 = nx.Graph()
g0.add_edge(1,2)
g0.add_edge(2,3)
g0.add_edge(2,4)
g0.add_edge(3,5)
g0.add_edge(4,5)
g0.add_edge(5,6)

graph_0 = [(1,2), (2,3), (2,4), (3,5),(4,5),(5,6)]

graph_1 = [(1,2), (2,3), (3,4), (4,5),(5,1)]
g1 = nx.Graph()
for edge in graph_1:
    g1.add_edge(edge[0], edge[1])

graph_2 = [(1,2),(1,3), (2,3),(2,4) ,(3,4), (4,5),(5,1)]
g2 = nx.Graph()
for edge in graph_2:
    g2.add_edge(edge[0], edge[1])

graph_3 = [(1,2),(1,3), (2,3),(2,4) ,(3,4),(3,6), (4,5),(5,1),(6,7),(6,8), (7,8), (8,9) ]
g3 = nx.Graph()
for edge in graph_3:
    g3.add_edge(edge[0], edge[1])

g4 = nx.path_graph(50)
graph_4 = []
for line in nx.generate_edgelist(g4, data=False):
    vi = int(line.split()[0])
    vj = int(line.split()[1])
    pair = (vi, vj)
    graph_4.append(pair)

g5 = nx.complete_graph(7)
graph_5 = []
for line in nx.generate_edgelist(g5, data=False):
    vi = int(line.split()[0])
    vj = int(line.split()[1])
    pair = (vi, vj)
    graph_5.append(pair)

g6 = nx.cycle_graph(8)
graph_6 = []
for line in nx.generate_edgelist(g6, data=False):
    vi = int(line.split()[0])
    vj = int(line.split()[1])
    pair = (vi, vj)
    graph_6.append(pair)

n=200 # number of nodes for Barabasi-Albert graph
q=4 # number of edges each new node has in the generation process of BA graph

g7 = nx.barabasi_albert_graph(n, q, seed=34)
graph_7 = []
for line in nx.generate_edgelist(g7, data=False):
    vi = int(line.split()[0])
    vj = int(line.split()[1])
    pair = (vi, vj)
    graph_7.append(pair)


g8 = nx.erdos_renyi_graph(100,0.13, seed=15)
graph_8 = []
for edge in g8.edges():
    graph_8.append(edge)

