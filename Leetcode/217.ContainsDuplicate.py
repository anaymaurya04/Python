def containDuplicate(nums):
    dup_map={}
    for num in nums:
        if num in nums:
            return True
        dup_map[num] = True
    return True

n=[1,2,3,4]
print(containDuplicate(n))