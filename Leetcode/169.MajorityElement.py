def majorityElement(nums):
    count_map={}
    for num in nums:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1
    majority = max(count_map, key= count_map.get)
    return majority
    

print(majorityElement(nums=[1,1,1,1,3,3,3]))