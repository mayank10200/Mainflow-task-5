def fibonacci(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

n = int(input("Enter the value of n to find the nth Fibonacci number: "))
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
