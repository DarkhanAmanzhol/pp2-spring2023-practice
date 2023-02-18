# Finding the minimum and maximum sum of n-1, 5=>4
def miniMaxSum(arr):
    minSum = sum(arr) - max(arr)
    maxSum = sum(arr) - min(arr)

    # Function can return more than one value!
    return minSum, maxSum

# Another approach with anonymous function - lambda
# miniMaxSum = lambda arr: (sum(arr) - max(arr), sum(arr) - min(arr))

minSum, maxSum = miniMaxSum([1,3,5,7,9])

print(f"Minimum sum is {minSum}\nMaximum sum is {maxSum}")