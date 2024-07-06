
def maxFrequency(self, nums, k):
    left = 0
    right = 0
    total = 0
    res = 0
    nums.sort()
    while right < len(nums):
        total += nums[right]
        while nums[right] * (right - left + 1) > total + k:
            total -= nums[left]
            left += 1

        res = max(res, right - left + 1)
        right += 1
    return res
