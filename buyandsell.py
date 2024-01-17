def maxProfit(A):
    if not A or len(A) < 2:
        return 0
    
    min_price = A[0]
    max_profit = 0

    for price in A:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

# Example 1
A1 = [1, 2]
result1 = maxProfit(A1)
print(result1)  # Output: 1

# Example 2
A2 = [1, 4, 5, 2, 4]
result2 = maxProfit(A2)
print(result2)  # Output: 4
