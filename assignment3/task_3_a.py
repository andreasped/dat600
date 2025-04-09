def addEdge(adj, s, t):
    adj[s].append(t)

def dfsRecursive(adj, visited, s):
    visited.add(s)
    for i in adj[s]:
        if i not in visited:
            dfsRecursive(adj, visited, i)

def dfs(adj, s):
    visited = set()
    dfsRecursive(adj, visited, s)
    return visited

def reachAllNodes(start_node, graph):
    visited = dfs(graph, start_node)
    return len(visited) == len(graph)  

def findChampions(graph):
    champions = []
    nodes = list(graph.keys())
    for node in nodes:
        if reachAllNodes(node, graph):
            champions.append(node)
    if champions:
        return champions
    else:
        return "No champion exists."

if __name__ == "__main__":

    graphOneChampion= {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': ['E'],
        'E': []
    }

    graphNoChampions = {
        'A': ['B'],
        'B': ['C'],
        'C': [],
        'X': ['Y'],
        'Y': []
    }

    graphTwoChampions = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'C', 'D'],
        'C': [],
        'D': []
    }

    graphAllChampions = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['A', 'B', 'C']
    }

    oneChampion = findChampions(graphOneChampion)
    print("One champion graph", oneChampion)
    noChampion = findChampions(graphNoChampions)
    print("No champion graph: ", noChampion)
    twoChampions = findChampions(graphTwoChampions)
    print("Two champion graph: ", twoChampions)
    allChampions = findChampions(graphAllChampions)
    print("All champions graph: ", allChampions)

