#python function to addd new node of a graph using adjecency matrix method
def add_node(v):
    global node_count
    if v in nodes:
        print("the node is already present")
    else:
        node_count+=1
        nodes.append(v)
        for i in graph:
            i.append(0)
        temp=[]
        for j in range(node_count):
            temp.append(0)
        graph.append(temp)
#method for adding edge for udirected and unweitghted graph
def adding_edge(v1,v2):
    if v1 not in nodes:
        print(" the node v1 is not present in the graph")
    elif v2 not in nodes:
        print("the node v2 is not present in graph")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=1
        graph[index2][index1] = 1
# we can use this method for undirected and weithd graph by adding weigtht value in function
def adding_edge_weight(v1,v2,weight):
    if v1 not in nodes:
        print( " the node v1 is not presenet in the graph")
    elif v2 not in nodes:
        print("the node v2 is not found in graph")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=weight
        graph[index2][index1] =weight
#this method is used to add edge for directed  and unweigthed graph
def adding_edge_directed(v1,v2):
    if v1 not in nodes:
        print(" the node v1 is not present in the graph")
    elif v2 not in nodes:
        print("the node v2 is not found in graph")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=1
        #graph[index2][index1] = 0
#deltaing node using adjecency matrix method
def delating_node(node):
    global node_count
    if node not in nodes:
        print("the node is not found")
    else:
        index_val=nodes.index(node)
        node_count=node_count-1
        nodes.remove(node)
        graph.pop(index_val)
        for i in graph:
            i.pop(index_val)


def delating_edge(v1,v2):
    if v1 not in nodes:
        print(" the node v1 is not presenet in the graph")
    elif v2 not in nodes:
        print("the node v2 is not found in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        graph[index2][index1] = 0
#delating node using adjecency list method




def print_in_matrix_form():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3"),end=" ")
        print()
node_count = 0
nodes = []
graph = []
add_node("A")
add_node("B")
add_node("C")
add_node("D")
#print(nodes)
#print(graph)
print(adding_edge("A","B"))
print(print_in_matrix_form())
print(adding_edge_weight("A","B",23))
print(adding_edge_directed("A","C"))
#print(delating_node("A"))
print(nodes)
print(print_in_matrix_form())
#print(delating_edge("A","B"))
print(delating_node("A"))
print(nodes)
print(print_in_matrix_form())
