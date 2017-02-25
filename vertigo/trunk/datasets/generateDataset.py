import networkx as nx
import matplotlib.pyplot as plt
import string
# def RandomLetter():
#
#     string.ascii_letters
#     import random
#     letter = random.choice(string.ascii_lowercase)
#     return letter
# # erdos renyi graph
# # generate a graph which has n=20 nodes, probablity p = 0.2.
# ER = nx.random_graphs.erdos_renyi_graph(20, 0.2)
# PW = nx.powerlaw_cluster_graph(20,3,0)
#  # the shell layout
# pos = nx.shell_layout(ER)
# NER = []
# for e in nx.to_edgelist(ER):
#     T = (e[0],e[1],RandomLetter())
#     NER.append(T)
# print (NER)
# nx.draw(ER, pos, with_labels = False, node_size = 30)
# plt.show()

query = "a.b.c.d"
querylist=query.split("+", query.count(".", 0, len(query)))
print (querylist)

query1 ="a[2,3].h.(b+c+d.(e+f+g+t)+u).a[2,3].(b+c+d+e.(f+g))).y.(i+9)"

l2 = []
l3=[]
def SortString(queryyy):
    queryy = queryyy.replace(".","")
    queryy = queryy.replace(" ","")
    numberOfB = 0
    index = 0
    l = []
    l1=[]
    l2.clear()
    for i, ch in enumerate(queryy):
        if ch == "(":
            if numberOfB==0:
                if len(l)==0:
                    l.append(queryy[index:i])
                else:
                    for item in l:
                        l1.append(item  + queryy[index+1:i])
                    l.clear()
                    for item in l1:
                        l.append(item)
                    l1.clear()
                index = i
            numberOfB=numberOfB+1

        if ch ==")":
            if numberOfB==1:
                for item in l:
                    l1.append(item+queryy[index+1:i])
                index = i
                l.clear()
                for item in l1:
                    l.append(item)
                l1.clear()
            numberOfB=numberOfB-1
        if ch == "+":
            if numberOfB==1:
                for item in l:
                    l1.append(item+queryy[index+1:i])
                index = i
        if i==len(queryy)-1:
            for item in l:
                l1.append(item  + queryy[index+2:i+1])
            l.clear()
            for item in l1:
                l.append(item)
            l1.clear()
    for item in l:
        l2.append(item)

        #print(ch, '(%d)' % i)

l4=[]
l5=[]
SortString(query1)
print(l2)
def finalsort():
    for item in l2:
        if item.count("(")==0:
            l4.append(item)
        else:
            l3.append(item)


    while len(l3)!=0:
        for a in range(len(l3)):
            SortString(l3[a])
            for item in l2:
                if item.count("(") == 0:
                    l4.append(item)
                else:
                    l5.append(item)
        l3.clear()
        for item in l5:
            l3.append(item)
        l5.clear()
finalsort()

print(l4)
#print(l3)