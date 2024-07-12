def missingNumber(nums):
    n= len(nums)
    arr_sum = 0
    n_sum = (n*(n+1))//2
    for i in range(n):
        arr_sum += nums[i]
    n_sum = n_sum - arr_sum
    return n_sum