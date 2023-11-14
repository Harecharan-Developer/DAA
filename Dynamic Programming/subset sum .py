
def subset_sum(arr, target):
    n = len(arr)
    dp = [[False] * (target + 1) for _ in range(n+1)]
    
    # Base case: we can always make a sum of 0 with an empty subset
    for i in range(n+1):
        dp[i][0] = True
    
    # Fill the dp table
    for i in range(1, n+1):
        for j in range(1, target+1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
    
    # If there is no subset that makes up the target sum, return an empty list
    if not dp[n][target]:
        return []
    
    # Find the subset that makes up the target sum
    subset = []
    i, j = n, target
    while i > 0 and j > 0:
        if dp[i-1][j]:
            i -= 1
        elif dp[i][j]:
            subset.append(arr[i-1])
            j -= arr[i-1]
            i -= 1
    
    return subset[::-1]

# Driver code
arr = [3, 34, 4, 12, 5, 2]
target = 9
print(subset_sum(arr, target)) # Output: [4, 5]
