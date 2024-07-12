def rotate(nums, k):
    n = len(nums)
    k = k % n
    arr=nums[-k:] + nums[:-k]
    for i in range (n):
        nums[i]=arr[i]
    return arr
        