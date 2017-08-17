import networkx as nx

def edge_to_remove(G):
   dict1 = nx.edge_betweenness_centrality(G)
   list_of_tuples =  dict1.items()
   #print(list_of_tuples)
   list_list=list(sorted(list_of_tuples, key=lambda x:x[1],reverse=True))
   #need to convert list-of_tuples to list
   return list_list[0][0]         
   #will be returning tuple(a,b) a is source
 
def girvan(G):
    c = list(nx.connected_component_subgraphs(G))   
    l = len(c)
    print('The no. of connected components are',l)
    
    while(l==1):
        G.remove_edge(*edge_to_remove(G))#((a,b))-->(a,b)
        c = list(nx.connected_component_subgraphs(G))
        l = len(c)
        print ('The no. of connected componenets are',l)
    return c

print('The Barbell Graph \n')
G=nx.barbell_graph(5,0)
c = girvan(G)

for i in c:
  print(i.nodes())
  print('......... The Number of Nodes are .........', i.number_of_nodes())

print('\n\n')
print('The Karate Graph \n')
H=nx.karate_club_graph()
c=girvan(H)

for i in c:
  print(i.nodes())
  print('......... The Number of Nodes are .........', i.number_of_nodes())
