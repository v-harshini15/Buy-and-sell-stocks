Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e, buy one and sell one share of the
stock), design an algorithm to find the maximum profit.
Return the maximum possible profit.
Problem Constraints
0 <= len(A) <= 7e5
1 <= A[i] <= 1e7
Input Format
The first and the only argument is an array of integers, A.
Output Format
Return an integer, representing the maximum possible profit.
Example Input
Input 1:
A = [1, 2]
Input 2:
A = [1, 4, 5, 2, 4]
Example Output
Output 1:
1
Output 2:
4
Initialize min_price to the first stock price and max_profit to 0.

Iterate through the array of stock prices.

Update min_price to be the minimum encountered so far.

Calculate the potential profit by subtracting min_price from the current stock price.

Update max_profit to be the maximum value obtained so far.

The final max_profit is the result.

In the example with A = [1, 2], the algorithm determines that buying at day 1 and selling at day 2 yields a profit of 1.

In the example with A = [1, 4, 5, 2, 4], the algorithm determines that buying at day 1 and selling at day 3 yields a profit of 4, which is the maximum possible profit.

