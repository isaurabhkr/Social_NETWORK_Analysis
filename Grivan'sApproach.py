import networkx as nx


def edge_to_remove(G):
	dict1=nx.edge_betweenness_centrality(G)
	list_of_tuples = dict1.items()
	list_of_tuples.sort(key=lambda x:x[1], reverse=True)
	return list_of_tuples[0][0]
	#returns a tuple (a,b)


def Girvan(G):
	c= nx.connected_component_subgraphs(G)
	#it returns the list of conneceted subgraphs
	#if length ie=s zero then the graph doesn't have anny connected components
	l=len(c)
	print("The Number of connected components are",l)

	while(l==1):
		G.remove_edge(*gde_to_remove(G))
		#((a,b)) --> (a,b)
		c= nx.connected_component_subgraphs(G)
		#it returns the list of conneceted subgraphs
		#if length ie=s zero then the graph doesn't have anny connected components
		l=len(c)
		print("The Number of connected components are",l)
	return c
	#returns graph


G=nx.barbell_graph(5,0)
ci = Girvan(G)

for i in ci:
	print(i.nodes())
	print('         ')