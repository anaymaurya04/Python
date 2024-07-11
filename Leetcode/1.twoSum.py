def twoSum(nums, target):
    complement_map = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        
        if complement in complement_map:
            return [complement_map[complement], index]
        
        complement_map[num] = index
    
    return []

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  