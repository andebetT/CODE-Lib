
def adding_node(node):
    if node in graph:
        print("the node is already present")
    else:
        graph[node]=[]
#for unweithed and undirected graph
def adding_edge_undirected_unweitghed(v1,v2):
    if v1 not in graph:
        print("the node is not found")
    elif v2 not in graph:
        print("the node is not found")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
#traversing tree using DFS algorithm in adjecency list
'''def dfs(node,visited,graph):
    if node not in graph:
        print("the node is not in graph")
    else:
        if node not in visited:
            print(node)
            visited.add(node)
            for i in graph[node]:
                dfs(i,visited,graph)
visited=set()'''
graph={}
#dfs using itrative method
def dfsitrative(node,graph):
    visited=set()
    if node not in graph:
        print("the node is not found")
        return
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)




print(adding_node("A"))
print(adding_node("B"))
print(adding_node("C"))
print(adding_node("D"))
print(adding_edge_undirected_unweitghed("A","B"))
print(adding_edge_undirected_unweitghed("B","C"))
print(adding_edge_undirected_unweitghed("A","D"))
print(graph)
#print(dfs("K",visited,graph))
print(dfsitrative("A",graph))

