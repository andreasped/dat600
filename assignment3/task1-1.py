#        1  2  3  4  5  6
Adj =  [[0, 1, 0, 0, 0, 0],  # 1
        [0, 1, 1, 1, 0, 0],  # 2
        [1, 1, 0, 0, 1, 0],  # 3
        [0, 0, 0, 0, 1, 1],  # 4
        [0, 0, 1, 1, 0, 0],  # 5
        [0, 0, 0, 1, 0, 0]]  # 6


def adjacency_matrix_to_list(matrix):
    adj_list = {i + 1: [] for i in range(len(matrix))}
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                adj_list[i + 1].append(j + 1)
    
    return adj_list

adj_list = adjacency_matrix_to_list(Adj)

for key, value in adj_list.items():
    connections = " -> ".join(map(str, adj_list[key]))
    print(f"{key} -> {connections if connections else 'None'}")
