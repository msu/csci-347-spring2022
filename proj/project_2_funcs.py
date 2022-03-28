import networkx as nx

# get_nodes: returns all the nodes in a graph represented as an edge list
def get_nodes(edgelist):
    nodes = []
    for pair in edgelist:
        if pair[0] not in nodes:
            nodes.append(pair[0])
        if pair[1] not in nodes:
            nodes.append(pair[1])
    return nodes

# num_nodes: return the number of nodes in a graph represented as an edge list
def num_nodes(edgelist):
    nodes = get_nodes(edgelist)
    n_nodes = len(nodes)
    return n_nodes

def betweenness_centrality(edgelist, v):
    nodes = get_nodes(edgelist)
    num_nodes = len(nodes)
    f = open('edgelist_g.txt','w')
    for p in edgelist:
        f.write(str(p[0])+' '+str(p[1]))
        f.write('\n')
    f.close()
    G=nx.read_edgelist("edgelist_g.txt", nodetype=int)
    bc_v = 0
    
    list_pairs = []
    
    for s in nodes:
        for t in nodes:
            p = (s,t)
            if p not in list_pairs:
                list_pairs.append(p)
            
            if s!=t and s!=v and v!=t:
                count_paths = 0
                sps = nx.all_shortest_paths(G,s,t)
                num_sps = 0
                for p in sps:
                    num_sps += 1
                    if v in p:
                        count_paths += 1
                bc_v += count_paths/float(num_sps)
    bc_v = bc_v/2

    return bc_v

def degree(G, node):
    count = 0
    for pair in G:
        if pair[0] == node or pair[1] == node:
            count += 1
    return count

def clustering_coefficient(G, node):
    neighbors = []
    
    for pair in G:
        if pair[0] == node :
            neighbors.append(pair[1])
        else:
            if pair[1] == node :
                neighbors.append(pair[0])
    
    num_neighbors = len(neighbors)
    num_possible_edges = (num_neighbors*(num_neighbors-1))/2
    #print('neighbors of ',node,': ',neighbors)
    edge_count = 0
    for pair in G:
        if pair[0] in neighbors and pair[1] in neighbors:
            edge_count += 1
            
    cc = edge_count/num_possible_edges
    return cc

def clust_coeff_graph(edge_list):
    nodes = []
    for pair in edge_list:
        if pair[0] not in nodes:
            nodes.append(pair[0])
        if pair[1] not in nodes:
            nodes.append(pair[1])
    
    sum_cc = 0
    for node in nodes:
        cc_node = clustering_coefficient(node)
        sum_cc += cc+node
    
    avg_cc = sum_cc/(float(len(nodes)))
    
    return avg_cc

def closeness(edgelist,node):
    nodes = get_nodes(edgelist)
    sum_spl = 0;
    for n in nodes:
        if n != node:
            shortest_path_length = nx.shortest_path_length(node, n)
            sum_spl += shortest_path_length
    return 1/sum_spl

#def betweenness_centrality(edgelist, v):
#    nodes = get_nodes(edgelist)
#    f = open('edgelist_g.txt','w')
#    for p in edgelist:
#        f.write(str(p[0])+' '+str(p[1]))
#        f.write('\n')
#    f.close()
#    G=nx.read_edgelist("edgelist_g.txt", nodetype=int)
#    bc_v = 0
#    for s in nodes:
#        for t in nodes:
#            if s!=t and s!=v and v!=t:
#                count_paths = 0
#                sps = nx.all_shortest_paths(G,s,t)
#                num_sps = len(sps)
#                for sp in sps:
#                    for edge in sp:
#                        if v in edge:
#                            count_paths += 1
#                bc_v += count_paths/num_sps
#    bc_v = bc_v/2
#
#	return bc_v
    
import numpy as np
def get_adjacency_matrix(edgelist):
	nodes = get_nodes(edgelist)
	nodes.sort()
	num_nodes = len(nodes)
	
	A = np.zeros((num_nodes, num_nodes))

	for node in nodes:
		for v in nodes:
			if (node, v) in edgelist:
				A[node-1][v-1] = 1
				A[v-1][node-1] = 1
	
	return A

def avg_shortest_path_length(edgelist):
	nodes = get_nodes(edgelist)

	f = open('edgelist_g.txt','w')
	for p in edgelist:
		f.write(str(p[0])+' '+str(p[1]))
		f.write('\n')
	f.close()
	G=nx.read_edgelist("edgelist_g.txt", nodetype=int)
	
	count_sps = 0
	sum_sp_lengths = 0
	for s in nodes:
		for t in nodes:
			if t!= s:
				count_sps += 1
				shortest_pl = nx.shortest_path_length(G,s,t)
				sum_sp_lengths += shortest_pl
	avg_spl = sum_sp_lengths/count_sps
	
	return avg_spl
 

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

# Test cases for number of vertices
print('\nTest cases for number of vertices:\n')
print('Graph 0: networkx number of vertices = ', g0.number_of_nodes())
print('Graph 0: number of vertices = ', num_nodes(graph_0))
print('Graph 1: networkx number of vertices = ', g1.number_of_nodes())
print('Graph 1: number of vertices = ', num_nodes(graph_1))
print('Graph 2: networkx number of vertices = ', g2.number_of_nodes())
print('Graph 2: number of vertices = ', num_nodes(graph_2))
print('Graph 3: networkx number of vertices = ', g3.number_of_nodes())
print('Graph 3: number of vertices = ', num_nodes(graph_3))
print('Graph 4: networkx number of vertices = ', g4.number_of_nodes())
print('Graph 4: number of vertices = ', num_nodes(graph_4))
print('Graph 5: networkx number of vertices = ', g5.number_of_nodes())
print('Graph 5: number of vertices = ', num_nodes(graph_5))
print('Graph 6: networkx number of vertices = ', g6.number_of_nodes())
print('Graph 6: number of vertices = ', num_nodes(graph_6))
print('Graph 7: networkx number of vertices = ', g7.number_of_nodes())
print('Graph 7: number of vertices = ', num_nodes(graph_7))
print('Graph 8: networkx number of vertices = ', g8.number_of_nodes())
print('Graph 8: number of vertices = ', num_nodes(graph_8))

# Test cases for degree function
print('\nTest cases for degree of a vertex:\n')
print('Graph 1: degree of node 2 = ',degree(graph_1, 2))
print('Graph 1: networkx degree of node 2 = ',g1.degree[2])
print('Graph 2: degree of node 2 = ',degree(graph_2, 2))
print('Graph 2: networkx degree of node 2 = ',g2.degree[2])
print('Graph 3: degree of node 2 = ',degree(graph_3, 2))
print('Graph 3: networkx degree of node 2 = ',g3.degree[2])
print('Graph 3: degree of node 3 = ',degree(graph_3, 3))
print('Graph 3: networkx degree of node 3 = ',g3.degree[3])
print('Graph 3: degree of node 6 = ',degree(graph_3, 6))
print('Graph 3: networkx degree of node 6 = ',g3.degree[6])
print('Graph 4: degree of node 25 = ',degree(graph_4, 25))
print('Graph 4: networkx degree of node 25 = ',g4.degree[25])
print('Graph 5: degree of node 4 = ',degree(graph_5, 4))
print('Graph 5: networkx degree of node 4 = ',g5.degree[4])
print('Graph 6: degree of node 3 = ', degree(graph_6,3))
print('Graph 6: networkx degree of node 3 = ',g6.degree[3])
print('Graph 7: degree of node 27 = ', degree(graph_7,27))
print('Graph 7: networkx degree of node 27 = ',g7.degree[27])

# Test cases for clustering coefficient function:
print('\nTest cases for clustering coefficient of a vertex:\n')
print('Graph 1: clustering coefficient of node 2 = ',clustering_coefficient(graph_1, 2))
print('Graph 1: clustering coefficient of node 2 = ',nx.clustering(g1, 2));
print('\n')

print('Graph 2: clustering coefficient of node 4 = ',clustering_coefficient(graph_2, 4))
print('Graph 2: clustering coefficient of node 4 = ',nx.clustering(g2, 4));
print('\n')

print('Graph 3: clustering coefficient of node 3 = ',clustering_coefficient(graph_3, 3))
print('Graph 3: clustering coefficient of node 3 = ',nx.clustering(g3, 3));

print('Graph 4: clustering coefficient of node 5 = ',clustering_coefficient(graph_4, 5))
print('Graph 4: clustering coefficient of node 5 = ',nx.clustering(g4, 5));

print('Graph 5: clustering coefficient of node 4 = ',clustering_coefficient(graph_5, 4))
print('Graph 5: clustering coefficient of node 4 = ',nx.clustering(g5, 4));
print('\n')

print('Graph 6: clustering coefficient of node 1 = ',clustering_coefficient(graph_6, 1))
print('Graph 6: clustering coefficient of node 1 = ',nx.clustering(g6, 1));
print('\n')

print('Graph 7: clustering coefficient of node 11 = ',clustering_coefficient(graph_7, 11))
print('Graph 7: clustering coefficient of node 11 = ',nx.clustering(g7, 11));
print('\n')

print('Graph 8: clustering coefficient of node 46 = ',clustering_coefficient(graph_8, 46))
print('Graph 8: clustering coefficient of node 46 = ',nx.clustering(g8, 46));
print('\n')

# test cases for betweenness centrality
print('\nTest cases for betweennesss centrality of a vertex:\n')
for v in range(1,7):
	print('graph 0: betweenness centrality of node ', v,' = ', betweenness_centrality(graph_0,v))
	
bc_nx = nx.betweenness_centrality(g0,normalized=False)
for v in g0.nodes():
	print('graph 0: nx betweenness centrality of node ', v,' = ', bc_nx[v])
 
for v in range(1,6):
    print('graph 1: betweenness centrality of node ', v,' = ', betweenness_centrality(graph_1,v))
    
bc_nx = nx.betweenness_centrality(g1,normalized=False)
for v in g1.nodes():
    print('graph 1: nx betweenness centrality of node ', v,' = ', bc_nx[v])

bc_nx = nx.betweenness_centrality(g6, normalized=False)
for v in range(8):
    print('graph 6: betweenness centrality of node ', v,' = ', betweenness_centrality(graph_6,v))
for v in g6.nodes():
    print('graph 6: nx betweenness centrality of node ', v,' = ', bc_nx[v])

bc_nx = nx.betweenness_centrality(g7, normalized=False)
print('graph 7: bc for node 23 = ', betweenness_centrality(graph_7,23))
print('graph 7: nx bc for node 23 = ', bc_nx[23])

bc_nx = nx.betweenness_centrality(g8, normalized=False)
print('graph 8: bc for node 39 = ', betweenness_centrality(graph_8,39))
print('graph 8: nx bc for node 39 = ', bc_nx[39])

# Test cases for adjacency matrix
print('\nTest cases for adjacency matrix:\n')
print('graph 0: adjacency matrix:\n')
print(get_adjacency_matrix(graph_0))
A = nx.adjacency_matrix(g0)
print('graph 0: networkx adjacency matrix: \n', A.todense())

print('graph 1: adjacency matrix:\n')
print(get_adjacency_matrix(graph_1))
A = nx.adjacency_matrix(g1)
print('graph 1: networkx adjacency matrix: \n', A.todense())

print('graph 2: adjacency matrix:\n')
print(get_adjacency_matrix(graph_2))
A = nx.adjacency_matrix(g2)
print('graph 2: networkx adjacency matrix: \n', A.todense())

print('graph 5: adjacency matrix:\n')
print(get_adjacency_matrix(graph_5))
A = nx.adjacency_matrix(g5)
print('graph 5: networkx adjacency matrix: \n', A.todense())

print('graph 6: adjacency matrix:\n')
print(get_adjacency_matrix(graph_6))
A = nx.adjacency_matrix(g6)
print('graph 6: networkx adjacency matrix: \n', A.todense())

# test cases for average shortest path length
print('\nTest cases for average shortest path length:\n')

print('average shortest path length of graph 0: ', avg_shortest_path_length(graph_0))
print('networkx shortest path length of graph 0: ', nx.average_shortest_path_length(g0))
print('average shortest path length of graph 2: ', avg_shortest_path_length(graph_2))
print('networkx shortest path length of graph 2: ', nx.average_shortest_path_length(g2))
print('average shortest path length of graph 3: ', avg_shortest_path_length(graph_3))
print('networkx shortest path length of graph 3: ', nx.average_shortest_path_length(g3))
print('average shortest path length of graph 4: ', avg_shortest_path_length(graph_4))
print('networkx shortest path length of graph 4: ', nx.average_shortest_path_length(g4))
print('average shortest path length of graph 5: ', avg_shortest_path_length(graph_5))
print('networkx shortest path length of graph 5: ', nx.average_shortest_path_length(g5))
print('average shortest path length of graph 6: ', avg_shortest_path_length(graph_6))
print('networkx shortest path length of graph 6: ', nx.average_shortest_path_length(g6))
print('average shortest path length of graph 7: ', avg_shortest_path_length(graph_7))
print('networkx shortest path length of graph 7: ', nx.average_shortest_path_length(g7))
print('graph_8 average shortest path length of graph 8: ', avg_shortest_path_length(graph_8))
print('g8 networkx shortest path length of graph 8: ', nx.average_shortest_path_length(g8))
