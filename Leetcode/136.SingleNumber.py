# 136. Single Number
# Easy
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

def singleNumber(nums):
   single = 0
   for i in nums:
      single = single ^ i
      return single
   
nums =[2,4,5,5,4]
print(singleNumber(nums))