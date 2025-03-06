import random


def generate_items(n, max_weight, max_value):
    return [(random.randint(1, max_weight), random.randint(1, max_value)) for _ in range(n)]


def knapsack_01(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Find selected items
    w = capacity
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(items[i - 1])
            w -= items[i - 1][0]
    
    return dp[n][capacity], selected


def fractional_knapsack(items, capacity):
    items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    selected = []
    
    for weight, value in items:
        if capacity >= weight:
            selected.append((weight, value, 1))  # Fully take the item
            capacity -= weight
            total_value += value
        else:
            fraction = capacity / weight
            selected.append((weight, value, fraction))  # Take fraction of item
            total_value += value * fraction
            break
    
    return total_value, selected


if __name__ == "__main__":
    num_items = int(input("Enter number of items: "))
    max_capacity = int(input("Enter knapsack capacity (kg): "))
    max_weight = 20
    max_value = 100
    
    items = generate_items(num_items, max_weight, max_value)
    print("Generated items (kg, price):", items)
    
    # 0-1 Knapsack
    value_01, selected_01 = knapsack_01(items, max_capacity)
    print("\n0-1 Knapsack Solution:")
    print("Maximum price:", value_01)
    print("Selected items (kg, price):", selected_01)
    
    # Fractional Knapsack
    value_frac, selected_frac = fractional_knapsack(items, max_capacity)
    print("\nFractional Knapsack Solution:")
    print("Maximum price:", value_frac)
    print("Selected items (kg, price, fraction):", selected_frac)
