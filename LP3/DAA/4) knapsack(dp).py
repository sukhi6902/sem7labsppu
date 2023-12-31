# Write a program to solve a 0-1 Knapsack problem using dynamic programming strategy.
def knapsack_0_1(values, weights, capacity):
    n = len(values)
    # Create a table to store the maximum values for different subproblems
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the table using dynamic programming
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Find the items included in the knapsack
    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    return dp[n][capacity], selected_items

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value, selected_items = knapsack_0_1(values, weights, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
