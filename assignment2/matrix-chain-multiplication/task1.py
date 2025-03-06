import sys

def matrix_chain_order(p):
    n = len(p) - 1                   # Number of matrices
    m = [[0] * n for _ in range(n)]  # Cost table
    s = [[0] * n for _ in range(n)]  # Split table

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = sys.maxsize    # Large value

            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k + 1  # Store (k+1) instead of k to start indexing from 1 in s table

    return m, s

# Recursively reconstructs the optimal parenthesization.
def print_optimal_parens(s, i, j):
    if i == j:
        return f"A{i+1}"  # Matrix names are 1-based
    else:
        return f"({print_optimal_parens(s, i, s[i][j] - 1)} * {print_optimal_parens(s, s[i][j], j)})"

if __name__ == "__main__":
    # The 5 matrices with the dimensions: 10x5, 5x2, 2x8, 8x3, 3x20
    p = [10, 5, 2, 8, 3, 20]

    m, s = matrix_chain_order(p)
    print("Minimum number of multiplications:", m[0][len(p)-2])

    print("\nCost table:")
    for row in m:
        print(row)

    print("\nSplit table (1-based indexing, unused values as 0):")
    for row in s:
        print(row)

    print("\nOptimal Parenthesization:", print_optimal_parens(s, 0, len(p)-2))
