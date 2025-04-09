from collections import defaultdict

def addEdge(adj, s, t):
    adj[s].append(t)

def dfsRecursive(adj, visited, s, stack=None):
    visited.add(s)
    for neighbor in adj[s]:
        if neighbor not in visited:
            dfsRecursive(adj, visited, neighbor, stack)
    if stack is not None:
        stack.append(s) 

def getFinishingOrder(graph):
    visited = set()
    stack = []
    
    for node in graph:
        if node not in visited:
            dfsRecursive(graph, visited, node, stack)

    return stack  

def reverseGraph(graph):
    reversed_graph = defaultdict(list)
    for node in graph:
        for neighbor in graph[node]:
            reversed_graph[neighbor].append(node)
    return reversed_graph

def findSccs(graph):
    finish_order = getFinishingOrder(graph)

    reversed_graph = reverseGraph(graph)

    visited = set()
    sccs = []

    while finish_order:
        node = finish_order.pop()
        if node not in visited:
            component = []
            dfsRecursive(reversed_graph, visited, node, component)
            sccs.append(component)

    return sccs

if __name__ == "__main__":
   graphNoSCC = {
    'A': ['B'],
    'B': [],
    'C': ['D'],
    'D': [],
    'E': ['F'],
    'F': ['G'],
    'G': []
}
   print("No strongly connected nodes: ", findSccs(graphNoSCC))

   graphAllConnected = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}
   print("Only strongly connected nodes: ", findSccs(graphAllConnected))
   
   graphSharedNodesSCC = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A'],
    'D': ['E'],
    'E': ['D']
}
   print("Some strongly connected nodes: ", findSccs(graphSharedNodesSCC))
