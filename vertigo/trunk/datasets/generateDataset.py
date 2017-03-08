import networkx as nx
import matplotlib.pyplot as plt
import string

def ShowGraph():
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
    querylist=query.split("+", query.count(".", 0, len(query)))
    print (querylist)

    query1 ="a[2,3].h.(b+c+d.(e+f+g+t)+u).a[2,3].(b+c+d+e.(f+g))).y.(i+9)"



  ############################################################################################################
def QueryToWords(query1):
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
    l6=[]
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



    #print(l3)

    #query = "a[2,4]bc[2,5]d[2,3]"
    #query = "qwa[2,4]bc[2,5]d[2,3]"
    #query = "a[2,4]bc[2,5]d[2,3]fg"
    def repeatsort(query):
        index=0
        q=[]
        if query.count("[")!=0:
            for i, ch in enumerate(query):
                if ch == "[":
                    q.append(query[index:i+5])
                    index=i+5
            if index != len(query):
                q.append(query[index:len(query)])
        q1=[]
        q2=[]
        for item in q:
            if item.count("[") != 0:
                if len(q1)==0:
                    for i in range(int(item[len(item)-4]),int(item[len(item)-2])+1):
                        q1.append(item[0:len(item) - 5])
                        for ii in range(i-1):
                            q1[len(q1)-1] = q1[len(q1)-1] + item[len(item) - 6]
                else:
                    for n in range(int(item[len(item)-2])+1-int(item[len(item)-4])):
                        for e in q1:
                            q2.append(e)
                    index1 =0

                    for i in range(int(item[len(item)-4]),int(item[len(item)-2])+1):
                        for x in range(len(q1)):
                            for ii in range(i):
                                if ii ==0:
                                    q2[index1] = q2[index1] + item[0:len(item) - 5]
                                else:
                                    q2[index1] = q2[index1] + item[len(item) - 6]
                            index1 = index1 +1
                    q1.clear()
                    for it in q2:
                        q1.append(it)
                    q2.clear()
            else:
                if len(q1)==0:
                    q1.append(item)
                else:
                    for u in range(len(q1)):
                        q1[u - 1] = q1[u - 1] + item

        for f in q1:
            l6.append(f)
    #    print(q1)
    #    print(q)
    SortString(query1)
    #print(l2)
    finalsort()

    #print(l4)
    for item in l4:
        repeatsort(item)
    print(l6)

QueryToWords("a[2,3].h.(b+c+d.(e+f+g+t)+u).a[2,3].(b+c+d+e.(f+g))).y.(i+9)");