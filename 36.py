def longest_increasing_subsequence(nums):
    if not nums:
        return 0
    dp = [1]*len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

lst = list(map(int, input("Enter the list of numbers separated by space: ").split()))
print("Length of Longest Increasing Subsequence:", longest_increasing_subsequence(lst))
