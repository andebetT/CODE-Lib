graph={}
def adding_node(node):
    if node in graph:
        print("the node is already present")
    else:
        graph[node]=[]
#for unweithed and undirected graph
def adding_edge_undirected_unweitghed(v1,v2):
    if v1 not  in graph:
        print("the node is not found")
    elif v2 not in graph:
        print("the node is not found")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
def adding_edge_undirected_weitghed(v1,v2,weight):
    if v1 not  in graph:
        print("the node is not found")
    elif v2 not in graph:
        print("the node is not found")
    else:
        graph[v1].append([v2,weight])
        graph[v2].append([v1,weight])
def adding_edge_directed_unweitghed(v1,v2):
    if v1 not  in graph:
        print("the node is not found")
    elif v2 not in graph:
        print("the node is not found")
    else:
        graph[v1].append(v2)
        #graph[v2].append(v1)
def delating_node_adjcent_list(node):
    if node not  in graph:
        print("the node is not found")
    else:
        graph.pop(node)
        for i in graph:
            list1=graph[i]
            if node in list1:
                list1.remove(node)
#delating node of a weigthed list
def delating_node_weithed_list(node):
    if node not in graph:
        print("the node is not found")
    else:
        graph.pop(node)
        for i in graph:
            list1=graph[i]
            for j in list1:
                if node==j[0]:
                    list1.remove(j)
                    break
#undirected unweigted graph  edge delation

def delating_edge(v1,v2):
    if v1 not  in graph:
        print("the node is not found")
    elif v2 not in graph:
        print("the node is not found")
    else:
        if v1 in graph[v2]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)
#delating weithed and undirected edge
def delating_edge_wethed(v1,v2,cost):
    if v1 not  in graph:
        print("the node is not found")
    elif v2 not in graph:
        print("the node is not found")
    else:
        temp=[v1,cost]
        temp1=[v2,cost]
        if temp in graph[v2]:
            graph[v1].remove(temp1)
            graph[v2].remove(temp)



print(adding_node("A"))
print(adding_node("B"))
print(adding_node("C"))
print(adding_node("D"))

print(adding_edge_undirected_unweitghed("A","B"))
print(adding_edge_directed_unweitghed("A","B"))
print(adding_edge_undirected_weitghed("A","B",500))
print(adding_edge_undirected_weitghed("C","D",100))
print(adding_edge_undirected_weitghed("E","F",1800))
print(graph)
print(delating_node_adjcent_list("A"))
print(delating_edge("A","B"))
print(delating_node_weithed_list("A"))
print(graph)
