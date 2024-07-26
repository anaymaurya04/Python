def rearrangeElement(nums):
    pos =[]
    neg =[]
    for num in nums:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)
    i=0
    while 2*i < len(nums):
        nums[2*i] = pos[i]
        nums[2*i+1] = neg[i]
        i+=1
    return nums

print(rearrangeElement(nums=[1,2,-1,-2]))