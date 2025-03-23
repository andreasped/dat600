from collections import deque

# BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    bfs_result = []
    
    print(f"Starting BFS from node: {start}")
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            bfs_result.append(node)
            print(f"Visited: {node}, Queue: {list(queue)}")
            queue.extend(neigh for neigh in sorted(graph[node]) if neigh not in visited)
    
    print("BFS Complete")
    print("BFS Result:", " -> ".join(bfs_result))

# DFS
def dfs(graph, node, visited, start_finish, time, finish_order):
    time[0] += 1
    start_finish[node] = (time[0], None)
    print(f"Visiting {node} (Start Time: {time[0]})")
    
    visited.add(node)
    
    for neighbor in sorted(graph[node]):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, start_finish, time, finish_order)
    
    time[0] += 1
    start_finish[node] = (start_finish[node][0], time[0])
    print(f"Finishing {node} (Finish Time: {time[0]})")
    finish_order.append(node)


graph = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E', 'F'],
    'D': ['E', 'F'],
    'E': ['F', 'G', 'J'],
    'F': ['B', 'G', 'H', 'J'],
    'G': [],
    'H': ['I'],
    'I': [],
    'J': ['I']
}

# Run BFS
bfs(graph, 'A')

# Run DFS with start and finish times
visited = set()
start_finish_times = {}
time = [0]
finish_order = []

print("\nDFS Traversal with Start/Finish Times:")
dfs(graph, 'A', visited, start_finish_times, time, finish_order)

print("\nStart/Finish Times:")
for node, (start, finish) in start_finish_times.items():
    print(f"{node}: Start = {start}, Finish = {finish}")

# Print Finished DFS Order (Reverse of the Finish Order List)
print("\nDFS Finished Order:")
print(" -> ".join(reversed(finish_order)))