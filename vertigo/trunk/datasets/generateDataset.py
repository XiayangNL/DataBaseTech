import networkx as nx
import matplotlib.pyplot as plt
import string
def RandomLetter():

    string.ascii_letters
    import random
    letter = random.choice(string.ascii_lowercase)
    return letter
# erdos renyi graph
# generate a graph which has n=20 nodes, probablity p = 0.2.
ER = nx.random_graphs.erdos_renyi_graph(20, 0.2)
PW = nx.powerlaw_cluster_graph(20,3,0)
 # the shell layout
pos = nx.shell_layout(ER)
NER = []
for e in nx.to_edgelist(ER):
    T = (e[0],e[1],RandomLetter())
    NER.append(T)
print (NER)
nx.draw(ER, pos, with_labels = False, node_size = 30)
plt.show()

query = "a.b.c.d"
query.split(query=".", num =query.count(".", beg=0, end=len(query)))
print (query)